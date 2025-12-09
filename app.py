import streamlit as st
import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# ----------------------------------------
# 1. Train model once (when app starts)
# ----------------------------------------
@st.cache_resource
def train_attrition_model():
    # Load training data from hr_data.csv
    df = pd.read_csv("hr_data.csv")

    # Adjust this if your target column name is different
    target_col = "Attrition"

    # Map Yes/No to 1/0 (if needed)
    if df[target_col].dtype == "object":
        df[target_col] = df[target_col].map({"Yes": 1, "No": 0}).astype(int)

    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Identify numeric & categorical columns
    numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_features = X.select_dtypes(include=["object"]).columns.tolist()

    # Preprocessor (same as in your Colab)
    numeric_transformer = "passthrough"
    categorical_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    # Model (same as Colab)
    model = LogisticRegression(max_iter=1000)

    clf = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    # Train the model
    clf.fit(X, y)

    # Return trained pipeline and feature columns
    return clf, X.columns.tolist()


# Train once and reuse
clf, feature_columns = train_attrition_model()

# ----------------------------------------
# 2. Streamlit UI
# ----------------------------------------
st.title("Employee Attrition Prediction System")

st.write(
    """
    This app uses a machine learning model trained on **hr_data.csv** to predict
    employee attrition.

    - The model is trained automatically when the app starts.
    - Upload a CSV file with the **same columns** (features) as the training data.
    """
)

uploaded_file = st.file_uploader("Upload Employee CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data (first 5 rows)")
    st.dataframe(data.head())

    # Check for missing or extra columns
    missing_cols = [col for col in feature_columns if col not in data.columns]
    extra_cols = [col for col in data.columns if col not in feature_columns]

    if missing_cols:
        st.error(f"The following required columns are missing: {missing_cols}")
    else:
        if extra_cols:
            st.warning(
                f"The following extra columns will be ignored: {extra_cols}"
            )

        # Keep only the columns used for training, in the same order
        data_model = data[feature_columns]

        # Predict
        preds = clf.predict(data_model)
        proba = clf.predict_proba(data_model)[:, 1]

        result_df = data.copy()
        result_df["Attrition_Prediction"] = preds  # 1 = likely to leave, 0 = stay
        result_df["Attrition_Probability"] = proba

        st.subheader("Prediction Results (1 = High Attrition Risk)")
        st.dataframe(result_df.head())

        # Download button
        csv = result_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download predictions as CSV",
            data=csv,
            file_name="attrition_predictions.csv",
            mime="text/csv",
        )
else:
    st.info("Please upload a CSV file to get predictions.")

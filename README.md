# ✅ Employee Attrition Prediction System

This project predicts whether an employee is likely to leave the organization using Machine Learning.  
The application is built using **Python, Scikit-learn, and Streamlit** and deployed as a web application.

This project was developed as part of the **Algonive Internship Program**.

---

## 📌 Project Overview

Employee attrition refers to the number of employees who leave an organization over a period of time.  
This project helps HR teams predict employee attrition using historical data and machine learning techniques.

### The system:
- Trains a machine learning model using an HR dataset  
- Accepts a CSV file as input through a Streamlit web app  
- Predicts whether each employee is likely to leave  
- Provides prediction probability  
- Allows users to download prediction results  

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  
- Machine Learning (Logistic Regression)  

---

## 📂 Project Structure – Algonive Employee Attrition

```
Algonive_Employee_Attrition/
│
├── README.md
├── app.py
├── employee_attrition_colab.ipynb
├── hr_data.csv
├── requirements.txt
├── result1.png
└── result2.png
```

---

## 📊 Dataset Information

- **Dataset Name:** HR Employee Attrition Dataset  
- **Target Column:** `Attrition`  
- **Values:**  
  - `1` → Employee likely to leave  
  - `0` → Employee likely to stay  

---

## ⚙️ How the System Works

1. The model is trained automatically when the Streamlit app starts.  
2. The user uploads a new CSV file with employee details.  
3. The model predicts:  
   - Attrition status (`0` or `1`)  
   - Probability of attrition  
4. The user can download the prediction results as a CSV file.  

---

## ✅ Output Screenshots

- `result1.png` → App Interface & File Upload  
- `result2.png` → Prediction Output & Download Option  

---

## 🚀 How To Run the Project Locally

### Step 1: Install Required Libraries
```bash
pip install -r requirements.txt
```

### Step 2: Run the Streamlit App
```bash
streamlit run app.py
```

### Step 3: Open in Browser
```
http://localhost:8501
```

---

## 🌐 Deployment

The project can be deployed for free using **Streamlit Cloud** by connecting this GitHub repository.

---

## 👩‍💻 Developed By

- **Name:** Harshitha Mandala  
- **Course:** B.Tech – Computer Science and Engineering  
- **Internship:** Algonive Internship Program  
- **Project:** Employee Attrition Prediction System  

---

## 📜 License

This project is for educational and internship purposes only.

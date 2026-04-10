# 🔐 SmartSentry – AI-Powered Network Security System

SmartSentry is an intelligent cybersecurity platform that detects and classifies network attacks using Machine Learning models. It helps in identifying threats like DDoS, Ransomware, Port Scanning, and more in real-time.

---

## 🚀 Features

* 🔍 Detects multiple cyber attacks (DDoS, Ransomware, Password attacks, etc.)
* 🤖 Machine Learning models (Random Forest, KNN, SVM, DNN)
* 📊 CSV file upload and analysis
* 📈 Real-time prediction system
* 🔐 User authentication (Login/Register)
* 🛡️ Attack details with prevention tips

---

## 🧠 Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **Database:** MySQL
* **Machine Learning:** Scikit-learn, TensorFlow
* **Libraries:** Pandas, NumPy, Joblib

---

## 📁 Project Structure

```
SmartSentry/
│── models/                # ML models (.h5, .joblib)
│── static/                # CSS, JS, images
│── templates/             # HTML pages
│── app.py                 # Main Flask app
│── requirements.txt       # Dependencies
│── sql.sql                # Database setup
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/SmartSentry.git
cd SmartSentry
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Setup Database

* Create a MySQL database named `network`
* Import `sql.sql` file

### 4️⃣ Run the application

```
python app.py
```

### 5️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Supported Attack Types

* DDoS (ICMP, TCP, UDP)
* Password Attacks
* Port Scanning
* Ransomware
* Vulnerability Scanning

---

## 🎯 Future Enhancements

* 🌐 Live network traffic monitoring
* ☁️ Cloud deployment
* 📱 Mobile-friendly UI
* 🔔 Real-time alert system

---

👨‍💻 Project Team

Developed by Final Year B.Tech CSE students at Vasireddy Venkatadri Institute of Technology (VVIT):
Vankayala Bala Harshitha
Shaik Nayum Akthar
Yaragopu Mukesh
Shaik Abdul Rehaman

Under the Guidance of:
Dr. G. Sanjay Gandhi, Professor, CSE

---

## 📜 License

This project is for educational and research purposes.

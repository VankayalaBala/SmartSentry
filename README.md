🛡️ SmartSentry Cyber Threat Intelligence in IIoT

🏢 Overview

SmartSentry is a comprehensive Cyber Threat Intelligence (CTI) framework tailored for Industrial Internet of Things (IIoT) environments. The architecture integrates advanced machine learning algorithms and deep learning architectures to detect and mitigate cyber threats effectively, ensuring continuous operational integrity and resilience of IIoT infrastructures against attacks that can disrupt operations or compromise data integrity.
🏗️ Architecture Diagram
<img width="1325" height="763" alt="image" src="https://github.com/user-attachments/assets/990ca819-bb35-4bcc-8400-454b1767371e" />

🧱 Block Diagram
<img width="865" height="1027" alt="image" src="https://github.com/user-attachments/assets/27a9d6b3-e17b-43ae-a46a-25b40d335837" />

🗂️ ER Diagram (Entity-Relationship)
<img width="1420" height="637" alt="image" src="https://github.com/user-attachments/assets/6d337235-6a90-4542-aff1-670fe7ebf94a" />

🔄 DFD Diagram (Data Flow Diagram)
<img width="1585" height="800" alt="image" src="https://github.com/user-attachments/assets/78f4894e-2fee-45fe-984c-ea1203e0ab9c" />

<img width="1492" height="755" alt="image" src="https://github.com/user-attachments/assets/b92ecf6b-eaa7-4e81-bc6c-d4c3fa44c44e" />


🚀 Features

    Real-time Threat Detection: Preemptively identify and classify specific attack types.

    Advanced ML/DL Integration: Utilizes a suite of models including Random Forest (RF), Decision Tree (DT), Extra Tree Classifier (ETC), Support Vector Machine (SVM), k-Nearest Neighbor (KNN), and Deep Neural Network (DNN).

    Data Balancing: Implements the Synthetic Minority Over-sampling Technique (SMOTE) to handle class imbalances, which is crucial in IIoT anomaly detection.

    Threat Categorization: Detects specific attacks such as Port Scanning, DDoS ICMP, DDoS TCP, Ransomware, Vulnerability Scanner, and DDoS UDP.


👨‍💻 User Modules

    Home: Navigate the main interface.

    Load Dataset: Access and load live training data.

    Model Selection: Choose specific machine learning or deep learning models for attack detection.

    Prediction: Input network behavior attributes or data points to manually predict attack types.


🖥️ System Modules

    Accept Dataset: Retrieve and import datasets dynamically.

    Implement Models: Process data through the selected ML/DL architecture.

    Prediction Engine: Evaluate user-provided attributes against trained models.

    Generate Attack Types: Output the definitive predicted attack classification.


📱 Screens

    HomeScreen: Dashboard and main navigation interface.

    Dataset Upload Screen: Interface to load the Kaggle IIoT dataset.

    Model Analytics/Selection: Interface to choose between RF, DT, ETC, SVM, KNN, or DNN.

    Prediction Interface: Form to enter network attributes and receive real-time threat classifications.
    

🛠️ Technology Stack

    Operating System: Windows 7+

    Server-Side Scripting: Python 3.6+

    Web Framework: Flask (Python)

    Data Processing & Visualization: Pandas, NumPy, Matplotlib, OS

    Machine Learning Libraries: Scikit-Learn, Imbalanced-learn (for SMOTE)

    IDE: PyCharm / VSCode


## 🧠 Machine Learning & Deep Learning Models
SmartSentry evaluates network traffic against multiple trained algorithms to provide the most accurate threat classification. The models implemented include:

* **Random Forest (RF):** Used for its high accuracy and ability to handle complex, non-linear network data by creating an ensemble of decision trees.
* **Decision Tree (DT):** Provides a highly interpretable model for tracing the exact decision path of an identified threat.
* **Extra Trees Classifier (ETC):** Utilized for fast processing and reducing variance by strongly randomizing the cut-point choices.
* **Support Vector Machine (SVM):** Highly effective in high-dimensional spaces, creating optimal hyperplanes to separate normal traffic from malicious anomalies.
* **k-Nearest Neighbor (KNN):** A robust instance-based learning algorithm used for proximity-based anomaly detection.
* **Deep Neural Network (DNN):** A deep learning architecture designed to catch complex, layered patterns in modern IIoT cyberattacks.
* **SMOTE (Synthetic Minority Over-sampling Technique):** While not a classification model, this crucial preprocessing algorithm is used to balance the dataset, ensuring the models don't become biased toward majority classes (like normal traffic) and can accurately detect rare, high-severity attacks.

⚙️ Core Functionality

## 🚨 Detected Cyber Threats
SmartSentry is trained on the comprehensive Edge-IIoTset dataset, enabling it to accurately identify and classify high-severity anomalies and attacks specific to Industrial IoT networks. Our platform successfully detects:

* 🔍 **Port Scanning:** Identifies unauthorized reconnaissance attempts where attackers systematically probe the IIoT network for open ports and vulnerable services.
* 💥 **DDoS ICMP (Ping Flood):** Detects volumetric attacks that attempt to overwhelm IIoT devices and network bandwidth with massive amounts of ICMP echo requests.
* 🛑 **DDoS TCP (SYN Flood):** Recognizes TCP-based Denial of Service attacks designed to exhaust server connection state tables and render industrial systems unresponsive.
* 🌊 **DDoS UDP:** Spots UDP flood attacks aiming to overwhelm random ports on targeted IIoT hosts, causing critical systems to continuously check for applications that don't exist.
* 🔒 **Ransomware:** Flags anomalous network traffic patterns indicative of ransomware spreading laterally across the industrial network or communicating with command-and-control servers.
* 🩻 **Vulnerability Scanner:** Detects aggressive, automated scanning activities that attempt to find known exploits, misconfigurations, and weak points within the infrastructure.

  
🏃‍♂️ Quick Start
📋 Prerequisites

    Python 3.6 or higher

    Git
    

💻 Installation

Clone the repository:
Bash

git clone https://github.com/yourusername/SmartSentry.git
cd SmartSentry

Install dependencies:
Bash

pip install pandas numpy matplotlib flask scikit-learn imbalanced-learn

Start the application:
Bash

python app.py

📦 Project Structure

SmartSentry/
├── app.py                 # Main Flask application and routing
├── models/                # Pre-trained ML/DL models 
├── static/                # CSS, JavaScript, and image assets
└── templates/             # HTML templates (Home, Upload, Prediction, etc.)
    ├── index.html
    ├── load_dataset.html
    ├── model_selection.html
    └── prediction.html


📊 Data Management

    Dataset: Relies on the Edge-IIoTset dataset for training and testing.

    Source: Retrieves data from Kaggle (live_data_training.csv).

    Preprocessing: Uses Pandas and NumPy for manipulation, alongside SMOTE for robust handling of imbalanced network traffic anomalies.


🎯 Future Enhancements

    Real-time automated packet sniffing integration.

    Expansion to cover emerging zero-day vulnerabilities.

    Advanced graphical dashboards for live threat monitoring.


🏆 Academic Project

This application was developed as a B.Tech Major Project in Computer Science and Engineering at Vasireddy Venkatadri Institute of Technology (VVIT) by:

    Vankayala Bala Harshitha

    Shaik Nayum Akthar

    Yaragopu Mukesh

    Shaik Abdul Rehaman

Under the guidance of Dr. G. Sanjay Gandhi.


🛡️ SmartSentry Cyber Threat Intelligence in IIoT

🏢 Overview

SmartSentry is a comprehensive Cyber Threat Intelligence (CTI) framework tailored for Industrial Internet of Things (IIoT) environments. The architecture integrates advanced machine learning algorithms and deep learning architectures to detect and mitigate cyber threats effectively, ensuring continuous operational integrity and resilience of IIoT infrastructures against attacks that can disrupt operations or compromise data integrity.
🏗️ Architecture Diagram
🚀 Features
⚙️ Core Functionality

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

🏃‍♂️ Quick Start
📋 Prerequisites

    Python 3.6 or higher

    Git

💻 Installation

Clone the repository:

git clone https://github.com/yourusername/SmartSentry.git
cd SmartSentry

Install dependencies:

pip install pandas numpy matplotlib flask scikit-learn imbalanced-learn

Start the application:

python app.py

🛡️ SmartSentry Cyber Threat Intelligence in IIoT
🏢 Overview

SmartSentry is a comprehensive Cyber Threat Intelligence (CTI) framework tailored for Industrial Internet of Things (IIoT) environments. The architecture integrates advanced machine learning algorithms and deep learning architectures to detect and mitigate cyber threats effectively, ensuring continuous operational integrity and resilience of IIoT infrastructures against attacks that can disrupt operations or compromise data integrity.
🏗️ Architecture Diagram
<img width="1325" height="763" alt="image" src="https://github.com/user-attachments/assets/990ca819-bb35-4bcc-8400-454b1767371e" />

🚀 Features
⚙️ Core Functionality

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


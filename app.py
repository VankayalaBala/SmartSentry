from flask import Flask, url_for, redirect, render_template, request
import mysql.connector
import pandas as pd
import joblib
import numpy as np
from datetime import datetime
import json

app = Flask(__name__)

# Attack information and prevention tips dictionary
ATTACK_DETAILS = {
    'DDoS_ICMP': {
        'name': 'DDoS_ICMP',
        'full_name': 'Distributed Denial of Service (DDoS) using Internet Control Message Protocol (ICMP)',
        'description': 'ICMP flood attack where attackers overwhelm a target with ICMP echo request (ping) packets.',
        'severity': 'High',
        'icon': '🔄',
        'color': '#dc3545',
        'prevention_tips': [
            'Implement rate limiting on ICMP packets',
            'Use intrusion prevention systems (IPS)',
            'Configure firewalls to block unnecessary ICMP traffic',
            'Deploy DDoS mitigation services',
            'Monitor network traffic for unusual ICMP patterns'
        ]
    },
    'DDoS_TCP': {
        'name': 'DDoS_TCP',
        'full_name': 'Distributed Denial of Service (DDoS) using Transmission Control Protocol (TCP)',
        'description': 'TCP SYN flood attack that exploits the TCP three-way handshake to exhaust server resources.',
        'severity': 'High',
        'icon': '⚡',
        'color': '#dc3545',
        'prevention_tips': [
            'Implement SYN cookies',
            'Configure TCP intercept on routers',
            'Increase backlog queue size',
            'Use load balancers with DDoS protection',
            'Deploy Web Application Firewalls (WAF)'
        ]
    },
    'DDoS_UDP': {
        'name': 'DDoS_UDP',
        'full_name': 'Distributed Denial of Service (DDoS) using User Datagram Protocol (UDP)',
        'description': 'UDP flood attack where attackers send numerous UDP packets to random ports.',
        'severity': 'High',
        'icon': '💥',
        'color': '#dc3545',
        'prevention_tips': [
            'Disable unused UDP services',
            'Implement UDP flood protection on firewalls',
            'Use rate limiting for UDP packets',
            'Deploy traffic filtering solutions',
            'Monitor for unusual UDP traffic patterns'
        ]
    },
    'Password': {
        'name': 'Password',
        'full_name': 'Password Attack',
        'description': 'Attempts to gain unauthorized access by cracking or guessing passwords.',
        'severity': 'Medium',
        'icon': '🔐',
        'color': '#ffc107',
        'prevention_tips': [
            'Enforce strong password policies',
            'Implement multi-factor authentication',
            'Use account lockout mechanisms',
            'Monitor for failed login attempts',
            'Regularly update and patch authentication systems'
        ]
    },
    'Port_Scanning': {
        'name': 'Port_Scanning',
        'full_name': 'Port Scanning Attack',
        'description': 'Reconnaissance attack to discover open ports and services on a target system.',
        'severity': 'Low',
        'icon': '🔍',
        'color': '#28a745',
        'prevention_tips': [
            'Use port knocking techniques',
            'Implement intrusion detection systems (IDS)',
            'Close unnecessary ports',
            'Configure firewalls to block port scanning',
            'Use network segmentation'
        ]
    },
    'Ransomware': {
        'name': 'Ransomware',
        'full_name': 'Ransomware Attack',
        'description': 'Malware that encrypts files and demands ransom for decryption keys.',
        'severity': 'Critical',
        'icon': '💰',
        'color': '#721c24',
        'prevention_tips': [
            'Regularly backup important data',
            'Keep all software updated',
            'Use antivirus/anti-malware solutions',
            'Educate users about phishing emails',
            'Implement email filtering',
            'Disable macro scripts in Office files'
        ]
    },
    'Vulnerability_scanner': {
        'name': 'Vulnerability_scanner',
        'full_name': 'Vulnerability Scanner Attack',
        'description': 'Automated scanning to identify security weaknesses in systems and applications.',
        'severity': 'Medium',
        'icon': '🛡️',
        'color': '#ffc107',
        'prevention_tips': [
            'Regularly patch and update systems',
            'Conduct regular security assessments',
            'Use Web Application Firewalls (WAF)',
            'Implement network segmentation',
            'Monitor for scanning activities'
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database='network'
)
mycursor = mydb.cursor()

def executionquery(query, values):
    mycursor.execute(query, values)
    mydb.commit()
    return

def retrivequery1(query, values):
    mycursor.execute(query, values)
    data = mycursor.fetchall()
    return data

def retrivequery2(query):
    mycursor.execute(query)
    data = mycursor.fetchall()
    return data

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        c_password = request.form['c_password']
        
        if password != c_password:
            return render_template('register.html', message="Confirm password does not match!")
        
        query = "SELECT email FROM users"
        email_data = retrivequery2(query)
        email_data_list = [i[0] for i in email_data]
        
        if email in email_data_list:
            return render_template('register.html', message="Email already exists!")

        query = "INSERT INTO users (name, email, password, phone) VALUES (%s, %s, %s, %s)"
        values = (name, email, password, phone)
        executionquery(query, values)
        
        return render_template('login.html', message="Successfully Registered!")
    
    return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        query = "SELECT email FROM users"
        email_data = retrivequery2(query)
        email_data_list = [i[0] for i in email_data]

        if email in email_data_list:
            query = "SELECT name, password FROM users WHERE email = %s"
            values = (email,)
            password_data = retrivequery1(query, values)
            if password == password_data[0][1]:
                name = password_data[0][0]
                return render_template('home.html', message=f"Welcome to SmartSentry, {name}!")
            return render_template('login.html', message="Invalid Password!!")
        return render_template('login.html', message="This email ID does not exist!")
    return render_template('login.html')

@app.route('/home')
def home():
    current_time = datetime.now().strftime("%I:%M %p")
    return render_template('home.html', 
                         current_time=current_time)

@app.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        try:
            if 'file' not in request.files:
                return render_template('upload.html', 
                                     error="No file selected. Please choose a file to upload.",
                                     stats=None)
            
            file = request.files['file']
            
            if file.filename == '':
                return render_template('upload.html', 
                                     error="No file selected. Please choose a file to upload.",
                                     stats=None)
            
            if not file.filename.endswith('.csv'):
                return render_template('upload.html', 
                                     error="Invalid file type. Please upload a CSV file.",
                                     stats=None)
            
            # Read and process the CSV
            df = pd.read_csv(file, encoding='latin1')
            
            # Calculate statistics
            stats = {
                'total_rows': len(df),
                'total_columns': len(df.columns),
                'columns': list(df.columns[:10]),  # Show first 10 columns
                'data_types': df.dtypes.astype(str).to_dict(),
                'missing_values': df.isnull().sum().sum(),
                'file_size': len(file.read()) / 1024,  # KB
                'sample_data': df.head(10).to_html(classes='table table-striped')
            }
            
            # Save the dataframe for preview
            df_preview = df.head(100).to_html(
                classes='table table-striped table-bordered table-hover',
                index=False
            )
            
            return render_template('upload.html', 
                                 success=f"File '{file.filename}' uploaded successfully!",
                                 stats=stats,
                                 df=df_preview,
                                 filename=file.filename)
            
        except Exception as e:
            return render_template('upload.html', 
                                 error=f"Error processing file: {str(e)}",
                                 stats=None)
    
    return render_template('upload.html', stats=None)

@app.route('/info')
def info():
    return render_template('data_info.html')

@app.route('/models')
def models():
    return render_template('models.html')

@app.route('/prediction', methods=["GET", "POST"])
def prediction():
    if request.method == "POST":
        try:
            ip_dst_host = float(request.form['ip_dst_host'])
            http_content_length = float(request.form['http_content_length'])
            tcp_ack = float(request.form['tcp_ack'])
            tcp_ack_raw = float(request.form['tcp_ack_raw'])
            tcp_dstport = float(request.form['tcp_dstport'])
            tcp_flags = float(request.form['tcp_flags'])
            tcp_len = float(request.form['tcp_len'])
            tcp_options = float(request.form['tcp_options'])
            tcp_payload = float(request.form['tcp_payload'])
            tcp_seq = float(request.form['tcp_seq'])
            tcp_srcport = float(request.form['tcp_srcport'])
            dns_retransmit = float(request.form['dns_retransmit'])
            mqtt_ver = float(request.form['mqtt_ver'])
            
            inputs = [[
                ip_dst_host, http_content_length, tcp_ack, tcp_ack_raw, tcp_dstport,
                tcp_flags, tcp_len, tcp_options, tcp_payload, tcp_seq, tcp_srcport,
                dns_retransmit, mqtt_ver
            ]]
            
            model = joblib.load("models/RandomForestClassifier.joblib")
            prediction1 = model.predict(inputs)
            
            attack_mapping = {
                0: 'DDoS_ICMP',
                1: 'DDoS_TCP',
                2: 'DDoS_UDP',
                3: 'Password',
                4: 'Port_Scanning',
                5: 'Ransomware',
                6: 'Vulnerability_scanner'
            }
            
            attack_key = attack_mapping.get(prediction1[0], 'Unknown')
            attack_info = ATTACK_DETAILS.get(attack_key, {
                'name': 'Unknown',
                'full_name': 'Unknown Attack',
                'description': 'No information available',
                'severity': 'Unknown',
                'icon': '❓',
                'color': '#6c757d',
                'prevention_tips': ['No prevention tips available']
            })
            
            return render_template('prediction.html', 
                                 result=attack_info['full_name'],
                                 attack_info=attack_info)
            
        except ValueError as e:
            return render_template('prediction.html', 
                                 error=f"Invalid input: Please enter valid numbers. {str(e)}")
        except Exception as e:
            return render_template('prediction.html', 
                                 error=f"Prediction error: {str(e)}")
    
    return render_template('prediction.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
# 🔐 Secure Chat Application with End-to-End Encryption

A professional real-time web-based secure messaging application built using **Python**, **Flask**, **Flask-SocketIO**, **Web Crypto API**, **RSA-2048**, and **AES-256-GCM**. The application ensures that messages remain encrypted from sender to receiver, preventing the server from accessing plaintext messages.

---

## 📖 Project Overview

This project demonstrates the practical implementation of **Hybrid Encryption** in a real-time chat application. The system uses **RSA-2048** for secure key exchange and **AES-256-GCM** for encrypting chat messages. The encryption and decryption processes occur entirely in the browser, ensuring true **End-to-End Encryption (E2EE)**.

The server acts only as a message relay and never has access to users' private keys or plaintext messages.

---

## ✨ Features

- 🔐 End-to-End Encrypted Messaging
- 🔑 RSA-2048 Public/Private Key Generation
- 🔒 AES-256-GCM Message Encryption
- 🔄 Hybrid Encryption (RSA + AES)
- 🌐 Real-time Communication using Flask-SocketIO
- 👥 Live Online User List
- ⌨️ Typing Indicator
- ✅ Message Delivery Status
- 👀 Read Receipts
- 🛡️ SHA-256 Public Key Fingerprints
- 🎨 Dark & Light Theme
- 🖼️ Custom Chat Wallpaper
- 📱 Responsive User Interface
- ⚡ Smooth Real-Time Messaging
- 🔒 Server Never Reads Plaintext Messages

---

## 🏗️ Technology Stack

### Backend
- Python 3
- Flask
- Flask-SocketIO
- Eventlet
- Gunicorn

### Frontend
- HTML5
- CSS3
- JavaScript (ES6)
- Web Crypto API
- Socket.IO Client

### Cryptography
- RSA-2048 (OAEP)
- AES-256-GCM
- SHA-256 Fingerprint
- Hybrid Encryption

---

## 🔐 Encryption Workflow

```text
Sender
   │
   ▼
Generate AES-256 Session Key
   │
   ▼
Encrypt Message using AES-GCM
   │
   ▼
Encrypt AES Key using Receiver's RSA Public Key
   │
   ▼
Send Encrypted Payload
   │
   ▼
Flask Socket.IO Server
   │
   ▼
Forward Ciphertext Only
   │
   ▼
Receiver
   │
   ▼
Decrypt AES Key using RSA Private Key
   │
   ▼
Decrypt Message using AES-GCM
```

---

## 📂 Project Structure

```
Secure-Chat-App/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/
│   ├── js/
│   ├── wallpapers/
│   └── images/
│
├── templates/
│   └── index.html
│
└── screenshots/
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Secure-Chatbox.git
```

### Open Project

```bash
cd Secure-Chatbox
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Application will start at:

```
http://127.0.0.1:5000
```

---

## 🌍 Deployment

This application can be deployed using:

- Render
- Railway
- VPS
- Docker

Recommended Platform:

**Render**

---

## 🔑 Security Features

- RSA-2048 Public Key Cryptography
- AES-256-GCM Symmetric Encryption
- Hybrid Encryption
- Browser-side Encryption
- Private Keys Never Leave Client Device
- Secure Random Initialization Vector
- SHA-256 Fingerprint Verification
- Server Cannot Read Messages



## 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- End-to-End Encryption
- Hybrid Cryptography
- Web Crypto API
- Socket Programming
- Real-Time Communication
- Secure Client-Server Architecture
- Browser Cryptography
- Secure Messaging Systems

---

## 📚 References

- Flask Documentation
- Flask-SocketIO Documentation
- Web Crypto API
- RSA Cryptography
- AES-GCM Encryption
- Signal Protocol Documentation
- RFC 3526

---

## 👨‍💻 Developed By

**Sudhanshu Chouhan**

B.Tech Computer Science & Engineering

Cybersecurity Enthusiast

GitHub:
https://github.com/Sudhanshuasha

---

## ⭐ Future Enhancements

- 📂 Encrypted File Sharing
- 🎤 Voice Messages
- 📞 Audio Calling
- 🎥 Video Calling
- 👥 Group Chat
- 🔄 Forward Secrecy using ECDH
- 📱 Progressive Web App (PWA)
- ☁️ Cloud Synchronization
- 🤖 AI-powered Smart Assistant
- 🔔 Push Notifications

---

## 📄 License

This project is developed for **educational and research purposes**.

© 2026 Sudhanshu Chouhan. All Rights Reserved.

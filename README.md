# 🎮 PhishArena

## 🎯 Project Objective

PhishArena is an interactive cybersecurity training platform designed to simulate real-world phishing scenarios through structured email communication.

The system trains users to craft professional, realistic emails while demonstrating how incomplete, vague, or misleading messages can resemble phishing attempts.

PhishArena combines email-based interaction, AI evaluation, and a case-based game environment to provide practical cybersecurity awareness training.

---

## 🚀 Quick Start (Setup)

### 1. Clone

```bash
git clone https://github.com/Aldana-althawadi/PhishArena-_Game.git
cd PhishArena
````

### 2. Create virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install flask
```

### 4. Run the application

```bash
python3 app.py
```

Open in browser:
 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📧 Email-Based Gameplay (Primary Mode)

PhishArena is built around a **real email interaction model** using Postfix and Dovecot.

Players must use an email client (Thunderbird) to complete cases.

### 📥 Incoming Mail (IMAP - Dovecot)

* Server: `127.0.0.1`
* Port: `143`
* Security: None
* Authentication: Normal password

### 📤 Outgoing Mail (SMTP - Postfix)

* Server: `127.0.0.1`
* Port: `25`
* Security: None
* Authentication: None

### Example Account

* Email: `player1@emailme.com`
* Username: `player1`
* Password: `pass123`

---

## 🎮 How It Works

PhishArena is a case-based interactive game.

### Game Flow

1. Select a level
2. Open a case
3. Read the mission brief + hints
4. Send an email using Thunderbird
5. Click **"Check My Attempt"**
6. System reads the email from Maildir
7. AI evaluates the message
8. System replies via email
9. Player retrieves the response and extracts the FLAG
10. Submit the flag in the web interface to unlock the next case

---

## 🏁 Flag System

* Flags are **NOT shown in the UI**
* Flags are delivered **ONLY via email response**
* Players must:

  * check inbox
  * copy the flag
  * submit it in the game

---

## 📊 Evaluation Logic

Each email is evaluated using AI based on:

* Professionalism
* Realism
* Completeness

A successful attempt unlocks the next case.
A weak attempt requires improvement.

---

## 🌐 Alternative Testing Mode (Web Mode)

Due to hardware and deployment limitations, a **web-based submission mode** was implemented.

### Purpose

* Enables testing across multiple devices
* Removes dependency on email clients (Thunderbird)
* Used for demonstrations and evaluation

### How It Works

* Users submit messages directly in the browser
* AI evaluates the message instantly
* Feedback and scores are displayed in the UI
* Flag is revealed directly for testing

> ⚠️ This mode is not the primary system design, but a practical workaround for testing.

---

## 🌍 Multi-Device Deployment

The system was tested across multiple devices using a local network setup.

### Configuration

* Virtual Machine (Ubuntu) running Flask
* VirtualBox NAT + Port Forwarding
* Host machine IP used for access

### Access

```
http://HOST_IP:5000
```

Example:

```
http://192.168.100.18:5000
```

### Tested Devices

* 1 Host Laptop
* 1 Additional Laptop
* 2 Tablets (iPads)

---

## 🧪 Testing Summary

The system was validated across multiple devices.

### Verified Features

* Multi-device access
* Case interaction
* Message submission
* AI evaluation
* Score generation
* Flag system
* Case progression
* Shared progress synchronization

### Result

The system functioned correctly across all devices and maintained stability under concurrent usage.

---

## 🧠 Core Concept

PhishArena demonstrates that phishing is not only about malicious links, but also about:

> **how communication is structured**

Users learn to:

* Write clear and professional emails
* Provide sufficient and realistic information
* Recognize weak or suspicious communication patterns

---

## 📁 Project Structure

```
phishArena/
│
├── app.py                → Main Flask application
├── cases/
│   ├── profiles.py      → Cases & scenarios
│   ├── helpers.py       → Case logic
│
├── mail/
│   ├── mail_reader.py   → Reads Maildir
│   ├── smtp_sender.py   → Sends responses
│
├── llm/
│   ├── checker.py       → Validation logic
│   ├── pipeline.py      → AI pipeline
│   ├── rag.py           → Retrieval system
│   ├── reply_generator.py → Response generation
│   ├── post_processor.py → Output validation
│
├── logs/                → Game logs & progress
├── templates/           → HTML pages
├── static/              → Images & assets
└── env/                 → Virtual environment
```

---

## 👥 Contributors

* Aldana Althawadi
* Ghufran Sheikh
* Haya Alkaabi

---

## 🏆 Academic Context

This project was developed as a final-year cybersecurity project at:

**University of Bahrain**
College of Information Technology – 2026

---

## 📌 Notes

* This system is for **educational use only**
* All scenarios are simulated
* No real phishing activity is performed

---

# 🎯 PhishArena

**Train smart. Think deeper. Communicate better.**



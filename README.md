# 🎮 PhishArena

## 🎯 Project Objective

PhishArena is an interactive cybersecurity training platform designed to help users understand how email communication can appear legitimate or suspicious.

The system trains users to write structured, credible emails while demonstrating how incomplete, vague, or misleading messages can resemble phishing behavior.

PhishArena combines professional email writing practice with phishing-awareness training through a case-based game environment powered by real email infrastructure.

---

## 🚀 Quick Start (Setup)

### 1. Clone

```bash
git clone https://github.com/Aldana-althawadi/PhishArena-_Game.git
cd PhishArena
```

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

The web interface will open at:
👉 http://127.0.0.1:5000

---

## 📧 Thunderbird Configuration

PhishArena uses a real email system (Postfix + Dovecot).
You must configure Thunderbird to send and receive emails.

### Example Account

* Email: `player1@emailme.com`
* Username: `player1`
* Password: `pass123`

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

---

## 🎮 How It Works

PhishArena is a case-based interactive game where users complete email scenarios to progress.

### Game Flow

1. Select a level
2. Open a case
3. Read the mission brief + hints
4. Send an email using Thunderbird
5. Click **"Check My Attempt"**
6. Receive evaluation + feedback
7. If successful → receive a FLAG via email
8. Submit the flag to complete the case

---

## 🏁 Flag System

* Flags are **NOT shown in the UI**
* Flags are sent **ONLY via email reply**
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

A passing score allows progression.
A weak email requires improvement and retry.

---

## 🧠 Core Concept

PhishArena teaches that phishing is not only about malicious links —
it is about **how communication is structured**.

Users learn to:

* Write clear and structured emails
* Provide sufficient supporting information
* Understand how weak communication resembles phishing

---

## 📁 Project Structure

phishArena/

* app.py → Main Flask application
* cases/

  * profiles.py → Cases & scenarios
  * helpers.py → Case logic
* mail/

  * mail_reader.py → Reads Maildir
  * smtp_sender.py → Sends responses
* llm/

  * checker.py → Validation logic
  * pipeline.py → AI pipeline
  * rag.py → Retrieval system
  * reply_generator.py → Response generation
  * post_processor.py → Output validation
* logs/ → Game logs
* templates/ → HTML pages
* static/ → Images & assets
* env/ → Virtual environment

---

## 👥 Contributors

* Aldana Althawadi
* Ghufran Sheikh
* Haya Alkaabi

---

## 🏆 Academic Context

This project was developed as a final-year cybersecurity project at:

University of Bahrain
College of Information Technology – 2026

---

## 📌 Notes

* This system is for **educational use only**
* All scenarios are simulated
* No real phishing activity is performed

---

# 🎯 PhishArena

Train smart. Think deeper. Communicate better.

# 🤖 Data Engineering Mentor Bot

AI-powered chatbot built with Gemini API and Streamlit to help users learn Data Engineering concepts such as SQL, ETL, Data Warehouse, Data Modeling, and Data Governance.

## 📌 Project Overview

Data Engineering Mentor Bot is an educational chatbot designed to assist students, aspiring data engineers, and data analysts in understanding data engineering concepts through natural language conversations.

The chatbot leverages Google's Gemini Large Language Model (LLM) to provide relevant explanations, examples, learning recommendations, and technical guidance.

## 🎯 Features

### ✅ AI Chatbot

* Powered by Gemini API
* Natural language interaction
* Context-aware responses

### ✅ Conversation Memory

* Maintains chat history during the session
* Provides more contextual responses

### ✅ Multiple Expert Modes

Users can choose different mentoring modes:

* SQL Expert
* ETL Specialist
* Data Architect
* Data Governance

### ✅ Adjustable Creativity

Users can control response creativity using the temperature parameter.

### ✅ Educational Responses

* Beginner-friendly explanations
* Step-by-step guidance
* Practical examples

### ✅ Learning Recommendations

* Roadmaps for Data Engineering
* Suggested learning paths
* Skill recommendations

---

## 🛠️ Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Backend Programming             |
| Streamlit     | User Interface                  |
| Gemini API    | Large Language Model            |
| python-dotenv | Environment Variable Management |

---

## 📂 Project Structure

```text
data-engineering-mentor-bot/
│
├── app.py
├── chatbot.py
├── prompts.py
├── requirements.txt
├── .env
├── .gitignore
│
├── screenshots/
│
└── README.md
```

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/data-engineering-mentor-bot.git

cd data-engineering-mentor-bot
```

### 2. Create Virtual Environment

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create a `.env` file in the project root directory.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your Gemini API key.

---

## ▶️ Run Application

```bash
streamlit run app.py
```

After running the command, open your browser and access:

```text
http://localhost:8501
```

---

## 💡 Example Questions

### SQL

```text
Explain the difference between INNER JOIN and LEFT JOIN.
```

```text
Create a query to find the top 10 highest sales.
```

### ETL

```text
What are the common causes of ETL failures?
```

### Data Warehouse

```text
What is the difference between Star Schema and Snowflake Schema?
```

### Data Governance

```text
Why is data governance important in organizations?
```

---

## 📸 Screenshots

### Home Page

Insert screenshot here.

### SQL Expert Mode

Insert screenshot here.

### ETL Specialist Mode

Insert screenshot here.

### Data Architect Mode

Insert screenshot here.

### Conversation Memory

Insert screenshot here.

---

## ⚙️ Configuration

### Temperature

Controls response creativity.

| Value | Behavior        |
| ----- | --------------- |
| 0.0   | Deterministic   |
| 0.3   | Balanced        |
| 0.7   | Creative        |
| 1.0   | Highly Creative |

### Expert Mode

The chatbot can switch between different knowledge domains:

* SQL Expert
* ETL Specialist
* Data Architect
* Data Governance

---

## 🔒 Security Notes

This project does not use any proprietary, confidential, or organizational data.

Do not commit the following files to GitHub:

```text
.env
```

Ensure that API keys are stored securely using environment variables.

---

## 🎓 Final Project Information

**Course:** LLM Based Tools and Gemini API Integration for Data Scientists

**Platform:** Hacktiv8

**Project Type:** AI Chatbot using Gemini API

**Author:** Erlangga Riyyan Nugraha

---

## 📄 License

This project is developed for educational purposes as part of the Hacktiv8 Final Project.

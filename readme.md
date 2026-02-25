# 🚀 Social Media Platform API

A scalable **Social Media Backend Application** built using **Django** and **Django REST Framework**.
This project focuses on implementing real-world social networking features while following clean backend architecture and REST API design principles.

---

## 📌 Project Overview

This project is part of my backend engineering journey where I am building a production-style social media platform step by step.

The goal is to understand how large-scale social platforms manage users, relationships, engagement, and content delivery using REST APIs.

---

## ✅ Features Implemented

### 👤 User Management

* User Registration
* Secure User Login & Authentication
* Custom User Model

### 🤝 Social Features

* Follow / Unfollow Users
* User Relationship Management

### 📝 Content System

* Create Posts
* Like Posts
* Comment on Posts
* Post Interaction APIs

---

## 🚧 Currently Working On

* Feed API (Personalized User Feed)

---

## 🛠️ Tech Stack

* **Backend Framework:** Django
* **API Framework:** Django REST Framework
* **Database:** SQLite (Development)
* **Authentication:** Token-Based Authentication
* **Version Control:** Git & GitHub

---
## 📂 Project Structure

```
Social-Platform/
│
├── apps/
│   ├── users/          # User registration, authentication & profile logic
│   ├── connections/    # Follow / Unfollow system
│   ├── posts/          # Posts, likes & comments functionality
│   └── core/           # Shared configurations & common utilities
│
├── SocialPlatform/     # Main project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

### 5️⃣ Start Development Server

```bash
python manage.py runserver
```

---

## 🎯 Learning Goals

* Build scalable REST APIs
* Understand social graph relationships
* Implement production-level backend logic
* Prepare foundation for future AI-powered features

---

## 🔮 Upcoming Features

* Personalized Feed API
* User Profile APIs
* Media Upload Support
* Notifications System
* API Optimization & Pagination

---

## 🤝 Contributions

This project is currently under active development. Suggestions and feedback are always welcome!

---

## ⭐ Support

If you find this project helpful, consider giving it a ⭐ on GitHub.

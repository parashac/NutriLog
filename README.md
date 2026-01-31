# 🥗 NutriLog

NutriLog is a **Django-based calorie and exercise tracking web application** designed to help users monitor their daily calorie intake, calories burned through exercise, and overall progress toward fitness goals.

The project emphasizes **clean backend architecture**, **proper database design**, and **real-world health tracking logic**, built **without using AI**, making it ideal for learning and demonstrating core Django development skills.

---

## ✨ Features

* 🔐 **User Authentication & Profile Management**
  Secure registration, login, and personalized user profiles.

* 🍽️ **Food Calorie Tracking**
  Track calorie intake based on food quantity and per-100g nutritional values.

* 🏃 **Exercise Tracking with MET Values**
  Log exercises using standard MET (Metabolic Equivalent of Task) values.

* 🔢 **Automatic Calorie Burn Calculation**
  Calories burned are calculated automatically based on activity duration and MET.

* 🎯 **Daily Calorie Burn Goals**
  Set and monitor personalized daily calorie burn targets.

* 📊 **Dashboard & Progress Summary**
  View daily and weekly summaries of calories consumed vs. burned.

* 🛠️ **Django Admin Panel**
  Full admin interface for managing users, food items, and exercise data.

---

## 🧰 Tech Stack

* **Backend:** Python, Django
* **Database:** SQLite
* **Frontend:** HTML, Bootstrap
* **Authentication:** Django Auth System

---

## 🚀 Getting Started

Follow these steps to run NutriLog locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/NutriLog.git
cd NutriLog
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install django
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser (Admin Access)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to:

```
http://127.0.0.1:8000/
```

---

## 📁 Project Focus

NutriLog is ideal for:

* Learning **Django ORM and model relationships**
* Implementing **real-world business logic**
* Understanding **calorie & fitness tracking systems**
* Building a **clean, maintainable backend**

---

## 📸 Screenshots



<img width="1920" height="1080" alt="Screenshot 2026-01-31 175558" src="https://github.com/user-attachments/assets/1f4746f1-894f-4d5a-921e-61058b6ccdf7" />
---


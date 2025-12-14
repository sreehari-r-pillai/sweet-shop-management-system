
# 🍬 Sweet Shop Management System

A full-stack **Sweet Shop Management System** built as part of a technical assignment.
The application allows users to browse and purchase sweets, while admins can manage inventory.
It includes a **secure RESTful backend API** and a **modern single-page frontend application (SPA)**.

---

## 📌 Features Overview

### 👤 User Features
- User registration and login
- JWT-based authentication
- View all available sweets
- Search sweets by name, category, or price range
- Purchase sweets (disabled when out of stock)

### 👑 Admin Features
- Add new sweets
- Update sweet details
- Delete sweets
- Restock sweets
- Role-based access control (Admin vs User)

---

## 🧱 Tech Stack

### Backend
- **Language / Framework:** Python – FastAPI
- **Database:** SQLite (persistent, file-based)
- **Authentication:** JWT (JSON Web Tokens)
- **ORM:** SQLAlchemy
- **Testing:** Pytest (includes negative tests: 401 / 403)

### Frontend
- **Framework:** React (SPA)
- **HTTP Client:** Axios
- **State Management:** React Context API
- **Styling:** CSS (clean, responsive, minimal polish)

---

## 📂 Project Structure

```
sweet-shop/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── security.py
│   │   ├── dependencies.py
│   │   └── routers/
│   │       ├── auth.py
│   │       └── sweets.py
│   ├── tests/
│   │   ├── test_auth.py
│   │   ├── test_admin_access.py
│   │   ├── test_negative_auth.py
│   │   └── test_inventory.py
│   └── requirements.txt
│
├── frontend/
│   ├── package.json
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── api.js
│       ├── styles.css
│       ├── context/
│       │   └── AuthContext.jsx
│       ├── pages/
│       │   ├── Login.jsx
│       │   ├── Register.jsx
│       │   ├── Dashboard.jsx
│       │   └── Admin.jsx
│       └── components/
│           ├── SweetCard.jsx
│           └── SearchBar.jsx
│
└── README.md
```

---

## 🚀 How to Run the Application

### 1️⃣ Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend will run at:
```
http://localhost:8000
```

Swagger API Docs:
```
http://localhost:8000/docs
```

---

### 2️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will run at:
```
http://localhost:5173
```

> Ensure the backend is running before using the frontend.

---

## 🔐 Authentication & Roles

- **Default Role:** USER
- **Admin Role:** ADMIN

Admins can:
- Add, update, delete sweets
- Restock inventory

JWT tokens are required for all protected routes.

---

## 🧪 Testing

Backend includes **comprehensive Pytest coverage**, including:
- Authentication tests
- Admin-only access tests
- Inventory tests
- Negative tests (401 Unauthorized, 403 Forbidden)

Run tests with:
```bash
cd backend
pytest -v
```

---

## 🎨 Design & UX

- Clean, card-based UI
- Responsive layout
- Disabled states for unavailable actions
- Role-based UI rendering
- Minimal CSS polish for usability and clarity

No heavy UI libraries or animations were used to keep the focus on functionality, performance, and accessibility.

---

## 🤖 AI Usage Disclosure

AI tools (ChatGPT) were used for:
- Architectural guidance
- Boilerplate generation
- Test case scaffolding

All logic, structure, and final decisions were **reviewed, modified, and validated manually**.

---

## ✅ Final Status

- ✔ Backend requirements: **Fully met**
- ✔ Frontend requirements: **Fully met**
- ✔ Security & authentication: **Implemented**
- ✔ Testing: **Included**
- ✔ Submission-ready: **Yes**

---

## 📬 Notes for Evaluators

This project focuses on:
- Correctness
- Security
- Clean architecture
- Requirement completeness

Advanced UI animations were intentionally avoided to prioritize clarity, usability, and scope adherence.

---

**Thank you for reviewing this project.**

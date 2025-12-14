
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

```text
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

## 🤖 My AI Usage

AI tools were used intentionally and transparently during the development of this project as part of a modern software development workflow.

### 🔧 AI Tools Used
- **ChatGPT (OpenAI)**

### 🛠️ How I Used AI
- Architecture brainstorming and REST API design validation  
- Generating initial backend boilerplate (FastAPI, auth, models)  
- Assisting with Pytest structure and negative test scenarios  
- Reviewing frontend structure and state management patterns  
- Improving code readability and best practices  

### ✍️ Human Review & Ownership
All AI-generated outputs were treated as **starting points only**.  
I manually reviewed, modified, and extended the code to:
- Add validation and error handling  
- Enforce role-based access control  
- Ensure business logic correctness  
- Improve maintainability  

All final implementation decisions were **fully owned and verified by me**.

### 🔄 Impact on My Workflow
AI improved productivity by reducing boilerplate effort, allowing greater focus on:
- Correctness  
- Clean architecture  
- Comprehensive testing  

AI was used as an **assistant**, not a replacement for engineering judgment.

### 🧾 Transparency & Accountability
I am fully transparent about AI usage and comfortable discussing:
- Where AI helped  
- Where manual decisions were required  
- How correctness was validated  

---

## ✅ Final Status

- ✔ Backend requirements: **Fully met**  
- ✔ Frontend requirements: **Fully met**  
- ✔ Security & authentication: **Implemented**  
- ✔ Testing: **Included**  
- ✔ Submission-ready: **Yes**

---

## 📬 Notes for Evaluators

This project prioritizes:
- Correctness  
- Security  
- Clean architecture  
- Requirement completeness  

Advanced UI animations were intentionally avoided to maintain clarity and scope focus.

---

**Thank you for reviewing this project.**

# 💰 Expense Tracker - Full Stack Web Application

A modern **Full Stack Expense Tracker** built with **React.js, Node.js, Express.js, Firebase Authentication, and Cloud Firestore**. The application enables users to securely manage their personal finances while providing an **Admin Dashboard** to monitor users and application statistics.

---

# 📺 Project Preview

> *(Add screenshots or GIF here)*

```text
📌 Login Page
📌 User Dashboard
📌 Add Income
📌 Add Expense
📌 Transaction History
📌 Admin Dashboard
```

Login

### Login
![Expense Tracker](https://drive.google.com/uc?export=view&id=1hYsubMyLKpmSGfREURdKTDDhYVHWlEwL)

### SignUP
![Expense Tracker](https://drive.google.com/uc?export=view&id=1HQtnYe5poMncQw22T97FRavIhFBDjXsy)

### Admin
![Expense Tracker](https://drive.google.com/uc?export=view&id=1hYsubMyLKpmSGfREURdKTDDhYVHWlEwL)

---

# 🚀 Features

## 👤 User Features

- 🔐 Secure Sign Up & Login using Firebase Authentication
- 💰 Add Income
- 💸 Add Expenses
- 📊 Dashboard showing:
  - Total Income
  - Total Expenses
  - Current Balance
- 📜 Transaction History
- ✏️ Edit Transactions
- 🗑️ Delete Transactions
- 📥 Download Income Report (Excel)
- 📱 Responsive UI
- 🔒 Protected Routes

---

## 👨‍💼 Admin Features

- Admin Login
- User Management
- View Total Users
- Monitor Total Income Records
- Monitor Total Expense Records
- View Overall Application Statistics
- Role-Based Access Control

---

# 🛠️ Tech Stack

## Frontend

- React.js
- React Router DOM
- Axios
- Tailwind CSS
- React Icons
- Chart.js
- React Toastify

---

## Backend

- Node.js
- Express.js
- Firebase Admin SDK
- JWT Authentication
- Multer
- XLSX

---

## Database

- Cloud Firestore

---

## Authentication

- Firebase Authentication

---

## Hosting

### Frontend

- Firebase Hosting

### Backend

- Express.js API

---

# 📂 Project Structure

```
Expense-Tracker
│
├── client
│   ├── src
│   ├── components
│   ├── pages
│   ├── user
│   └── admin
│
├── server
│   ├── config
│   ├── controllers
│   ├── middleware
│   ├── models
│   ├── routes
│   ├── uploads
│   └── server.js
│
└── README.md
```

---

# 🔑 Authentication Flow

```
User Login
      │
      ▼
Firebase Authentication
      │
      ▼
Firebase ID Token
      │
      ▼
Express Backend
      │
Verify Firebase Token
      │
      ▼
Cloud Firestore
```

---

# 📊 Database Collections

```
users
income
expenses
```

Each transaction stores:

```
title
amount
category
date
note
userId
createdAt
```

---

# 🔧 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Expense-Tracker.git
```

```
cd Expense-Tracker
```

---

# Backend Setup

```
cd server
```

Install dependencies

```bash
npm install
```

Create `.env`

```env
PORT=8000

CLIENT_URL=http://localhost:5173

FIREBASE_SERVICE_ACCOUNT=./config/serviceAccountKey.json
```

Run backend

```bash
npm run dev
```

---

# Frontend Setup

```
cd client
```

Install packages

```bash
npm install
```

Create `.env`

```env
VITE_FIREBASE_API_KEY=

VITE_FIREBASE_AUTH_DOMAIN=

VITE_FIREBASE_PROJECT_ID=

VITE_FIREBASE_STORAGE_BUCKET=

VITE_FIREBASE_MESSAGING_SENDER_ID=

VITE_FIREBASE_APP_ID=
```

Run frontend

```bash
npm run dev
```

---

# 📡 API Endpoints

## Authentication

```
POST /api/auth/signup

POST /api/auth/login
```

---

## Income

```
GET /api/income

POST /api/income

PUT /api/income/:id

DELETE /api/income/:id
```

---

## Expenses

```
GET /api/expenses

POST /api/expenses

PUT /api/expenses/:id

DELETE /api/expenses/:id
```

---

## Dashboard

```
GET /api/dashboard

GET /api/home
```

---

## Admin

```
GET /api/admin/stats

GET /api/admin/users
```

---

# 📷 Screenshots

## Login

(Add Screenshot)

---

## User Dashboard

(Add Screenshot)

---

## Add Income

(Add Screenshot)

---

## Add Expense

(Add Screenshot)

---

## Transaction History

(Add Screenshot)

---

## Admin Dashboard

(Add Screenshot)

---

# 📌 Future Enhancements

- Monthly Analytics
- Budget Planning
- Expense Categories Chart
- PDF Report Export
- Email Notifications
- Multi-Currency Support
- Dark Mode
- Profile Management
- Recurring Transactions
- Mobile App Version

---

# 👨‍💻 Author

**Siva P**

- 💼 Full Stack Developer
- 🔗 GitHub: https://github.com/Sva-Dagger
- 💼 LinkedIn: *(Add your LinkedIn profile URL here)*

---

# ⭐ Support

If you found this project helpful,

⭐ Star this repository

🍴 Fork the repository

🛠️ Contribute with pull requests

---

# 📄 License

This project is licensed under the MIT License.

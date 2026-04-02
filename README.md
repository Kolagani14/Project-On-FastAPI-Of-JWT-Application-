# FastAPI JWT Authentication API

This project is a backend application built using **FastAPI** that implements **JWT (JSON Web Token) authentication** for securing APIs.
It demonstrates how to handle user authentication, authorization, and protected routes using token-based security instead of session-based login systems.
---

## 🚀 Overview

This project focuses on building a secure authentication system where users can:
* Register a new account
* Log in using credentials
* Receive a JWT access token
* Access protected routes using the token
It shows how modern APIs handle authentication without storing session data on the server.
---

## ⚙️ Features

* User registration (signup)
* User login (authentication)
* JWT token generation
* Protected routes (require valid token)
* Password hashing for security
* Token-based authorization
* Clean and modular architecture
---

## 🛠️ Tech Stack

* **Backend**: FastAPI
* **Language**: Python
* **Authentication**: JWT (JSON Web Tokens)
* **Password Hashing**: Passlib / bcrypt
* **Database**: SQLite (can be extended)
* **ORM**: SQLAlchemy
* **Validation**: Pydantic
* **Server**: Uvicorn
---

## 🔐 How JWT Works

1. User logs in with username and password
2. Server verifies credentials
3. Server generates a JWT token
4. Client stores the token
5. Token is sent in headers for protected requests

## ▶️ How to Run

1. Run server:

   ```
   uvicorn main:app --reload
   ```
2. Open API docs:

   ```
   http://127.0.0.1:8000/docs
   ```

---

## 🧠 What This Project Teaches

Most beginners either:

* Store plain passwords (terrible idea)
* Don’t secure APIs at all

This project fixes that by:

* Hashing passwords securely
* Using JWT instead of sessions
* Protecting routes with authentication middleware
* Structuring authentication logic separately

---

## 📈 Future Improvements

* Add refresh tokens
* Implement role-based access control (RBAC)
* Use PostgreSQL instead of SQLite
* Add email verification
* Add rate limiting and security headers

---

## 💥 Reality Check

This is not production-ready yet:

* No refresh token → tokens expire and require re-login
* No blacklist system → tokens can't be revoked
* Basic security only → missing advanced protections

If you want to build real systems, you must go deeper into security.

---

## 📎 Conclusion

This project demonstrates how to implement secure authentication using JWT in FastAPI. It provides a strong foundation for building protected APIs and understanding modern authentication mechanisms.

## Fintrack Backend — Local Setup

Follow these steps to run the Django backend locally on macOS, Linux, or Windows.

### Table of Contents
- Prerequisites
- Clone or open the project
- macOS (zsh/bash)
- Linux (bash)
- Windows (PowerShell)
- Project structure (quick reference)
- Troubleshooting

### 1) Prerequisites
- Python 3.10+ installed (check with `python3 --version`)
- Git installed (optional if the project is already downloaded)

### 2) Clone or open the project
```bash
git clone https://github.com/talha-rauf-qbatch/Auth-using-Django.git Fintrack_backend
cd Fintrack_backend
```

If you already have the folder, just:
```bash
cd /Users/macbook/Downloads/Fintrack_backend
```

### macOS (zsh/bash)
1) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Upgrade pip and install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3) Apply database migrations
```bash
python fintrack_backend/manage.py migrate
```

4) (Optional) Create a superuser for the admin
```bash
python fintrack_backend/manage.py createsuperuser
```

5) Run the development server
```bash
python fintrack_backend/manage.py runserver
```

Open `http://127.0.0.1:8000/`.

To deactivate later:
```bash
deactivate
```

### Linux (bash)
1) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Upgrade pip and install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3) Apply database migrations
```bash
python fintrack_backend/manage.py migrate
```

4) (Optional) Create a superuser
```bash
python fintrack_backend/manage.py createsuperuser
```

5) Run the development server
```bash
python fintrack_backend/manage.py runserver
```

Open `http://127.0.0.1:8000/`.

### Windows (PowerShell)
Use these equivalents on Windows with PowerShell:

1) Open PowerShell in the project folder
```powershell
cd C:\path\to\Fintrack_backend
```

2) (One-time) Allow script execution for virtualenv activation if needed
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned -Force
```

3) Create and activate virtual environment
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4) Upgrade pip and install dependencies
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

5) Apply database migrations
```powershell
python .\fintrack_backend\manage.py migrate
```

6) (Optional) Create a superuser
```powershell
python .\fintrack_backend\manage.py createsuperuser
```

7) Run the development server
```powershell
python .\fintrack_backend\manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

Notes:
- To deactivate the venv: `deactivate`
- If using Command Prompt (cmd.exe), activate with: `.\.venv\Scripts\activate.bat`

### Project structure (quick reference)
```
Fintrack_backend/
├─ .venv/                # virtual environment (local)
├─ .gitignore
├─ requirements.txt
├─ README.md
└─ fintrack_backend/
   ├─ manage.py
   ├─ db.sqlite3         # local SQLite DB
   ├─ fintrack_backend/  # Django project package
   └─ accounts/          # Django app
```

### Troubleshooting
- If `command not found: python` or `python3`, install Python from python.org or via Homebrew: `brew install python`.
- If migrations fail, try deleting the local DB and rerun migrations: `rm fintrack_backend/db.sqlite3 && python fintrack_backend/manage.py migrate` (only for local dev).
- Ensure the virtualenv is active (your shell prompt should begin with `(.venv)`), otherwise `pip`/`python` may point to system Python.



## API Reference

Base URL: `http://127.0.0.1:8000`

Auth uses JWT (SimpleJWT). Send the access token in the `Authorization` header: `Authorization: Bearer <ACCESS_TOKEN>`.

### POST /api/auth/register/
- Purpose: Create a new user account
- Request (JSON):
```json
{
  "username": "talha123",
  "email": "talha123@example.com",
  "password": "StrongPass123!",
  "first_name": "Talha",
  "last_name": "Rauf"
}
```
- Response 201 (JSON):
```json
{
  "id": 1,
  "username": "talha123",
  "email": "talha123@example.com",
  "first_name": "Talha",
  "last_name": "Rauf",
  "date_joined": "2025-01-01T12:00:00Z",
  "last_login": null
}
```
- Errors: 400 on validation (e.g., email already in use)

### POST /api/auth/login/
- Purpose: Obtain JWT tokens (login)
- Request (JSON):
```json
{
  "email": "talha123@example.com",
  "password": "StrongPass123!"
}
```
- Response 200 (JSON):
```json
{
  "refresh": "<JWT_REFRESH>",
  "access": "<JWT_ACCESS>"
}
```
- Errors: 401 on invalid credentials

Notes:
- Login requires `email` and `password` only. `username` is not accepted.

### POST /api/auth/refresh/
- Purpose: Refresh access token using a valid refresh token
- Request (JSON):
```json
{
  "refresh": "<JWT_REFRESH>"
}
```
- Response 200 (JSON):
```json
{
  "access": "<NEW_JWT_ACCESS>"
}
```

### GET /api/auth/me/
- Purpose: Get the authenticated user's profile
- Headers: `Authorization: Bearer <ACCESS_TOKEN>`
- Response 200 (JSON):
```json
{
  "id": 1,
  "username": "talha123",
  "email": "talha123@example.com",
  "first_name": "Talha",
  "last_name": "Rauf",
  "date_joined": "2025-01-01T12:00:00Z",
  "last_login": null
}
```

### PATCH /api/auth/me/
- Purpose: Update the authenticated user's profile (partial updates)
- Headers: `Authorization: Bearer <ACCESS_TOKEN>`
- Request (JSON, any subset of these fields):
```json
{
  "first_name": "Talha",
  "last_name": "Rauf",
  "email": "newmail@example.com",
  "username": "newusername"
}
```
- Response 200 (JSON): Returns the updated user object (same shape as GET /me)
- Notes: Email must be unique; validation errors return 400


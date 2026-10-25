from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
import sqlite3
from passlib.context import CryptContext

# --- CONFIGURATION DE LA SÉCURITÉ ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI(title="Budget Master API")

# --- BASE DE DONNÉES ---
DB_PATH = "budget_master.db"

def get_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT,
                type TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        conn.commit()

@app.on_event("startup")
async def startup_event():
    init_db()

# --- MODÈLES ---
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class TransactionCreate(BaseModel):
    amount: float
    category: str
    date: str
    description: Optional[str] = None
    type: str # 'income' or 'expense'

# --- ROUTES AUTH ---

@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                (user.username, user.email, hashed_password)
            )
            conn.commit()
            return {"message": "Utilisateur créé avec succès"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="L'utilisateur ou l'email existe déjà.")

@app.post("/login")
async def login(user: UserLogin):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (user.username,))
        db_user = cursor.fetchone()
        if not db_user or not pwd_context.verify(user.password, db_user["password_hash"]):
            raise HTTPException(status_code=401, detail="Identifiants incorrects.")
        return {"message": "Connexion réussie", "user_id": db_user["id"], "username": db_user["username"]}

# --- ROUTES BUDGET ---

@app.post("/transactions")
async def add_transaction(transaction: TransactionCreate, user_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO transactions (user_id, amount, category, date, description, type) VALUES (?, ?, ?, ?, ?, ?)",
            (user_id, transaction.amount, transaction.category, transaction.date, transaction.description, transaction.type)
        )
        conn.commit()
        return {"message": "Transaction ajoutée"}

@app.get("/transactions/{user_id}")
async def get_transactions(user_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions WHERE user_id = ? ORDER BY date DESC", (user_id,))
        return [dict(row) for row in cursor.fetchall()]

@app.delete("/transactions/{transaction_id}")
async def delete_transaction(transaction_id: int, user_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transactions WHERE id = ? AND user_id = ?", (transaction_id, user_id))
        conn.commit()
        return {"message": "Transaction supprimée"}

@app.get("/stats/{user_id}")
async def get_stats(user_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE user_id = ? AND type = 'income'", (user_id,))
        income = cursor.fetchone()[0] or 0.0
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE user_id = ? AND type = 'expense'", (user_id,))
        expense = cursor.fetchone()[0] or 0.0
        return {"total_income": income, "total_expense": expense, "balance": income - expense}

@app.get("/")
async def root():
    return {"status": "Budget Master Server is running"}

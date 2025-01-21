from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncpg
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "db_task")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")


async def get_db_connection():
    return await asyncpg.connect(
        user=DB_USER, password=DB_PASSWORD, database=DB_NAME, host=DB_HOST
    )


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit", response_class=HTMLResponse)
async def submit(title: str = Form(...), description: str = Form(...)):
    conn = await get_db_connection()
    await conn.execute(
        "INSERT INTO tasks (title, description) VALUES ($1, $2)", title, description
    )
    await conn.close()
    return "Data submitted successfully! <a href='/data'>View Data</a>"


@app.get("/data", response_class=HTMLResponse)
async def data(request: Request):
    conn = await get_db_connection()
    rows = await conn.fetch("SELECT * FROM tasks")
    await conn.close()
    return templates.TemplateResponse("data.html", {"request": request, "rows": rows})

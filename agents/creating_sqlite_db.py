import sqlite3
from faker import Faker
import random

fake = Faker("pt_BR")

con = sqlite3.connect("empresa.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    salario REAL,
    tempo_empresa INTEGER
)
""")

# Gerar dados falsos
for _ in range(20):
    nome = fake.name()
    idade = random.randint(18, 65)
    salario = round(random.uniform(1500, 15000), 2)
    tempo_empresa = random.randint(0, idade - 18)

    cur.execute(
        "INSERT INTO funcionarios (nome, idade, salario, tempo_empresa) VALUES (?, ?, ?, ?)",
        (nome, idade, salario, tempo_empresa)
    )

con.commit()
con.close()

import sqlite3

# Nome do arquivo do banco de dados SQLite
DATABASE = 'user.db'

# Conecta ao banco de dados SQLite (cria se não existir)
conn = sqlite3.connect(DATABASE)

# Cria um objeto cursor para executar comandos SQL
cursor = conn.cursor()

# Cria a tabela 'Usuarios' se ainda não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
    ''')

# Insere dados na tabela 'Usuarios'
cursor.execute('INSERT INTO Usuarios(nome, idade) VALUES (?, ?)', ('John', 22))
cursor.execute('INSERT INTO Usuarios(nome, idade) VALUES (?, ?)', ('Roger', 19))
cursor.execute('INSERT INTO Usuarios(nome, idade) VALUES (?, ?)', ('jose', 30))

# Commit das alterações no banco de dados
conn.commit()

# Seleciona todos os registros da tabela 'Usuarios' e imprime
cursor.execute('SELECT * FROM Usuarios')
for row in cursor.fetchall():
    print(row)

# Fecha a conexão com o banco de dados
conn.close()

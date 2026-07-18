# importando
import sqlite3

# criando o banco/ conexão
banco = sqlite3.connect("banco_escolar.db")

# para podermos mexer no banco
cursor = banco.cursor()

# definir o q vamos passar
cursor.execute("CREATE TABLE IF NOT EXISTS alunos (nome TEXT, idade NUMBER, gênero TEXT, curso TEXT, contato NUMBER)")

# passando os itens
cursor.execute("INSERT INTO alunos VALUES ('Israel Shalon', 16, 'Masculino', 'Python', 92994108026)")

# confirmando
banco.commit()

# fechando
banco.close()
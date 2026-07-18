# aqui você vai estar importando o sqlite3
import sqlite3

# Agora vc vai estar  ligando o banco fazendo uma conexão cinema.db pra gravar dados sobre filmes
con = sqlite3.connect("cinema.db")

# Agora a gente vai criar o curso que consegue " ele vai ser meio que associado/ andar pelos itens no banco de dados"
cur = con.cursor()

# ele vai executar o sqlite uma declaração sql ai a gente define oq vai ser passado o titulo o ano e a duração
cur.execute("CREATE TABLE IF NOT EXISTS filme(titulo, ano, duracao)")

# isso vai nos motrar os itens que nos temos do banco de dados e vai nos mostrar se foi criado ou não
res = cur.execute("SELECT name FROM sqlite_master")

# esse fetchone vai retonar 1 item do banco fetchone vai buscar 1
res.fetchone()

# aqui vamos definir oq vai ser colocado dentro do banco de dados
cur.execute("""
            INSERT INTO filme VALUES
            ('Gente Grande 2 ', 2013, 101),
            ('Gente Grande 1 ', 2010, 102)
""")

# quando alteramos algo do banco de dados sempre vamos commitar ou em outrar palavras confirmar
con.commit()

# aqui vamos confirmar se realmente foi adicionado
res = cur.execute("SELECT titulo FROM filme")
# e aqui vamos buscar todos os registros
res.fetchall()

#inserir mais registros
dados_films = [
    ("Idiana Jones e a Última Cruzada", 1989, 127),
    ("De volta para o Futuro", 1985, 116)
]

# ele vai pegar cada uma das tuplas que ta dentro da lista e executar cada uma separadamente e vamos aproveitar e colocar um placheholder VALUES usamos pra evitar ataques de injeção de sql
cur.executemany("INSERT INTO filme (titulo, ano, duracao) VALUES(?, ?, ?)", dados_films)
# e agora vamos confirmar
con.commit()

# outra fomra de verificar os dados inseridos

for linha in cur.execute("SELECT ano, titulo FROM filme ORDER BY ano"):
    print(linha)

# Gerenciador de Conteto com objeto connection: dispensa commit ou rollback explicitos da pra adicionar tambem mais itens as vexes evitar alguns problemas e etc
try:
    with con:
        con.execute("INSERT INTO filme (titulo,ano,duracao) VALUES(?,?,?)", ('Oppenheimer', 2023, 180))
except sqlite3.ProgrammingError:
    print("Banco de dados não acessivel")

res = cur.execute("SELECT titulo FROM filme")
res.fetchall()

# aqui vamos estar fechando
con.close()
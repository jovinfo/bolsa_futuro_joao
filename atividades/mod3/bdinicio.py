#Em um novo arquivo python crie um bd e estabeleça uma conexao com ele
#dps crie uma tabela com as seguintes colunas Id, nome, idade, cpf, email, endereco, sexo e salario

import sqlite3

con = sqlite3.connect('bdinicio.db')
cur = con.cursor()

q ="""CREATE TABLE IF NOT EXISTS funcionario (
id INTEGER PRIMARY KEY,
nome TEXT NOT NULL,
idade INT NOT NULL,
cpf TEXT NOT NULL,
email TEXT NOT NULL,
endereco TEXT NOT NULL,
sexo TEXT NOT NULL,
salario FLOAT NOT NULL 
); """

cur.execute(q)
# con.commit()

# q = "INSERT INTO funcionario (id, nome, idade, cpf, email, endereco, sexo, salario) VALUES (?,?,?,?,?,?,?,?);"
# valores = [
#     (10, 'Joao', 25, '12345678912', 'email@mail.com', 'Rua das ruas', 'M', 99000.00),
#     (144, 'OaoJ', 52, '12345678911', 'aaaa@mail.com', 'Ruas da ruaaaaa', 'X', 1234.00),
#     (200, 'Rafa', 29, '33345678910', 'rafa@mail.com', 'CaSA das ruas', 'F', 99999.36)
# ]

# cur.executemany(q, valores)

con.commit()

cur.execute("SELECT * FROM funcionario;")
res = cur.fetchall()
for r in res:
    print(f'Id = {r[0]} - Nome = {r[1]} - Idade = {r[2]}\nCPF = {r[3]} - Email = {r[4]} - Endereço = {r[5]}\nSexo = {r[6]} - Salário = {r[7]}\n')

con.close()
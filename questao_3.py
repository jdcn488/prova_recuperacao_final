
usuario = (nome, idade, telefone, email)

num = 0

for num in range(0, 1):

    nome = str(input("digite o Nome: \n"))

    if len(nome) == 0:

        usuario = usuario.append(0)

    idade = str(input("Digite a idade: \n"))

    if len(idade) == 0:

        idade = usuario.append(1)

    telefone = str(input("digite o telefone: \n"))

    if len(telefone) == 0:

        telefone = usuario.append(2)

    email = str(input("digite o email: \n"))

    if len(email) == 0:

        email = usuario.append(3)


    print(usuario)


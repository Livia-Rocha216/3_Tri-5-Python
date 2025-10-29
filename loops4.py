usuarios = ["ana", "", " ", "marcos", "julia123", "marcos@3", "gabrielly 123"]

for usuario in usuarios:
    if not usuario:
        continue

    for letra in usuario:
        if letra.isspace():
            print(f"| Ignorando '{usuario}', contém espaços vazios.") 
            break
        elif letra.isalpha() == False:
            print(f"| Ignorando '{usuario}', contém caractéres especiais.")
            break

    else:
        print(f"| Cadastrando usuário '{usuario}';")
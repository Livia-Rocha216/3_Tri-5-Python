inventario = ["elmo", "chapéu", "espada", "botas"]
busca = input("Digite um item: ")

for item in inventario:
    if item == busca:
        print(f"{busca.capitalize()} foi encontrada!")
        break
else:
    print("Item não encontrado.")    
        
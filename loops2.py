inventario = ["elmo", "chapéu", "espada", "botas"]
busca = input("Busque por um item: ")

for item in inventario:
    if item == busca:
        print(f"{busca.capitalize()} foi encontrado(a)!")
        break
else:
    print("Item não encontrado.")    
        
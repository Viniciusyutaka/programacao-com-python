personagem = [
    {"nome": "Bob Esponja", "idade": 40, "categoria": "desenho"},
    {"nome": "Moranguinho", "idade": 6, "categoria": "desenho"},
    {"nome": "Harry Postter", "idade": 15, "categoria": "ficção"},
    ]
for personagem in personagem:
    print("nome: ", personagem["nome"])
    print("idade: ", personagem["idade"])
    print("categoria: ", personagem["categoria"])
    print()
from repositorio import banco


def listarProdutos():
    print('----LISTA DE PRODUTOS----')
    for produto in banco:
        print(f"Codigo : {produto['codigo']}")
        print(f"Nome:{produto['nome']}")
        print(f"Categoria:{produto['categoria']}")
        print(f"Preço:{produto['preco']}")
        print('-'*50)



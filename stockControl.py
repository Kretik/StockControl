import re

def menu(): # Um monte de printkk
    print("\n1 - Adicionar Produto")
    print("2 - Atualizar Estoque")
    print("3 - Listar Produtos")
    print("4 - Pesquisar Produto")
    print("5 - Excluir Produto")
    print("6 - Exibir Valor Total do Estoque")
    print("7 - Sair")

def registerProduct(): # Registra o produto
    name = input("Nome:")
    quantity =  int(input("Quantidade: "))
    value = float(input("Preço: "))

    product = {"nome":name, "quantidade":quantity ,"valor":value}
    products.append(product) # Adiciona a lista
    while True:
        repeat = input("\nCadastra novamente? (y/n): \n").strip().lower()

        if repeat == "y":
            return True
        
        elif repeat == "n":
            return False
        
        else:
            print("Por gentileza retorne um valor correto!")

def productsList(): # Mostra os produtos cadastrados na lista
    if products:
        print("\nProdutos em estoque:\n")
        for i, product in enumerate(products):
            print(f"{i}. Nome: {product["nome"]} | {product["quantidade"]}un | R${product["valor"]}")
    else:
        print("\nNão há nenhum produto no estoque.\n")    

def backMenu():
    while True:
        back = input('\nPressione "0" para voltar: ').strip()
        if back == "0":
            break
        else:
            print("Por gentileza retorne um valor correto!")

products = []


while True: # Escolhe as opçoes do menu
    menu()
    choose = input("\nEscolha uma opção: \n").strip()

    if choose == "1":
        while registerProduct():
         pass # Quando o usuario selecionar 'n' voltará ao menu()

    elif choose == "2":
        if products:
            print("\nEscolha um produto para atualizar: ")
            productsList()

            try:
                    index = int(input("\nDigite o número do produto: "))
                    if  0 <= index < len(products):

                        print(f"\nProduto selecionado: {products[index]['nome']}") # Mostra o produto selecionado 
                        
                        while True: # Loop para verificar se o que o user digitou é válido para a opção.
                            name_input = input("\nDigite o novo nome |Ou Enter para não mudar!|:")
                            if name_input == "":
                                break
                            
                            if re.match("^[A-Za-zÀ-ÿ\s]+$", name_input): # Uso da biblioteca re para verificar se o nome não vai ser um número ou outro caractere
                                products[index]["nome"] = name_input
                                break
                            else:
                                print("\nNome inválido. O nome deve conter apenas letras e espaços. Tente novamente.")
                             

                        while True: # Loop para verificar se o que o user digitou é válido para a opção.
                            try:
                                products[index]["quantidade"] = int(input("Digite a nova quantidade |Ou Enter para não mudar!|:")) or products[index]["quantidade"]
                                break
                            except ValueError:
                                print("\nEntrada inválida. Tente novamente.\n")  

                        while True: # Loop para verificar se o que o user digitou é válido para a opção.
                            try:
                                products[index]["valor"] = float(input("Digite o novo valor |Ou Enter para não mudar!|:")) or products[index]["valor"]
                                break
                            except ValueError:
                                print("\nEntrada inválida. Tente novamente.\n")

                    print("\n- Produto atualizado com sucesso!")

            except:
                    print("\nEntrada inválida. Tente novamente.\n")

        else:
            print("\nNão há nenhum produto no estoque.\n")
            backMenu()
            
    elif choose == "3":
       productsList()
       backMenu()

    elif choose == "7":
        print("Saindo.. Até mais!")
        break
from time import sleep
from typing import List, Dict, Literal
from textwrap import dedent
from models.produto import Produto

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()
    pass


# Teste
# ps4 = Produto("Playstation4", 1789.44)
# xbox = Produto("Xbox", 1200.00)
# produtos.extend([ps4, xbox])


def menu() -> None:
    option: int = int(input(dedent("""
                ==================================
                ========== Bem-vindo(a) ==========  
                ==========  Geek Shop   ==========
                ==================================
                        
                Selecione uma opção abaixo:
                1 - Cadastrar produto
                2 - Listar produto
                3 - Comprar produto
                4 - Visualizar carrinho
                5 - Fechar pedido
                6 - Sair do sistema
                """)))

    match option:
        case 1:
            cadastro_produto()
        case 2:
            listar_produtos()
        case 3:
            comprar_produtos()
        case 4:
            visualizar_carrinho()
        case 5:
            fechar_pedido()
        case 6:
            print("Volte sempre!")
            exit()
        case _:
            print(dedent("""
            
            ==============
            Opção Inválida
            """))
            sleep(2)
            menu()


def cadastro_produto() -> None:
    print(dedent(
        """
        Cadastro de Produto
        ==================
        """))
    nome_produto: str = input("Informe o produto:  ")
    preco_produto: float = float(input("Informe o preço do produto: "))
    produto: Produto = Produto(nome_produto, preco_produto)
    produtos.append(produto)

    print(dedent(f"O produto {nome_produto} foi cadastrado com sucesso!"))
    print("")

    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print(dedent(
            """
            Listagem de produtos
            =================="""))
        for produto in produtos:
            print(produto)
            print("==================")
            sleep(1)

    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()


def comprar_produtos() -> None:
    if len(produtos) > 0:
        print(dedent("""
            Informe o código do produto que deseja adicionar ao carrinho:
            ============================================================
            =================== Produtos Disponíveis ===================
            """))
        for element in produtos:
            print(element)
            sleep(1)
            print("==================")

        codigo_produto: int = int(input())
        produto: Produto = pega_produto(codigo_produto)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(
                            f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(
                        f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()

        else:
            print(f'O produto com código {codigo_produto} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos para vender.')
    sleep(2)
    menu()


def visualizar_carrinho():
    if len(carrinho) > 0:
        print(dedent(
            """
                Produtos no carrinho
                =================="""))
        for item in carrinho:
            for produto in item.items():
                print(produto[0])
                print(f'Quantidade: {produto[1]}')
                print('=======================')
                sleep(1)
    else:
        print("Ainda não existem produtos no carrinho. ")

    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total = 0
        print("Produtos do Carrinho")

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}")
                valor_total += dados[0].preco*dados[1]
                print("=======================")
                sleep(1)
        print(f"Sua fatura é {valor_total:.2f}")
    else:
        print("Ainda não existem produtos no carrinho.")
    sleep(2)
    menu()


def pega_produto(codigo: int) -> Produto:
    for produto in produtos:
        if produto.codigo == codigo:
            match_produto = produto
    return match_produto


if __name__ == "__main__":
    main()

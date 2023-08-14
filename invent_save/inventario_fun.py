import csv 
produtos = {}
#Adição
def adicionar(produtos):
    dados = "save.csv"
    with open(dados, mode='a') as arquivo:
        escreve = csv.writer(arquivo)
    
        resp = input("Quer adicionar mais um produto? [S/N]: ").upper()
        while resp == 'S':
            nome = input("Entre com o nome do produto: ").title()
            qtd = int(input("Entre com a quantidade do produto: "))
            valor_compra = float(input("Entre com o valor do produto: "))
            departamento = input("Entre com o departamento do produto: ")
            valor_atual = valor_compra
            produtos[nome] = {'quantidade': qtd, 'valor_compra': valor_compra, 'departamento': departamento, 'valor_atual': valor_atual} 
            escreve.writerow([nome, qtd, valor_compra, departamento, valor_atual])
            resp = input("Quer adicionar mais um produto? [S/N]: ").upper()
            if resp == 'N':
                break

#Buscar Item
def buscar(nome, arquivo_csv):
    with open(arquivo_csv, mode='r') as arquivo:
        ler = csv.DictReader(arquivo)
        for linha in ler:
            if linha['nome'] == nome:
                return linha
     
            
#Depreciar Item
def depreciar(produtos): 
    deprecia = input("Qual o nome do item que voce esta buscando: ").title() 
    if deprecia in produtos:  
            porcento = 100 - float(input("Entre com a porcentagem de depreciação: ")) 
            valor_atual = valor_Compra * porcento/100
            print("\nNome......................", deprecia)
            print("Quantidade................", produtos[deprecia][0])
            print("Valor de Compra...........", produtos[deprecia][1])
            print("Departamento..............", produtos[deprecia][2])
            print("Valor atualizado..........", produtos[deprecia][3])
    else: 
        print("Item não localizado!")

def menu(op):
    print("=" * 20)
    print("MENU INVENTARIO")
    print("=" * 20)
    print("[1] - Adicionar produto")
    print("[2] - Buscar produto")
    print("[3] - Produtos")
    print("[4] - Remover produto")
    print("[5] - Sair")
    
    op = int(input("Digite uma opção: "))
    while op > 5:
        print("Opção invalida")
        op = input("Digite uma opção: ")
    return op


def mostraDados():
    dados = "save.csv"
    with open(dados, mode='r') as arquivo:
        ler = csv.reader(arquivo)
        organiza = next(ler)
        print("{:<15} {:<10} {:<15} {:<20} {:<15}".format(*organiza))
        for linha in ler:
            print("{:<15} {:<10} {:<15} {:<20} {:<15}".format(*linha))

def apagaItem(nome):
    dados = "save.csv"
    linhas = []
    with open(dados, mode='r') as arquivo:
        ler= csv.DictReader(arquivo)
        for linha in ler:
            if linha['nome'] != nome:
                linhas.append(linha)
    
    with open(dados, mode='w') as arquivo:
        organiza = ['nome', 'quantidade', 'valor_compra', 'departamento', 'valor_atual'] #header
        escritor = csv.DictWriter(arquivo, fieldnames=organiza) #coluna nome
        escritor.writeheader()
        escritor.writerows(linhas)
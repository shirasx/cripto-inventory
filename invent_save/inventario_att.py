from inventario_fun import *
from time import sleep
from Crypto.Cipher import AES

def encrypt(arquivo, key):
    with open(save, 'rb') as file:
        data = file.read()

    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)

    with open(save, 'wb') as file:
        file.write(nonce)
        file.write(tag)
        file.write(ciphertext)

def decrypt(arquivo, key):
    with open(save, 'rb') as file:
        nonce = file.read(16)
        tag = file.read(16)
        ciphertext = file.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    with open(save, 'wb') as file:
        file.write(data)



while True:
    chave = bytes("FIAPfiap20232023", "utf-8")
    save = "save.csv"
    encrypt(save, chave)
    escolha = 0
    escolha = menu(escolha)
    if escolha == 1:
        decrypt(save, chave)
        adicionar(produtos)
    elif escolha == 2:
        decrypt(save, chave)
        nome_busca = input("Digite o nome do produto: ").title()
        arquivo_csv = "save.csv"
        found = buscar(nome_busca, arquivo_csv)
        if found:
            print("Produto encontrado:")
            for chave, valor in found.items():
                print(f"{chave}: {valor}")
            sleep(2)
        else:
            print("Produto não encontrado.")
            sleep(2)
    elif escolha == 3:
        decrypt(save, chave)
        mostraDados()
    elif escolha == 4:
        decrypt(save, chave)
        nome_apaga = input("Nome do item para apagar: ")
        apagaItem(nome_apaga)
    elif escolha == 5:
        print("Saindo...")
        break
    else:
        print("Opção invalida.")




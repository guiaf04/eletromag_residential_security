import time
from motor import abrir_cofre, fechar_cofre
from rfid import verificar_cartao

# UID válido do cartão RFID
valid_uid = [0xDE, 0xAD, 0xBE, 0xEF]  # Substitua pelo UID do seu cartão

def main():
    while True:
        uid = verificar_cartao()  # Tenta ler o cartão
        if uid:
            print("Cartão detectado! UID:", [hex(i) for i in uid])
            if uid == valid_uid:
                print("Cartão válido!")
                abrir_cofre()
                time.sleep(10)  # Aguarda 10 segundos antes de fechar o cofre
                fechar_cofre()
            else:
                print("Cartão inválido!")
        else:
            print("Nenhum cartão detectado.")
        
        time.sleep(1)  # Aguarda 1 segundo antes de tentar ler novamente

if __name__ == "__main__":
    main()

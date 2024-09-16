from machine import Pin
from mfrc522 import MFRC522

# Pinos SPI para o módulo RFID RC522
sck = Pin(18)
mosi = Pin(19)
miso = Pin(16)
rst = Pin(5)
cs = Pin(17)

# Inicializando o leitor RFID
rfid = MFRC522(spi_id=0, sck=sck, mosi=mosi, miso=miso, rst=rst, cs=cs)

def verificar_cartao():
    (status, tag_type) = rfid.request(rfid.REQIDL)
    if status == rfid.OK:
        (status, uid) = rfid.anticoll()
        if status == rfid.OK:
            return uid
    return None

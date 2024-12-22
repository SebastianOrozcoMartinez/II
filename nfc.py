import board
import busio
import time
from adafruit_pn532.i2c import PN532_I2C

# Inicia la comunicación I2C
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c)  # No se necesita especificar la dirección

# Espera a que el dispositivo se inicialice y esté listo
print("Esperando por una tarjeta NFC...")

while True:
    # Intentar leer una tarjeta NFC
    uid = pn532.read_passive_target()
    if uid is not None:
        print("Tarjeta detectada con UID:", [hex(i) for i in uid])
        time.sleep(1)
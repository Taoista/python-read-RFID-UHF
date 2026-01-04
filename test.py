import serial
import time

PORT = "COM3"        # cambia si es necesario
BAUDRATE = 115200

def checksum(data):
    return sum(data) & 0xFF

ser = serial.Serial(PORT, BAUDRATE, timeout=0.5)
time.sleep(1)

# "HOLA MUNDO" en hex (EPC debe ir en pares de bytes)
epc_hex = [
    0x48, 0x4F,  # HO
    0x4C, 0x41,  # LA
    0x20, 0x4D,  #  M
    0x55, 0x4E,  # UN
    0x44, 0x4F   # DO
]

# WRITE EPC
# BB 00 49 | LEN | ANT | MEM | WORD_PTR | PWD | DATA | CRC | 7E
cmd = [
    0xBB, 0x00, 0x49,
    0x00, 0x13,        # length
    0x01,              # antenna
    0x02,              # EPC memory
    0x06,              # word pointer
    0x00, 0x00, 0x00, 0x00  # access password
] + epc_hex

crc = checksum(cmd[1:])
cmd.append(crc)
cmd.append(0x7E)

print("TX WRITE:", " ".join(f"{b:02X}" for b in cmd))
ser.write(bytes(cmd))

time.sleep(0.3)
resp = ser.read(100)

if resp:
    print("RX:", " ".join(f"{b:02X}" for b in resp))
else:
    print("RX: (sin respuesta)")

ser.close()



# 115200
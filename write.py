import serial
import time

PORT = "COM3"
BAUDRATE = 115200

# TEXTO a escribir en EPC (máximo ~12 caracteres, depende del tag)
TEXTO = "TAO123"

def texto_a_hex(texto):
    hex_data = texto.encode("ascii").hex()
    # Aseguramos que la cantidad de hex sea múltiplo de 4 (1 word = 2 bytes)
    if len(hex_data) % 4 != 0:
        hex_data += "00"
    return hex_data

def main():
    ser = serial.Serial(PORT, BAUDRATE, timeout=0.3)
    time.sleep(2)

    INVENTORY = bytes.fromhex("BB00220000227E")

    print("📡 Lector listo, acerque un TAG para grabar...\n")

    while True:
        ser.write(INVENTORY)
        time.sleep(0.3)

        raw = ser.read(512)
        if not raw or b"\xbb\x02\x22" not in raw:
            continue

        print("🟢 TAG detectado")

        # Convertimos texto a HEX
        data_hex = texto_a_hex(TEXTO)
        words = len(data_hex) // 4  # 1 word = 2 bytes = 4 hex chars

        # Comando WRITE EPC
        WRITE_HEX = (
            "BB0049"          # Header
            "000D"            # Longitud (dummy)
            "00"              # Antena
            "00000000"        # Password
            "01"              # EPC memory
            "0002"            # Dirección EPC (word 2)
            f"{words:02X}"    # Cantidad de palabras
            + data_hex +
            "7E"
        )

        ser.write(bytes.fromhex(WRITE_HEX))
        time.sleep(0.4)

        resp = ser.read(128)
        print("✍️ Escritura OK:", resp.hex())
        print("⏳ Retire el TAG...\n")
        time.sleep(2)

if __name__ == "__main__":
    main()

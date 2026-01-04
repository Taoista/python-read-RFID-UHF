import serial
import time

PORT = "COM3"
BAUDRATE = 115200

# Diccionario de TAGs (EPC HEX → Texto legible)
TAGS = {
    "E28011700000021B2F6F85F0": "Taoista Neumáticos",
    "E28011700000021B2F6F85F1": "Neumático de prueba",
    # Agrega más EPC aquí según tus tags
}

def extraer_epc_yrm100(raw_hex):
    """Extrae EPC de la respuesta INVENTORY del YRM100"""
    if "bb0222" not in raw_hex:
        return None

    idx = raw_hex.find("bb0222")
    length = int(raw_hex[idx+6:idx+10], 16)  # 2 bytes de length

    # EPC empieza después de bb0222(3 bytes) + length(2) + RSSI(1) + PC(2) = 8 bytes = 16 hex chars
    epc_start = idx + 16

    # EPC bytes = length - 5 (RSSI + PC + CRC)
    epc_len = (length - 5) * 2  # cada byte = 2 hex chars

    return raw_hex[epc_start:epc_start + epc_len].upper()

def main():
    ser = serial.Serial(PORT, BAUDRATE, timeout=0.5)
    time.sleep(2)

    INVENTORY = bytes.fromhex("BB00220000227E")
    print("📡 Lector listo, acerque un TAG...\n")

    while True:
        ser.write(INVENTORY)
        time.sleep(0.3)

        raw = ser.read(512)
        if not raw:
            print("⏳ Esperando TAG...")
            time.sleep(0.5)
            continue

        raw_hex = raw.hex()
        epc_hex = extraer_epc_yrm100(raw_hex)
        if not epc_hex:
            continue

        # Traducimos EPC a texto usando el diccionario
        epc_txt = TAGS.get(epc_hex, "(sin nombre)")

        print("🟢 EPC HEX :", epc_hex)
        print("📝 EPC TXT :", epc_txt)
        print("-"*40)
        time.sleep(1.5)

if __name__ == "__main__":
    main()

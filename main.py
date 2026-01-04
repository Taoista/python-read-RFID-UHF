import serial
import time

# ? puerto donde debe estar conectado
PORT = "COM3"
# ? velocidad de comunicacion debe coincidir con el lector
BAUDRATE = 115200

# ? espero tiempo por dato en este caso 0.2 segundos por dato
ser = serial.Serial(PORT, BAUDRATE, timeout=0.2)
# ? tiempo para que inicie correctamente
time.sleep(2)

print("📡 Lector UHF listo, acerque un TAG...\n")

# ? Comando INVENTORY UHF es un comando estandar escanea y dime que TAGs hay cerca
INVENTORY = bytes.fromhex("BB00220000227E")


# * funcion para pasar la data
#  TODO: DEBO BUCAR EN QUE MAS SE PUEDE APLICAR O QUE OTROS MOTIVOS TIENEN LOS DATOS DEL FRAME
def parse_uhf_frame(hex_raw: str) -> dict | None:
    """
    Parsea una respuesta UHF Inventory y devuelve sus campos.
    Retorna None si el frame no es valido.
    """
    try:
        # ? los datos los pasa de hex a bytes
        data = bytes.fromhex(hex_raw)

        # ? validaciones minimas
        if len(data) < 12:
            return None
        # ? evita errores a la lectura incompleta
        if data[0] != 0xBB or data[-1] != 0x7E:
            return None
        # ? debe iniciar con un BB y Terminar con un 7E
        if data[1] != 0x02 or data[2] != 0x22:
            return None
        # ? separa el frame en partess
        frame = {
            "header": data[0:1].hex().upper(),          # BB Inicio del frame (BB)
            "tipo": data[1:2].hex().upper(),            # 02 Tipo de respuesta
            "comando": data[2:3].hex().upper(),         # 22 INVENTORY
            "largo": data[3:5].hex().upper(),           # 00 11 Largo del mensaje
            "rssi_hex": data[5:6].hex().upper(),        # C0 Intensidad de señal en hex
            "rssi": int(data[5]),                       # RSSI decimal Intensidad de señal en decimal
            "extra": data[6:8].hex().upper(),           # 34 00 Datos del lector
            "epc": data[8:-3].hex().upper(),            # EPC ID DEL RFID
            "crc": data[-3:-1].hex().upper(),           # CRC control de errores
            "end": data[-1:].hex().upper()               # 7E el temrino del dato
        }

        return frame

    except Exception:
        return None


while True:
    # ? Limpiar buffer
    ser.reset_input_buffer()
    # ? envia el inventory o el codigo 
    ser.write(INVENTORY)
    time.sleep(0.2)
    # ? lee los bytes se ve asi la wea BB 02 22 00 11 C0 34 00 E2 80 11 70 00 00 02 1B 2F 6F 85 F0 0A 6C 7E
    data = ser.read(256)
    if not data:
        continue
    # ? muestra el dato crudo o real
    hex_raw = data.hex()
    print("📥 RAW:", hex_raw)

    # ? parsea el dato
    parsed = parse_uhf_frame(hex_raw)
    if parsed:
        print("🟢 TAG DETECTADO ✅")
        print("📌 EPC :", parsed["epc"])
        print("📶 RSSI:", parsed["rssi"])
        print("-" * 40)
        time.sleep(1)

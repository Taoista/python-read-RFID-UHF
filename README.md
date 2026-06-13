# 📡 Módulo lector RFID UHF YRM100 TTL con Python

Proyecto base para la **lectura de TAGs RFID UHF** utilizando el **módulo lector RFID UHF YRM100 TTL**, conectado por **puerto serial**, y un script en **Python** para capturar, interpretar y mostrar los datos del TAG.

Este proyecto forma parte de un sistema **IoT**, orientado al **control y trazabilidad de neumáticos**, con futura integración con **Flutter** y un **backend**.

---

## 🖼️ Módulo lector RFID UHF YRM100

A continuación se muestra el módulo lector utilizado en este proyecto:

Módulo lector RFID UHF YRM100
<p align="center"> <img src="https://i.ibb.co/QjrN69Vv/Screenshot-2026-01-04-172706.png" alt="Módulo lector RFID UHF YRM100 TTL" width="100"> </p>

> 📌 **Nota:** tiene el adaptador usb

link de descarga del driver

https://drive.google.com/file/d/12umlcMJ7ybuY_GG_qCyKnHlg813JQzcs/view?usp=sharing

---

## 🚀 Características

- Lectura de TAGs RFID UHF mediante el comando **INVENTORY**
- Comunicación serial TTL configurable
- Compatible con módulo **YRM100 UHF**
- Parseo del frame UHF
- Obtención de:
  - EPC del TAG
  - RSSI (intensidad de señal)
  - Datos crudos del frame
- Código simple y extensible para proyectos IoT

---

## 🧰 Tecnologías utilizadas

- Python 3.x
- pySerial
- Módulo RFID UHF YRM100 TTL
- ESP32 (opcional como bridge serial)
- Comunicación serial (UART / TTL)

---

## 📦 Notas

- El archivo **`main.py`** es el archivo oficial del proyecto.
- Los demás archivos son utilizados únicamente para pruebas.
- El módulo YRM100 se comunica mediante comandos UHF estándar.

---

## 📦 Requisitos

### 🔧 Hardware
- Módulo lector RFID UHF **YRM100 TTL**
- ESP32 (opcional)
- Antena UHF
- TAGs RFID UHF
- Conexión USB al computador

### 💻 Software
- Python 3.10 o superior
- Librería `pyserial`

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

---

## 🔁 Retorno de datos

El script procesa la respuesta del lector UHF y retorna un diccionario con la siguiente estructura:

```json
{
  "header": "BB",
  "tipo": "02",
  "comando": "22",
  "largo": "0011",
  "rssi_hex": "C0",
  "rssi": 192,
  "extra": "3400",
  "epc": "E28011700000021B2F6F85F0",
  "crc": "0A6C",
  "end": "7E"
}
```

### Descripción de campos

- **header**: Inicio del frame UHF (`BB`)
- **tipo**: Tipo de respuesta del lector
- **comando**: Comando ejecutado (`22` = INVENTORY)
- **largo**: Largo del mensaje
- **rssi_hex**: Intensidad de señal en hexadecimal
- **rssi**: Intensidad de señal en decimal
- **extra**: Datos adicionales del lector
- **epc**: Identificador único del TAG RFID
- **crc**: Código de verificación
- **end**: Fin del frame (`7E`)

---

## 📬 Mis Redes Sociales

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Taoista)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alberto-olave-carvajal-838482197/)
[![Instagram](https://img.shields.io/badge/Instagram-E1306C?style=flat&logo=instagram&logoColor=white)](https://www.instagram.com/alberto_olave73/)
[![Threads](https://img.shields.io/badge/Threads-000000?style=flat&logo=threads&logoColor=white)](https://www.threads.net/@alberto_olave73?hl=es-la)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=flat&logo=youtube&logoColor=white)](https://www.youtube.com/@devtao3753)
[![Web](https://img.shields.io/badge/Web-0078D4?style=flat&logo=internet-explorer&logoColor=white)](https://alberto-olave.cl)

---

<p align="center">
  ❤️ by <strong>Taoista</strong> · ¡Sígueme!
</p>

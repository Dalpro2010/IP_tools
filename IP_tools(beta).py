import requests
import os
import socket

def limpiar_pantalla():
    # Función para limpiar la pantalla dependiendo del sistema operativo
    if os.name == 'posix':  # Linux y macOS
        _ = os.system('clear')
    else:  # Windows
        _ = os.system('cls')

def obtener_info_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?lang=es&fields=66846719")
        data = response.json()

        if response.status_code != 200 or data['status'] != 'success':
            return "Error al obtener la información."

        ip_info = {
            "IP": data.get("query", "N/A"),
            "estado": data.get("status", "N/A"),
            "Zona Horaria": data.get("timezone", "N/A"),
            "continente": data.get("continent", "N/A"),
            "abreviatura continente": data.get("continentCode", "N/A"),
            "pais": data.get("country", "N/A"),
            "abreviatura país": data.get("countryCode", "N/A"),
            "región": data.get("regionName", "N/A"),
            "abreviatura región": data.get("region", "N/A"),
            "ciudad": data.get("city", "N/A"),
            "distrito": data.get("district", "N/A"),
            "código postal": data.get("zip", "N/A"),
            "latitud": data.get("lat", "N/A"),
            "longitud": data.get("lon", "N/A"),
            "diferencia horaria": data.get("offset", "N/A"),
            "moneda": data.get("currency", "N/A"),
            "isp": data.get("isp", "N/A"),
            "organización": data.get("org", "N/A"),
            "as": data.get("as", "N/A"),
            "as name": data.get("asname", "N/A"),
            "reverse": data.get("reverse", "N/A"),
            "consulta móvil": data.get("mobile", "N/A"),
            "proxy": data.get("proxy", "N/A"),
            "hosting": data.get("hosting", "N/A"),
        }

        info = "\n".join([f"{key}: {value}" for key, value in ip_info.items()])
        return info
    
    except Exception as e:
        return f"Ha ocurrido un error: {e}"

def obtener_ip(url):
    try:
        ip = socket.gethostbyname(url)
        return ip
    except socket.gaierror:
        return "No se pudo resolver la dirección IP."

def registrar_ip(ip):
    filename = "ips_recientes.txt"
    cambios = []

    if os.path.exists(filename):
        with open(filename, "r") as file:
            ips = file.read().splitlines()
    else:
        ips = []

    if ips:
        ultima_ip = ips[-1]
        if ip != ultima_ip:
            cambio = f"La IP ha cambiado de {ultima_ip} a {ip}."
            cambios.append(cambio)
        else:
            cambios.append("La IP no ha cambiado.")
    else:
        cambios.append(f"Primera IP registrada: {ip}.")

    ips.append(ip)
    with open(filename, "w") as file:
        file.write("\n".join(ips))
    
    return cambios

if __name__ == "__main__":
    while True:
        limpiar_pantalla()
        print("\n1. Obtener IP")
        print("2. Información de IP")
        opcion = input("\nSeleccione una opción (1 o 2): ")

        if opcion == '1':
            url = input("Ingrese la URL para obtener la IP: ")
            print("Obteniendo dirección IP...\n")
            ip = obtener_ip(url)
            print(f"La dirección IP es: {ip}")
            input("Presione Enter para continuar...")
        elif opcion == '2':
            ip = input("Ingrese la dirección IP: ")
            print("Obteniendo información de la IP...\n")
            info_ip = obtener_info_ip(ip)
            print(info_ip)

            cambios_ip = registrar_ip(ip)
            print("\n".join(cambios_ip))
            input("Presione Enter para continuar...")
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")
            input("Presione Enter para continuar...")

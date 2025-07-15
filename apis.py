#!/usr/bin/env python3
import json
import requests
from pathlib import Path
from datetime import datetime

API_URL = "http://ip-api.com/json/{ip}?fields=status,message,country,regionName,isp,lat,lon,query"

def consultar(ip: str) -> dict:
    """Devuelve un diccionario con la respuesta de IP‑API para la IP dada."""
    resp = requests.get(API_URL.format(ip=ip), timeout=5)
    return resp.json()

def mostrar(info: dict) -> None:
    """Imprime en consola los campos requeridos."""
    if info["status"] != "success":
        print(f" Error: {info.get('message', 'consulta fallida')}")
        return
    print(f"País           : {info['country']}")
    print(f"Región         : {info['regionName']}")
    print(f"ISP            : {info['isp']}")
    print(f"Coordenadas    : {info['lat']},{info['lon']}\n")

def main() -> None:
    resultados = []
    print("Consultor de geolocalización IP‑API (escribe 'exit' para salir) ")
    while True:
        ip = input("IP pública  ").strip()
        if ip.lower() == "exit":
            break
        datos = consultar(ip)
        mostrar(datos)
        # agrega marca de tiempo para que tu JSON sea trazable
        datos["timestamp"] = datetime.utcnow().isoformat()
        resultados.append(datos)

    # Guarda todos los resultados
    if resultados:
        Path("resultadosAP.json").write_text(
            json.dumps(resultados, ensure_ascii=False, indent=2)
        )
        print(f" Resultados guardados en {Path('resultadosAP.json').resolve()}")
    print("Programa finalizado.")

if __name__ == "__main__":
    main()

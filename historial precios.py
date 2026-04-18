import requests
from datetime import datetime

def convertir_fecha(fecha_input):
    try:
        fecha_limpia = fecha_input.split()[0]
        fecha_dt = datetime.strptime(fecha_limpia, "%y-%m-%d")
        return fecha_dt.strftime("%d-%m-%Y")
    except:
        return None


def obtener_precio_historico(coin_id, fecha):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/history"
    
    params = {
        "date": fecha,
        "localization": "false"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if "market_data" in data:
            precio = data["market_data"]["current_price"]["eur"]
            print(f"\n📅 Fecha: {fecha}")
            print(f"🪙 Moneda: {coin_id}")
            print(f"💶 Precio en EUR: {precio}\n")
        else:
            print("❌ No se encontraron datos para esa fecha o moneda.\n")

    except Exception as e:
        print(f"⚠️ Error: {e}\n")


# CABECERA
print("""
\t██████╗██████╗ ██╗██████╗ ████████╗ ██████╗ 
\t██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝██╔═══██╗
\t██║     ██████╔╝██║██████╔╝   ██║   ██║   ██║
\t██║     ██╔══██╗██║██╔═══╝    ██║   ██║   ██║
\t╚██████╗██║  ██║██║██║        ██║   ╚██████╔╝
\t╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝    ╚═════╝ 

\t   HISTORIAL DE PRECIOS CRYPTO @ Coingecko.com
""")

if __name__ == "__main__":

    while True:  # 🔁 BUCLE PRINCIPAL (nunca sale)
        coin = input("\nIntroduce el id de la moneda (ej: bitcoin): ").lower()

        while True:  # 🔁 BUCLE DE FECHAS
            entrada = input("\nIntroduce fecha (yy-mm-dd ...) o 's' para cambiar moneda: ").lower()

            if entrada == "s":
                print("🔄 Cambiando de moneda...\n")
                break  # sale solo del bucle de fechas

            fecha_convertida = convertir_fecha(entrada)

            if fecha_convertida:
                obtener_precio_historico(coin, fecha_convertida)
            else:
                print("❌ Formato inválido. Usa yy-mm-dd (ej: 21-03-15)\n")

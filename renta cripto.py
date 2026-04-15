# COLORES ANSI
COLOR_LETRA = ""
COLOR_FONDO = ""
RESET = ""


def calcular_impuesto(ganancia):
    tramos = [
        (6000, 0.19),
        (50000, 0.21),
        (200000, 0.23),
        (300000, 0.27),
        (float("inf"), 0.28)
    ]
    
    impuesto = 0
    restante = ganancia
    limite_anterior = 0

    for limite, tipo in tramos:
        if restante <= 0:
            break
        
        base_tramo = min(restante, limite - limite_anterior)
        impuesto += base_tramo * tipo
        
        restante -= base_tramo
        limite_anterior = limite

    return impuesto


# CABECERA
print(COLOR_FONDO + COLOR_LETRA + """
\t██████╗██████╗ ██╗██████╗ ████████╗ ██████╗ 
\t██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝██╔═══██╗
\t██║     ██████╔╝██║██████╔╝   ██║   ██║   ██║
\t██║     ██╔══██╗██║██╔═══╝    ██║   ██║   ██║
\t╚██████╗██║  ██║██║██║        ██║   ╚██████╔╝
\t╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝    ╚═════╝ 

\t   CALCULADORA CRIPTO HACIENDA
""" + RESET)


while True:
    try:
        entrada = input("\n💰 Introduce la ganancia (€) (o 'salir'): ")

        if entrada.lower() == "salir":
            print("👋 Programa finalizado.")
            break

        ganancia = float(entrada)

        if ganancia < 0:
            print("⚠️ La ganancia no puede ser negativa.")
            continue

        impuesto = calcular_impuesto(ganancia)
        neto = ganancia - impuesto

        print(COLOR_FONDO + COLOR_LETRA + "\n\t--- RESULTADO ---" + RESET)
        print(f"\tGanancia:        {ganancia:,.2f} €")
        print(f"\tImpuesto:        {impuesto:,.2f} €")
        print(f"\tGanancia neta:   {neto:,.2f} €")

    except ValueError:
        print("❌ Introduce un número válido o 'salir'.")
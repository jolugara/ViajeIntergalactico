import random

def SumaDeDados(Dado1, Dado2, Dado3):
    SumaDeDados = Dado1 + Dado2 + Dado3
    return SumaDeDados


def TirarDados():
    Dado1 = random.randrange(10)
    Dado2 = random.randrange(10)
    Dado3 = random.randrange(10)
    print("🎲🎲 Dados 🎲🎲")
    print(f"➡️Dado1: {Dado1}, Dado2: {Dado2}, Dado3: {Dado3}  ⬅️")
    print(f"1️⃣Primera suma de dados: {SumaDeDados(Dado1, Dado2, Dado3)}")
    Suma = SumaDeDados(Dado1, Dado2, Dado3)
    x = [int(a) for a in str(Suma)]
    print(f"2️⃣Segunda suma de dados: {x}")
    SumaTotal = sum(x)
    print(f"#️⃣Suma Final: {SumaTotal}")
    return SumaTotal

def partida():
    CasillaJugador = 0
    while(CasillaJugador <= 42 and CasillaJugador != 33):
        input("Volver a tirar")
        SumaTotal = TirarDados()
        CasillaJugador = CasillaJugador + SumaTotal
        CasillaJugador2 = 31
        resta = CasillaJugador - SumaTotal

        if SumaTotal <= 4:
            print(f"Avanzas a la casilla: {CasillaJugador}")
        else:
            print(f"No avanza casillas: {CasillaJugador}")

        if CasillaJugador2 == 31:
            print(resta)



partida()



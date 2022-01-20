import random

def TirarDados():
    SumaTotal = 42
    while (SumaTotal >= 42):
        Dado1 = random.randrange(10)
        Dado2 = random.randrange(10)
        Dado3 = random.randrange(10)
        print("🎲🎲 Dados 🎲🎲")
        print(f"➡️Dado1: {Dado1}, Dado2: {Dado2}, Dado3: {Dado3}  ⬅️")
        SumarDados = Dado1+Dado2+Dado3
        print(f"1️⃣Primera suma de dados: {SumarDados}")
        x = [int(a) for a in str(SumarDados)]
        print(f"2️⃣Segunda suma de dados: {x}")
        SumaTotal = sum(x)
        print(f"#️⃣Suma Final: {SumaTotal}")
        return SumaTotal
    print("fin")


ResultadoDados = TirarDados()

def GuarderDados():
    DadosGuardados = ResultadoDados
    return DadosGuardados


def ComprobarDados():
    if ResultadoDados <= 4:
        print("Avanzas casilla")
    else:
        print("Te quedas en la misma casilla")
print(ComprobarDados())

''''
def MoverseEnTablero():
    LugarTablero = 0
    while(ResultadoDados <= 4):
        MoverFicha = LugarTablero + ResultadoDados
        print(MoverFicha)
        return MoverFicha
print(MoverseEnTablero())
'''''
CasillaMaxima = 42
def iniciojuego():
    while (ResultadoDados >= CasillaMaxima):
        print(TirarDados())



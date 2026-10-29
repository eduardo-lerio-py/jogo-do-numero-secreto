import random
import json

ARQUIVO = "recordes.json"
frases = ("Tente novamente!", "Quase lá!", "Ops... Errou!", "Mais uma vez...", "Tenta outro!")

NIVEIS = {"1": {"nome": "Fácil", "maximo": 10, "tentativas": 5},
          "2": {"nome": "Médio", "maximo": 100, "tentativas": 7},
          "3": {"nome": "Difícil", "maximo": 1000, "tentativas": 10}}


def escolher_nivel():
    while True:
        nivel = input("Escolha um nível de 1 a 3: ")
        if nivel in NIVEIS:
            return NIVEIS[nivel]
        print("Nível inválido!")


def checar(segredo, adivinha):
    if segredo == adivinha:
        return 1
    elif segredo > adivinha:
        return 2
    else:
        return 0


def resultado(chute, segredo, adivinha):
    if chute == 1:
        print(f"Parabéns! O número era {segredo}")
    elif chute == 2:
        print(f"O número é MAIOR que {adivinha}")
    elif chute == 0:
        print(f"O número é MENOR que {adivinha}")


def jogar(nivel):
    segredo = random.randint(1, nivel["maximo"])
    usadas = 0
    print("Bem vindo ao jogo: Adivinhe o número!")
    print("\n"
          "======================================"
          "\n")
    print(f"Você escolheu o nível {nivel['nome']}")
    print(f"Você tem {nivel['tentativas']} tentativas para adivinhar um número de 1 a {nivel['maximo']}")

    while usadas < nivel['tentativas']:
        entrada = input("Qual o número secreto? ")

        if not entrada.isdigit():
            print("Insira um número inteiro...")
            continue

        adivinha = int(entrada)
        if not 1 <= adivinha <= nivel["maximo"]:
            print(f"Insira um número de 1 a {nivel['maximo']}")
            continue

        chute = checar(segredo, adivinha)
        resultado(chute, segredo, adivinha)
        usadas += 1

        if chute == 1:
            return usadas
        print(random.choice(frases))

        print("\n"
              "======================================"
              "\n")

    print(f"Acabaram as chances, o número era {segredo}...")
    return None


def carregar_recordes():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def salvar_recordes(recordes):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(recordes, f, ensure_ascii=False, indent=2)


def main():
    nivel = escolher_nivel()
    recordes = carregar_recordes()
    usadas = jogar(nivel)

    if usadas is None:
        print("Mais sorte na próxima!")
        return
    else:
        if usadas == 1:
            print(f"Você venceu em {usadas} tentativa!")
        else:
            print(f"Você venceu em {usadas} tentativas!")

    recorde = recordes.get(nivel["nome"])
    if recorde is None or usadas < recorde:
        print("Novo recorde!")
        recordes[nivel['nome']] = usadas
        salvar_recordes(recordes)
    else:
        print(f"O recorde do nível {nivel['nome']} é de {recorde} tentativa(s).")


if __name__ == "__main__":
    main()

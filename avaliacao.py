# > Exemplo de avaliação usando o dict
# > O código consiste em você responder cada pergunta com apenas uma alternativa (Padrão de prova tradicional)

print()
print("----Teste de Conhecimento----")
print("---/ MATEMÁTICA \---")

perguntas = {
    "Pergunta 01": {
        "Pergunta" : "Quanto é 10*2 ?",
        "Respostas" : {"A" : "5", "B" : "10", "C" : "20", "D" : "50"},
        "Resultado" : "C",
    },
    "Pergunta 02": {
        "Pergunta" : "Quanto é 5*5 ?",
        "Respostas" : {"A" : "5", "B" : "15", "C" : "25", "D" : "30"},
        "Resultado" : "C",
    },
    "Pergunta 03": {
        "Pergunta" : "Quanto é 100/4 ?",
        "Respostas" : {"A" : "5", "B" : "10", "C" : "20", "D" : "25"},
        "Resultado" : "D",
    },
    "Pergunta 04": {
        "Pergunta" : "Quanto é 40+80 ?",
        "Respostas" : {"A" : "100", "B" : "120", "C" : "150", "D" : "180"},
        "Resultado" : "B",
    },
    "Pergunta 05": {
        "Pergunta" : "Quanto é 10*3/2 ?",
        "Respostas" : {"A" : "15", "B" : "25", "C" : "40", "D" : "50"},
        "Resultado" : "A",
    },
}

Resultado = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["Pergunta"]}')

    print("Respostas: ")
    for rk, rv in pv ["Respostas"].items():
        print(f"[{rk}] : {rv}")

    resposta_usuario = input("Sua resposta: ")
    resposta_usuario = resposta_usuario.upper()

    if resposta_usuario.upper() == pv["Resultado"]:
        print("Certo")
        print("--------------")
        Resultado += 1 

    else:
        print("Errado")
        print("--------------")

print("Resultado do Teste: ")

qtd_perguntas = len(perguntas)
porcentagem = Resultado / qtd_perguntas * 100

print(f"Você acertou {Resultado} Respostas, de {qtd_perguntas} Perguntas")
print(f"Com um total de {porcentagem}% de acerto.")

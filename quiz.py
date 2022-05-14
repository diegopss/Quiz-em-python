import json
import random

#Esta função pega o arquivo JSON e retorna uma lista com as questoes
#OBS: AS VEZES O PYTHON NÃO RECONHECE O CAMINHO RELATIVO. (resolvi colocando o caminho absoluto)
def lista_questoes():
    with open("C:/Users/die-g/PROJETOS/Quiz-em-python/perguntas.json", encoding="utf8") as arquivo:

        json_perguntas = json.load(arquivo)
    
        return json_perguntas["questoes"]
        arquivo.close()
#esta função retorna uma só questao identificada pelo id
def questao(id):
    quetoes = lista_questoes()
    for questao in quetoes:
        if questao["id"] == id:
            return questao
#esta função retorna uma lista com os jogadores 
#OBS: AS VEZES O PYTHON NÃO RECONHECE O CAMINHO RELATIVO. (resolvi colocando o caminho absoluto)
def lista_jogadores():
     with open("C:/Users/die-g/PROJETOS/Quiz-em-python/jogadores.json","r") as arquivo:
        jogador = json.load(arquivo)
        
        return jogador
#esta função escreve os dados do jogador no Json
#OBS: AS VEZES O PYTHON NÃO RECONHECE O CAMINHO RELATIVO. (resolvi colocando o caminho absoluto)
def armazenar_jogador(nome,acertos):
    jogador = lista_jogadores()
    
    jogador["jogador"] += [{"nome": nome,"acertos":acertos}]
    with open("C:/Users/die-g/PROJETOS/Quiz-em-python/jogadores.json","w") as arquivo:        
        json.dump(jogador, arquivo, indent=4)

#Função que exibe um ranking dos jogadores(ainda não consegui fazer corretamente T_T )
def ranking():
    jogadores = lista_jogadores()   
    for jogador in jogadores["jogador"]:
        if jogador["acertos"] == 10:
            print("-------------------------------Jogadores nota 10-------------------------------")
            print(f"{jogador['nome']}  Nota: {jogador['acertos']} 🌟")

def quiz():
    acertos = 0
    for x in range(10):
        qtd_questoes = len(lista_questoes())
        id = random.randint(1,qtd_questoes)
        questao_random = questao(id)
        
        print("------------------------------------QUIZ------------------------------------")
        print(f"{questao_random['pergunta']}\n")
        print(f"1){questao_random['alt1']}")
        print(f"2){questao_random['alt2']}")
        print(f"3){questao_random['alt3']}")
        print(f"4){questao_random['alt4']}")
        print(f"5){questao_random['alt5']}\n")
        print("----------------------------------------------------------------------------")
        resp = input("Digite a alternativa correta: ")
        if resp == questao_random["correct_alt"]:
            acertos += 1
            print(f"Resposta correta ✅")
        else: print(f"Resposta incorreta ❌ (A alternativa correta era {questao_random['correct_alt']})")
    print("----------------------------------------------------------------------------")
    nome = input("Qual o seu nome? ")
    print(f"Parabéns {nome} você acertou {acertos} questões")
    armazenar_jogador(nome, acertos)    
    print("----------------------------------------------------------------------------")
    ranking()


quiz()

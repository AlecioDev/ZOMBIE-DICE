# Desenvolvedor: Gabriel Alecio Geteski Almeida || Aluno Curso de ADS PUCPR || Trabalho para composição de nota da Disciplina de Raciocinio Computacional

import random
import time

# Declara Dados
verde = ["CEREBRO", "PASSO", "CEREBRO", "TIRO", "PASSO", "CEREBRO"]
amarelo = ["TIRO", "PASSO", "CEREBRO", "TIRO", "PASSO", "CEREBRO"]
vermelho = ["TIRO", "PASSO", "TIRO", "CEREBRO", "PASSO", "TIRO"]

# Variaveis Somativas e de Controle
jogador_atual = 0
mao = []
tubo = []
dado_mao = []
Jogador = []
nomes = []

tiro = 0
passo = 0
cerebros = 0

pontos = dict()
pontos["cerebros"] = 0
pontos["passo"] = 0
pontos["tiro"] = 0

faces = ""

star_game = False

# Apresentação do Game
print("=" * 34)
print(f'\nPROTÓTIPO SEMANA 4 - ZOMBIE DICE\n')
print("=" * 34)

print("\nSEJA NEM VINDO AO JOGO ZOMBIE DICE!\n")
print("=" * 34)
time.sleep(1)

def cria_dados(tubo):
    for i in range(0, 6):
        tubo.append({"verde": verde})

    for i in range(0, 4):
        tubo.append({"amarelo": amarelo})

    for i in range(0, 3):
        tubo.append({"vermelho": vermelho})

# Lista pontos de cada jogador e exibe uma mensagem caso não tenha pontuado nada em alguma variavel
def listaPontos():
    time.sleep(1.5)
    print(f'Jogador {Jogador[jogador_atual]}:')
    try:
        time.sleep(0.5)
        print(f'CEREBRO: {nomes[jogador_atual]["cerebros"]}')
    except:
        time.sleep(0.5)
        print("Não COMEU nenhum cerebro!")
    try:
        time.sleep(0.5)
        print(f'PASSO: {nomes[jogador_atual]["passo"]}')
    except:
        time.sleep(0.5)
        print("Ninguem FUGIU do seu ATAQUE!!")
    try:
        time.sleep(0.5)
        print(f'TIRO: {nomes[jogador_atual]["tiro"]}')
    except:
        time.sleep(0.5)
        print("Não LEVOU nenhum TIRO!")
    try:
        print(f"Dados:{len(tubo)}")
    except:
        pass


def ReCriaDados():
    try:
        if len(tubo) <= 1:
            cria_dados(tubo)
        else:
            pass
    except:
        pass


# Condição de Loop onde funciona o Game.
while True:

    # Controle para inicio da partida
    try:
        start = int(input('\n(1 = SIM) / (2 = NÃO )\nDESEJA INICIAR A PARTIDA: '))
        if start == 1:
            star_game = True
        else:
            if start == 2:
                star_game = False
                print(f"Fecahndo o jogo...\n3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                print("Foi um prazer ter você por aqui, volte quando quiser comer mais alguns CEREBROS!!!")

                break
            else:
                print("\nEntrada Invalida, tente utilizar os números '1' e '2'! ")
                continue
    except:
        print("\nEntrada Invalida, tente utilizar os números '1' e '2'! ")
        continue

    numJogadores = 0

    # Condição Loop para dar entrada no número de jogadores
    while numJogadores < 2:
        try:
            numJogadores = int(input('\nEscreva a quantidade de jogadores: '))
            print("=" * 34)

            # Controle para número minimo de jogadores
            if numJogadores < 2:
                print('AVISO: São necessarios no minimo 2 jogadores!')
            else:
                continue

        # Econtrole em caso e entrada de valores diferentes de números inteiros
        except:
            print('AVISO: Entrada invalida, digite apenas números inteiros!')

    time.sleep(1)

    # Adicina nome aos Jogadores
    for i in range(numJogadores):
        nome = str(input(f'Escreva o nome do Jogador nº{i + 1} : '))
        nomes.append(nome)
        Jogador.append(nome)
        print(nomes[i])
        nomes[i] = dict()
        print("=" * 34)

    # Chama a função de criação dos dados
    print("\n Iniciando Partida...")
    time.sleep(2)
    cria_dados(tubo)

    # Inicia Partida
    while star_game == True:

        print("\n")
        print("=" * 34)

        # Seleciona 3 dados e a cada loop seleciona uma face e atribui o somatorio de pontos das devidas variaveis.
        for i in range(0, 3):
            mao.append(random.choice(tubo))
            ReCriaDados()

            # Verifica qual cor do dado.
            if "verde" in mao[i]:
                faces = random.choice(mao[i]["verde"])
                print(f"Dado Verde: {faces}")
                tubo.pop(verde in tubo)


                # Verifica qual a face e realiza atribuição aos diretorios referenciados aos jogadores para somatoria de pontos.
                if faces == 'CEREBRO':
                    try:
                        cerebros = cerebros + 1
                        nomes[jogador_atual]['cerebros'] = nomes[jogador_atual]['cerebros'] + cerebros
                        cerebros = 0
                    # Excessão caso não exista nenhum valor atribuido a algumavariavel do diretorio.
                    except:
                        nomes[jogador_atual]['cerebros'] = cerebros
                        cerebros = 0

                elif faces == 'PASSO':
                    try:
                        passo = passo + 1
                        nomes[jogador_atual]['passo'] = nomes[jogador_atual]['passo'] + passo
                        passo = 0
                    except:
                        nomes[jogador_atual]['passo'] = passo
                        passo = 0

                elif faces == 'TIRO':
                    try:
                        tiro = tiro + 1
                        nomes[jogador_atual]['tiro'] = nomes[jogador_atual]['tiro'] + tiro
                        tiro = 0
                    except:
                        nomes[jogador_atual]['tiro'] = tiro
                        tiro = 0
                try:
                    tubo.pop((tubo[jogador_atual]["verde"]))
                except:
                    pass

            elif "amarelo" in mao[i]:
                faces = random.choice(mao[i]["amarelo"])
                print(f"Dado Amarelo: {faces}")
                tubo.pop(amarelo in tubo)
                ReCriaDados()

                if faces == 'CEREBRO':
                    try:
                        cerebros = cerebros + 1
                        nomes[jogador_atual]['cerebros'] = nomes[jogador_atual]['cerebros'] + cerebros
                        cerebros = 0
                    except:
                        nomes[jogador_atual]['cerebros'] = cerebros
                        cerebros = 0

                if faces == 'PASSO':
                    try:
                        passo = passo + 1
                        nomes[jogador_atual]['passo'] = nomes[jogador_atual]['passo'] + passo
                        passo = 0
                    except:
                        nomes[jogador_atual]['passo'] = passo
                        passo = 0

                if faces == 'TIRO':
                    try:
                        tiro = tiro + 1
                        nomes[jogador_atual]['tiro'] = nomes[jogador_atual]['tiro'] + tiro
                        tiro = 0
                    except:
                        nomes[jogador_atual]['tiro'] = tiro
                        tiro = 0

                try:
                    tubo.pop((tubo[jogador_atual]["amarelo"]))
                except:
                    pass

            elif "vermelho" in mao[i]:
                faces = random.choice(mao[i]["vermelho"])
                print(f"Dado Vermelho: {faces}")
                tubo.pop(vermelho in tubo)

                if faces == 'CEREBRO':
                    try:
                        cerebros = cerebros + 1
                        nomes[jogador_atual]['cerebros'] = nomes[jogador_atual]['cerebros'] + cerebros
                        cerebros = 0
                    except:
                        nomes[jogador_atual]['cerebros'] = cerebros
                        cerebros = 0

                if faces == 'PASSO':
                    try:
                        passo = passo + 1
                        nomes[jogador_atual]['passo'] = nomes[jogador_atual]['passo'] + passo
                        passo = 0
                    except:
                        nomes[jogador_atual]['passo'] = passo
                        passo = 0

                if faces == 'TIRO':
                    try:
                        tiro = tiro + 1
                        nomes[jogador_atual]['tiro'] = nomes[jogador_atual]['tiro'] + tiro
                        tiro = 0
                    except:
                        nomes[jogador_atual]['tiro'] = tiro
                        tiro = 0

                try:
                    tubo.pop((tubo[jogador_atual]["vermelho"]))
                except:
                    pass

        # Limpa mao para proxima jogada
        mao.clear()

        # Verifica se o Jogador Atual Atingiu 13 Cerebros (Em desenvolvimento)
        try:
            if nomes[jogador_atual]['cerebros'] >= 13:
                print(f'Parabens Jogador {Jogador[jogador_atual]} , você comeu {cerebros} CEREBROS e venceu!')
                star_game = False
        except:
            pass

        # Verifica se o Jogador Não Perdeu a vez por Passos (Em desenvolvimento)
        try:
            if nomes[jogador_atual]['passo'] >= 3:
                nomes[jogador_atual]['passo'] = 0
                nomes[jogador_atual]['tiro'] = 0
                print(f'Suas presas fugiram {Jogador[jogador_atual]}, terá que passar a vez!')
                jogador_atual = int(input('Entre com o ID do jogador que irá continuar: \n (Ex: Jogador 1 = ID:1 )\n'))
                jogador_atual = jogador_atual - 1
                print(f"Vamos continuar com o jogador {Jogador[jogador_atual]}!")

        except:
            pass

        # Verifica se o Jogador Perdeu a vez por Tiros (Em desenvolvimento)
        try:
            if nomes[jogador_atual]['tiro'] >= 3:
                nomes[jogador_atual]['passo'] = 0
                nomes[jogador_atual]['tiro'] = 0
                print(f'Jogador {Jogador[jogador_atual]} levou 3 tiros e perdeu a vez!\n')
                jogador_atual = int(
                    input('Entre com o ID do jogador que irá continuar: \n (Ex: Jogador 1 = ID:1 )'))
                jogador_atual = jogador_atual - 1
                print(f"Vamos continuar com o jogador {Jogador[jogador_atual]}!")
        except:
            pass

        # Chame a função de Listagem de Pontos
        print("=" * 34)
        listaPontos()
        ReCriaDados()
        print("=" * 34)

        time.sleep(1)
        # Verifica se o Jogador quer ou não passar a rodada.
        rodada = int(input('Deseja passar a vez? \n 1: SIM \n 2: NÃO'))
        if rodada == 1 & rodada < 3:
            jogador_atual = int(input('Entre com o ID do jogador que irá continuar: \n (Ex: Jogador 1 = ID:1 )'))
            jogador_atual = jogador_atual - 1
            print(f"Vamos continuar com o jogador {Jogador[jogador_atual]}!")

            # Zera variaveis de controle de pontos para proxima rodada.
            cerebros = 0
            passo = 0
            tiro = 0

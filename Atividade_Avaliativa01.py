#Atividade Avaliativa 01 - Python - Gustavo Anibele

'''
1. O Reflorestador (Loop com Acumulador)
Em um mini-game de reflorestamento, o jogador deve plantar árvores até atingir uma meta de "Biomassa". 
Crie um programa que peça ao usuário a meta de biomassa (em unidades). 
Depois, use um while para ler sucessivamente o valor de biomassa de cada árvore plantada. 
O programa deve parar assim que a meta for atingida ou superada e exibir quantas árvores foram necessárias.
'''
meta = int(input("Digite a meta de biomassa: "))
contador = 0
arvores = 0
numero = 1
while contador < meta:
    biomassa= int(input("Digite a biomassa da árvore "+str(numero)+": "))
    contador += biomassa
    arvores += 1
    numero += 1
print("A meta foi atingida. Total de árvores = "+str(arvores)+" e biomassa = "+str(contador))

'''
2. Simulador de Combate: Turnos de RPG
Em um jogo de turno, um herói tem 100 de HP e enfrenta um monstro com 100 de HP. 
O programa deve pedir ao usuário o dano do ataque do herói e o dano do ataque do monstro por rodada. 
Use um while que continue enquanto ambos estiverem com HP acima de zero. Ao final de cada turno, mostre o HP restante de ambos. 
Se alguém chegar a 0, encerre e anuncie o vencedor.
'''
heroi_hp = 100
monstro_hp = 100
turno = 1
print("\n")
while heroi_hp > 0 and monstro_hp > 0:
    print("Iniciando o Turno "+str(turno))
    danoH = int(input("Digite o dano de ataque do herói: "))
    danoM = int(input("Digite o dano de ataque do monstro: "))
    heroi_hp -= danoM
    monstro_hp -= danoH
    print("HP do Herói: "+str(heroi_hp))
    print("HP do Monstro: "+str(monstro_hp))
    print("fim do turno "+str(turno)+"\n")
    turno += 1
if heroi_hp <= 0 and monstro_hp > 0:
    print("O monstro venceu!")
if monstro_hp <= 0 and heroi_hp > 0:
    print("O herói venceu!")
if heroi_hp <= 0 and monstro_hp <= 0:
    print("Empate! Ambos morreram.")
print("Fim do jogo.")

'''
3. Monitor de Inundação (Sentinela)
Você está desenvolvendo um sistema de alerta para uma Smart City. O programa deve ler o nível do rio (em metros) continuamente.

* Se o nível for menor que 3m: "Estado Normal".
* Entre 3m e 5m: "Estado de Alerta".
* Acima de 5m: "Evacuação Imediata".
O programa só deve encerrar a leitura se o usuário digitar um valor negativo (flag/bandeira de encerramento).
'''
leituraAtual = float(input("Digite o nível do rio (ou -1 para encerrar):"))
while leituraAtual >= 0:
    if leituraAtual < 3:
        print("Estado Normal")
    elif leituraAtual <= 5:
        print("Estado de Alerta")
    else:
        print("Evacuação Imediata")
    leituraAtual = float(input("Digite o nível do rio (ou -1 para encerrar):"))
print("Leitura encerrada. Monitoramento finalizado por digitar -1.")

'''
4. O Coletor de Itens e Inventário
Em um jogo de exploração, o jogador tem uma mochila com capacidade máxima de 15kg. 
Crie um programa que peça o peso de cada item encontrado no cenário, um por um. 
O while deve permitir a entrada de itens enquanto o peso total não ultrapassar 15kg.
Se um item ultrapassar o limite, o programa deve avisar "Mochila cheia, item descartado" e encerrar, mostrando o peso final total.
'''
print("iniciando Jogo...")
peso_atual = 0
cont = 1
while peso_atual < 15:
    peso_item = float(input("Digite o peso do item " +str(cont)+": "))
    cont += 1

    if peso_atual + peso_item > 15:
        print("Mochila cheia, item descartado.")
    else:
        peso_atual += peso_item
        print("Item adicionado. Peso atual da mochila: " + str(peso_atual) + " kg")
print("Fim de jogo. Peso final total na mochila: " + str(peso_atual) + " kg")

'''
5. Média de Temperatura Global
Para um painel informativo sobre mudanças climáticas, você precisa calcular a média de temperatura de um período.
O usuário deve informar quantos dias deseja analisar. Use o while para ler a temperatura de cada um desses dias.
Ao final, o programa deve exibir a média aritmética das temperaturas e informar se a média 
está "Acima do esperado" (caso seja maior que 25°C) ou "Dentro da normalidade".
'''
dias = int(input("Digite o número de dias que deseja analisar: "))
somaTemps = 0
contador = 1
while contador <= dias:
    temperatura = float(input("Digite a temperatura do dia " + str(contador) + ": "))
    somaTemps += temperatura
    contador += 1
media = somaTemps / dias
print("A média de temperatura global é: " + str(float(media)) + "°C")
if media > 25:
    print("A média está Acima do esperado.")
else:
    print("A média está Dentro da normalidade.")

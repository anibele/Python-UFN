#Aula02 -
print("Olá pessoal")
print("Primeira aula de programação prática com python")

'''
#Entrada de dados
Em python, para receber dados do usuário, utilizamos a função input()
A função input() recebe uma string como argumento, que é a mensagem que será exibida para o usuário. O valor digitado pelo usuário é retornado como uma string.
#Exemplo:
nome = input("Digite seu nome: ")
print("Olá", nome)
A função input() sempre retorna uma string, mesmo que o usuário digite um número. 
Se quisermos receber um número, precisamos converter a string para o tipo numérico desejado (int para inteiro ou float para decimal).
#Exemplo:
idade = int(input("Digite sua idade: "))
print("Você tem", idade, "anos")
Se o usuário digitar um valor que não pode ser convertido para o tipo numérico, o programa irá gerar um erro. 
Por isso, é importante validar a entrada do usuário antes de tentar converter para um tipo numérico.
'''
'''
#Operadores lógicos
Em python, temos os seguintes operadores lógicos:
and: retorna True se ambos os operandos forem verdadeiros
or: retorna True se pelo menos um dos operandos for verdadeiro
not: retorna True se o operando for falso
#Exemplo:
a = True
b = False
print(a and b) # False
print(a or b) # True
print(not a) # False
print(not b) # True
'''
'''
#Condicionais
Em python, utilizamos a estrutura if para criar condicionais. A sintaxe é a seguinte:
if condição:
  bloco de código a ser executado se a condição for verdadeira
else:
  bloco de código a ser executado se a condição for falsa
'''
'''
#Laços de repetição
Em python, temos os seguintes laços de repetição:
while: executa um bloco de código enquanto uma condição for verdadeira
for: executa um bloco de código para cada item em uma sequência (como uma lista ou um intervalo de números)
#Exemplo:

#Laço while
contador = 0
while contador < 5:
  print(contador)
  contador += 1 #contador = contador + 1  

#Laço for
for i in range(5):
  print(i)
'''
'''
#Listas
Em python, uma lista é uma coleção de itens ordenada e mutável. As listas são criadas usando colchetes [] e os itens são separados por vírgulas. 
#Exemplo:
frutas = ["maçã", "banana", "laranja"]
print(frutas[0]) # maçã
print(frutas[1]) # banana
print(frutas[2]) # laranja
As listas podem conter itens de diferentes tipos, como números, strings e até outras listas.
#Exemplo:
lista_mista = [1, "dois", 3.0, [4, 5]]
print(lista_mista[0]) # 1
print(lista_mista[1]) # "dois"
print(lista_mista[2]) # 3.0
print(lista_mista[3]) # [4, 5]  

#Podemos verificar se um elemento está na lista usando o operador in:
print("maçã" in frutas) # True
print("uva" in frutas) # False

#O contrário do operador in é o operador not in:
print("maçã" not in frutas) # False
print("uva" not in frutas) # True
'''
#Exercícios

#Exercício 1:
#Receber o nome e idade da pessoa e mostrar os anos dormidos
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
anos_dormidos = int(idade/3)
print(nome, "você já dormiu por",anos_dormidos, "anos")

#Exercício 2:
#receber nome, idade e sexo e dizer se é adulto ou criança
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade:" ))
sexo = input("Digite seu sexo [m ou f]: ")
if idade >= 18:
  if sexo == "f":
    print("você é adulta")
  if sexo == "m":
    print("você é adulto")
else:
  print("você é menor de idade")

#Exercício 3:
'''
Receber o nome de aluno, receber a nota do primeiro bimestre, do segundo, do terceiro e do quarto e calcular a media dos bimestres. após isso informar se o aluno está:
aprovado com media >= 7
recuperação media >= 5 ou media <7
reprovado media < 5
'''
nome = input("Digite o seu nome: ")
nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))
nota4 = int(input("Digite a nota 4: "))
media = (nota1 + nota2+ nota3 + nota4)/4

if media >= 7:
  print("Aprovado!")
if media >= 5 and media <7:
  print("Recuperacao")
if media < 5:
  print("Reprovado")

#Exercício 4:
#calculo de imc
nome = input("Digite o nome: ")
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

IMC = peso/(altura * altura)

print("o paciente",nome, "tem o imc:",IMC)

#Exercício 5:

'''
Receber o nome de um funcionário, o valor base da sua hora de trabalho, a quantidade de horas trabalhadas e o ano de ingresso na empresa.
calcular o salário do funcionario = valor base da hora * a quantidade de horas trabalhadas.
contudo, calcular quantos anos o funcionario está na empresa.
Se tem 4 a 8 anos, adicionar 4% ao salário.
Se tem 8 a 12 anos, adicionar 6% ao salário.
Se tem acima de 12 anos, adicionar 8% ao salário.
Ao final, exibir o nome e o salário do funcionário.

'''

nome = input("Digite o nome do funcionário:").upper()
valorBaseHora = float(input("Valor pago em R$ por hora trabalhada: "))
qtdHoras = int(input("Quantidade de horas trabalhadas:"))
tempoServico = 2026 - int(input("Digite o ano que entrou na empresa:"))

salario = valorBaseHora * qtdHoras
if tempoServico < 4:
  salario = salario * 1
if tempoServico >= 4 and tempoServico <8:
  salario = salario * 1.04
if tempoServico >= 8 and tempoServico <12:
  salario = salario * 1.06
if tempoServico > 12:
  salario = salario * 1.08

print("O salario de", nome,"é: R$", salario)

#Exercício 6:
'''
fazer um programa que receba a sigla de um estado brasileiro, contudo, enquanto a sigla digitada não for válida, o programa deve solicitar novamente ao usuário
'''
estado = input("Digite uma sigla de uma estado: ").upper()
estados_uf = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
    "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC",
    "SP", "SE", "TO"]

while estado not in estados_uf:
    print("A sigla digitada não é uma UF válida, por favor digite novamente...")
    estado = input("Digite uma sigla de uma estado: ").upper()

print("O estado digitado é válido!")

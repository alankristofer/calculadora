import tkinter as tk
from tkinter import *
from tkinter import ttk

#cores
cor1 = "#3b3b3b" # black/ preto
cor2 = "#feffff" # white/ branco
cor3 = "#38576b" # azul forte
cor4 = "#ECEFF1" # cinzento
cor5 = "#FFAB40" # Laranja/ orange
cor6 = "#0abef5" # azul claro

#janela da aplicaçao
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x301")
janela.config(background=cor1) #fundo do frame

#separando a tela em frames.
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height= 268)
frame_corpo.grid(row=1, column=0)


# variavel todos os valores

todos_valores = ''
def inserir_valor_texto(texto):
    global todos_valores
    todos_valores += texto
    valor_texto.set(todos_valores)


def entrar_numero0():
    inserir_valor_texto('0') 

def entrar_numero1():
    inserir_valor_texto('1')

def entrar_numero2():
    inserir_valor_texto('2')

def entrar_numero3():
    inserir_valor_texto('3')

def entrar_numero4():
    inserir_valor_texto('4')    

def entrar_numero5():
    inserir_valor_texto('5')    

def entrar_numero6():
    inserir_valor_texto('6')    

def entrar_numero7():
    inserir_valor_texto('7')

def entrar_numero8():
    inserir_valor_texto('8')    

def entrar_numero9():
    inserir_valor_texto('9')

# criando funcao
def entrar_valores(event):
    print (event)
    global todos_valores

    todos_valores = todos_valores + str(event)
    
    #passando o valor para a tela
    valor_texto.set(todos_valores)

# função para multiplicação
def multi():
    inserir_valor_texto("*")

# função para divisão
def divisao():
    inserir_valor_texto("/") 

# função para somar
def soma():
    inserir_valor_texto("+")

#função para subtrair
def subtrair():
    inserir_valor_texto("-")

# função para porcentagem
def porcentagem():
    inserir_valor_texto("%")  

# função para calcular o resultado
def igual():
    global todos_valores
    try:
        resultado = eval(todos_valores)
        if float(int(resultado))==resultado:
            resultado= int(resultado)
        valor_texto.set(resultado)
        todos_valores = str(resultado)
    except Exception as e:
        valor_texto.set("Erro")
        todos_valores = ''

#função-limpar
def limpar():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

def adicionar_ponto_decimal():
    global todos_valores
    if '.' not in todos_valores.split()[-1]:
        todos_valores += '.'
        valor_texto.set(todos_valores)


# criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 '), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)


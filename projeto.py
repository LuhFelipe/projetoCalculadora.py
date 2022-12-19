from tkinter import *  #importando tkinter
from tkinter import ttk

#cores para utilizar no programa
cor1 = "#000000" #cor preto
cor2 = "#a8a8a8" #cor cinza
cor3 = "#feffff" #cor branca
cor4 = "#38576b" #cor azul
cor5 = "#FFAB40" #cor laranja

#janela
janela = Tk()
janela.title("Calculadora") #nome da janela
janela.geometry("235x310") #tamanho da janela
janela.config(bg=cor1) # bg = background

#criando frame
frameTela = Frame(janela, width = 235, height = 50, bg=cor4) #frame do display
frameTela.grid(row = 0, column = 0) #fileira e coluna

frameCorpo = Frame(janela, width=235, height=268)
frameCorpo.grid(row = 1,column = 0)



#variavel todos valores
todosValores = ""

#criando label
valorTexto = StringVar()

appLabel = Label(frameTela, textvariable = valorTexto, width = 16, height = 2, padx = 7, relief = FLAT, anchor = "e", justify = RIGHT, font = "Ivy 18", bg = cor4, fg = cor3)
appLabel.place(x = 0, y = 0)

#criando função
def entrarValores(event):

    global todosValores
    todosValores += str(event)

    #passando valor para o display
    valorTexto.set(todosValores)

#função para calcular
def calcular():
    global todosValores
    resultado = eval(todosValores)
    
    valorTexto.set(str(resultado))

#função limpar tela
def limparTela():
    global todosValores
    todosValores = ""
    valorTexto.set("")


#criando botões
#primeira coluna##########
b1 = Button(frameCorpo, command = limparTela, text = "C", width = 11, height = 2, bg = cor2, font =("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b1.place(x = 0, y = 0)
b2 = Button(frameCorpo, command = lambda: entrarValores("%"), text = "%", width = 5,height = 2, bg = cor2, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b2.place(x = 118, y = 0)
b3 = Button(frameCorpo, command = lambda: entrarValores("/"),text = "/", width = 5, height = 2, bg = cor5, fg = cor3, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b3.place(x = 177, y = 0)

#segunda coluna############
b4 = Button(frameCorpo, command = lambda: entrarValores("7"), text = "7", width = 5,height = 2, bg = cor2, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b4.place(x = 0, y = 52)
b5 = Button(frameCorpo, command = lambda: entrarValores("8"),text = "8", width = 5,height = 2, bg = cor2, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b5.place(x = 59, y = 52)
b6 = Button(frameCorpo, command = lambda: entrarValores("9"),text = "9", width = 5,height = 2, bg = cor2, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b6.place(x = 118, y = 52)
b7 = Button(frameCorpo, command = lambda: entrarValores("*"),text = "*", width = 5, height = 2, bg = cor5, fg = cor3, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b7.place(x = 177, y = 52)

#terceira coluna##########
b8 = Button(frameCorpo, command = lambda: entrarValores("4"),text = "4", width = 5,height = 2, bg = cor2, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b8.place(x = 0, y = 104)
b9 = Button(frameCorpo, command = lambda: entrarValores("5"),text = "5", width = 5,height = 2, bg = cor2, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b9.place(x = 59, y = 104)
b10 = Button(frameCorpo, command = lambda: entrarValores("6"),text = "6", width = 5,height = 2, bg = cor2, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b10.place(x = 118, y = 104)
b11 = Button(frameCorpo, command = lambda: entrarValores("-"),text = "-", width = 5, height = 2, bg = cor5, fg = cor3, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b11.place(x = 177, y = 104)

#quarta coluna###########
b12 = Button(frameCorpo, command = lambda: entrarValores("1"),text = "1", width = 5,height = 2, bg = cor2, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b12.place(x = 0, y = 156)
b13 = Button(frameCorpo, command = lambda: entrarValores("2"),text = "2", width = 5,height = 2, bg = cor2, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b13.place(x = 59, y = 156)
b14 = Button(frameCorpo, command = lambda: entrarValores("3"),text = "3", width = 5,height = 2, bg = cor2, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b14.place(x = 118, y = 156)
b15 = Button(frameCorpo, command = lambda: entrarValores("+"),text = "+", width = 5, height = 2, bg = cor5, fg = cor3, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b15.place(x = 177, y = 156)

#quinta coluna
b12 = Button(frameCorpo, command = lambda: entrarValores("0"),text = "0", width = 11,height = 2, bg = cor2, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b12.place(x = 0, y = 208)
b13 = Button(frameCorpo, command = lambda: entrarValores("."),text = ".", width = 5,height = 2, bg = cor2, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b13.place(x = 118, y = 208)
b15 = Button(frameCorpo, command = calcular, text = "=", width = 5, height = 2, bg = cor5, fg = cor3, font = ("Ivy 13 bold"), relief = RAISED, overrelief = RIDGE)
b15.place(x = 177, y = 208)





janela.mainloop()
print("")
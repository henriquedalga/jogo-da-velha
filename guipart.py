
from tkinter import *




contador = 0

def jogar():

    quadrado00 = Button(root, padx=20, pady= 20, command=lambda: [preencha(quadrado00), conta()])
    quadrado01 = Button(root, padx=20, pady= 20, command=lambda: [preencha(quadrado01), conta()])
    quadrado02 = Button(root, padx=20, pady= 20, command=lambda: [preencha(quadrado02), conta()])
    quadrado10 = Button(root, padx=20, pady= 20, command=lambda: [preencha(quadrado10), conta()])
    quadrado11 = Button(root, padx=20, pady= 20, command=lambda: [preencha(quadrado11), conta()])
    quadrado12 = Button(root, padx=20, pady= 20, command=lambda: [preencha(quadrado12), conta()])
    quadrado20 = Button(root, padx=20, pady= 20, command=lambda: [preencha(quadrado20), conta()])
    quadrado21 = Button(root, padx=20, pady= 20, command=lambda: [preencha(quadrado21), conta()])
    quadrado22 = Button(root, padx=20, pady= 20, command=lambda: [preencha(quadrado22), conta()])
    #alocando os quadrados
    quadrado00.grid(row=3, column=0) 
    quadrado01.grid(row=3, column=1)
    quadrado02.grid(row=3, column=2)
    quadrado10.grid(row=4, column=0)
    quadrado11.grid(row=4, column=1)
    quadrado12.grid(row=4, column=2)
    quadrado20.grid(row=5, column=0)
    quadrado21.grid(row=5, column=1)
    quadrado22.grid(row=5, column=2)
    
    
    
def preencha(botao):
    if contador%2 == 0:
        botao.config(text="x")
    else:
        botao.config(text="O")

def conta():
    global contador
    contador = contador + 1




root = Tk()
root.title("jogo da velha")
mylabel = Label(root, text="Jogo da velha")
mylabel.grid()

botaojogar = Button(root, text="iniciar partida", padx=150, pady= 20, command=jogar)
botaojogar.grid(row= 1, column=0, columnspan=3)


root.mainloop()

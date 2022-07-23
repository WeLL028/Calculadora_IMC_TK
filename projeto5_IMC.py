##### Calculadora de IMC ###### Indice de Massa Corporal 

#Cores 

cor1 = '#1e1f1e' # preto 
cor2 = '#feffff' # branco
cor3 = '#38576b' # azul
cor4 = '#ECEFF1' # cizenta 
cor5 = '#FFAB40' # laranja

# importa tkinter# 

import re
from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title('IMC by WeLL 📳')
janela.geometry('355x250') # comprimentoXaltura
janela.resizable(width=False,height=False)
janela.configure(bg=cor2)

# Divisão de frames ##

frame_cima=Frame(janela,width=500,height=40, bg=cor1, pady=0,padx=0, relief='flat')
frame_cima.grid(row=0,column=0,sticky=NSEW)

frame_baixo=Frame(janela,width=500,height=180, bg=cor1, pady=0,padx=0, relief='flat')
frame_baixo.grid(row=1,column=0,sticky=NSEW)


#Configurão frame cima #

nome_app = Label(frame_cima, text='Calculadora de IMC',width=23, height=1,padx=0,relief='flat',anchor='center', font=('Ivy 16 bold'),bg=cor1,fg=cor5)
nome_app.place(x=0,y=0)

# Linha da Cal IMC 
linha_app = Label(frame_cima, text='',width=500, height=1,padx=0,relief='flat',anchor='center', font=('Ivy 1'),bg=cor5,fg=cor5)
linha_app.place(x=0,y=35)

#Funcão

def calcular():
    # Logica da calculadora IMC ## Função

    peso = float(e_peso.get())
    altura = float(e_altura.get())

    imc = peso / altura**2

    resultado_imc = imc

    if resultado_imc < 18.5:
        l_resultado_text['text'] ='Seu IMC é: Abaixo do peso'

    elif resultado_imc >= 18.5 and resultado_imc < 25:
        l_resultado_text['text'] =  'Seu IMC é: Normal'  

    elif resultado_imc >= 25 and resultado_imc < 30:
        l_resultado_text['text'] = 'Seu IMC é: Sobrepeso'

    else:
        l_resultado_text['text'] =  'Seu IMC é: Obesidade'  

    l_resultado['text'] = '{:.{}f}'.format(resultado_imc, 2)

    #print(resultado_imc)


#Configurão frame baixo #

l_peso = Label(frame_baixo, text='Insira seu Peso: ',height=1,padx=0,relief='flat',anchor='center', font=('Ivy 10 bold'),bg=cor1,fg=cor5)
l_peso.grid(row=0,column=0,sticky=NSEW, pady=10, padx=3)

e_peso = Entry(frame_baixo,width=5,relief='solid', font=('Ivy 10 bold'),justify='center')
e_peso.grid(row=0,column=1,sticky=NSEW, pady=10, padx=3)

l_altura = Label(frame_baixo, text='Insira sua Altura: ',height=1,padx=0,relief='flat',anchor='center', font=('Ivy 10 bold'),bg=cor1,fg=cor5)
l_altura.grid(row=1,column=0,sticky=NSEW, pady=10, padx=3)

e_altura = Entry(frame_baixo,width=5,relief='solid', font=('Ivy 10 bold'),justify='center')
e_altura.grid(row=1,column=1,sticky=NSEW, pady=10, padx=3)

# Resultado 

l_resultado = Label(frame_baixo,text='---',width=5,height=2,padx=12,relief='flat',anchor='center', font=('Ivy 24 bold'),bg=cor5,fg=cor2)
l_resultado.place(x=210,y=5)


l_resultado_text = Label(frame_baixo,text='',width=30,height=2,padx=0,relief='flat',anchor='center', font=('Ivy 10 bold'),bg=cor1,fg=cor2)
l_resultado_text.place(x=2,y=95)

b_calcular = Button(frame_baixo,command=calcular,text='Calcular',width=10,height=2,overrelief=SOLID,relief='raised',anchor='center', font=('Ivy 10 bold'),bg=cor5,fg=cor2)
b_calcular.grid(row=10,column=0,sticky=NE,pady=60,padx=5,columnspan=3)



#parei 29:55

janela.mainloop()

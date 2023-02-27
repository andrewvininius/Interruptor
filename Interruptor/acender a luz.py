#importar o tkinter

from tkinter import *

from PIL import Image, ImageTk

import random

# cores 
co0 = "#f0f3f5"  # cizenta / grey
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor
co4 = "#403d3d"  # preta / black

janela = Tk()
janela.title("")
janela.geometry("400x260")
janela.configure(background=co4)
janela.resizable(width=False, height=False)

#criar frame
frame_cima = Frame(janela, width=500, height=50, bg= co4)
frame_cima.grid(row=0, column=0, pady=1, padx= 0, sticky= NSEW )

frame_baixo = Frame(janela, width=500, height=210, bg= co4)
frame_baixo.grid(row=1, column=0, pady=1, padx= 0, sticky= NSEW )

#configurano frame em cima 

l_app = Label(frame_cima, text='Acenda a Lâmpada', anchor=NE, font=('Ivy 20'),bg=co4, fg='white')
l_app.place(x=5,y=5)

#configurano frame em baixo

img_2 = Image.open('2.png')
img_2 = img_2.resize((40,40))
img_2 = ImageTk.PhotoImage(img_2)

img_3 = Image.open('3.png')
img_3 = img_3.resize((40,40))
img_3 = ImageTk.PhotoImage(img_3)

img_4 = Image.open('4.png')
img_4 = img_4.resize((40,40))
img_4 = ImageTk.PhotoImage(img_4)

img_5 = Image.open('5.png')
img_5 = img_5.resize((40,40))
img_5 = ImageTk.PhotoImage(img_5)

#imagem
l_img = Label(frame_baixo, image= img_2,bg=co4)
l_img.place(x=30,y=10)

#texto
l_estado = Label(frame_baixo, text='Está Escuro', anchor=NW, font=('Ivy 13'),bg=co4, fg=co1)
l_estado.place(x=80,y=20)

global control

def ligar_lampada(i):
    global control
    lista = i
    # desabilitando o botao que foi clicado
    if lista[1] == 'interuptor - 1':
        b_interruptor_1['state'] = 'disable'
    elif lista[1] == 'interuptor - 2':
        b_interruptor_2['state'] = 'disable'   
    elif lista[1] == 'interuptor - 3':
        b_interruptor_3['state'] = 'disable' 
    elif lista[1] == 'interuptor - 4':
        b_interruptor_4['state'] = 'disable' 
    else: 
        b_interruptor_5['state'] = 'disable'

    def subistituir_valor(i): 
        global control
        nova_lista = []
        for string in control:
            novo_valor = string.replace(i[0],i[1]) 
            nova_lista.append(novo_valor)   

        control  = nova_lista           

    #Valor aleatorio

    valor_selecionado = random.sample(lista[0],1)[0]
    if int(valor_selecionado) == 1:
        if control[0] == 'lampada_1':
            l_img_1['image'] = img_lampada_on
            l_img['image'] = img_3
            l_estado['text'] = 'Ok obrigado'
            subistituir_valor(['lampada_1',str(1)])
        else:
            if control[1] == 'lampada_2':
                l_img_2['image'] = img_lampada_on
                l_img['image'] = img_4
                l_estado['text'] = 'Por favor, acenda todas as luz'
                subistituir_valor(['lampada_2',str(2)])
            else:
                if control[2] == 'lampada_3':
                    l_img_3['image'] = img_lampada_on
                    l_img['image'] = img_5
                    l_estado['text'] = 'Muito Obrigado! '
                    subistituir_valor(['lampada_3',str(3)])     
            
        



control = ['lampada_1','lampada_2','lampada_3']

#lampadas
img_lampada_on = Image.open('1.png')
img_lampada_on = img_lampada_on.resize((110,110))
img_lampada_on = ImageTk.PhotoImage(img_lampada_on)

img_lampada_off = Image.open('0.png')
img_lampada_off = img_lampada_off.resize((110,110))
img_lampada_off = ImageTk.PhotoImage(img_lampada_off)

#lampadas apagadas

l_img_1 = Label(frame_baixo, image= img_lampada_off,bg=co4)
l_img_1.place(x=5,y=70)

l_img_2 = Label(frame_baixo, image= img_lampada_off,bg=co4)
l_img_2.place(x=105,y=70)

l_img_3 = Label(frame_baixo, image= img_lampada_off,bg=co4)
l_img_3.place(x=205,y=70)

lista = [0,1,1,1,0]

#criando botao

b_interruptor_1 = Button(frame_baixo, command=lambda i=[lista,'interuptor - 1']: ligar_lampada(i),text='Interruptor- 1', anchor=NW, font=('Ivy 9 bold'),relief=RAISED, overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_1.place(x=300,y=50)

b_interruptor_2 = Button(frame_baixo, command=lambda i=[lista,'interuptor - 2']: ligar_lampada(i), text='Interruptor- 2', anchor=NW, font=('Ivy 9 bold'),relief=RAISED, overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_2.place(x=300,y=80)

b_interruptor_3 = Button(frame_baixo, command=lambda i=[lista,'interuptor - 3']: ligar_lampada(i), text='Interruptor- 3', anchor=NW, font=('Ivy 9 bold'),relief=RAISED, overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_3.place(x=300,y=110)

b_interruptor_4 = Button(frame_baixo, command=lambda i=[lista,'interuptor - 4']: ligar_lampada(i),text='Interruptor- 4', anchor=NW, font=('Ivy 9 bold'),relief=RAISED, overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_4.place(x=300,y=140)

b_interruptor_5 = Button(frame_baixo, command=lambda i=[lista,'interuptor - 5']: ligar_lampada(i),text='Interruptor- 5', anchor=NW, font=('Ivy 9 bold'),relief=RAISED, overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_5.place(x=300,y=170)


janela.mainloop()

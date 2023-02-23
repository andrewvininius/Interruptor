#importar o tkinter

from tkinter import *

from PIL import Image, ImageTk 

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
janela.resizable(width=FALSE, height=FALSE)

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

#lampadas
img_lampada_on = Image.open('1.png')
img_lampada_on = img_lampada_on.resize((110,110))
img_lampada_on = ImageTk.PhotoImage(img_lampada_on)

img_lampada_off = Image.open('0.png')
img_lampada_off = img_lampada_off.resize((110,110))
img_lampada_off = ImageTk.PhotoImage(img_lampada_off)

#lampadas apagadas

l_img = Label(frame_baixo, image= img_lampada_off,bg=co4)
l_img.place(x=5,y=70)

l_img = Label(frame_baixo, image= img_lampada_off,bg=co4)
l_img.place(x=105,y=70)

l_img = Label(frame_baixo, image= img_lampada_off,bg=co4)
l_img.place(x=205,y=70)

#criando botao

b_interruptor_1 = Button(frame_baixo, text='Interruptor- 1', anchor=NW, font=('Ivy 9 bold'),relief=RAISED, overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_1.place(x=300,y=50)

b_interruptor_2 = Button(frame_baixo, text='Interruptor- 2', anchor=NW, font=('Ivy 9 bold'),relief=RAISED, overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_2.place(x=300,y=80)

b_interruptor_3 = Button(frame_baixo, text='Interruptor- 3', anchor=NW, font=('Ivy 9 bold'),relief=RAISED, overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_3.place(x=300,y=110)

b_interruptor_4 = Button(frame_baixo, text='Interruptor- 4', anchor=NW, font=('Ivy 9 bold'),relief=RAISED, overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_4.place(x=300,y=140)

b_interruptor_5 = Button(frame_baixo, text='Interruptor- 5', anchor=NW, font=('Ivy 9 bold'),relief=RAISED, overrelief=RIDGE, bg=co4, fg=co1)
b_interruptor_5.place(x=300,y=170)


janela.mainloop()

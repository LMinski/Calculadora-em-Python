
from doctest import OutputChecker
from tkinter import *
from turtle import color, right

root=Tk()
root.title("Calculadora")
root.geometry("350x464")

label_display= Label(root, width=350, height=5, bg="#ECEFF1")
label_display.place(x=0,y=0)


visor= Entry(root, font=('Ivy 22'), bg="#3b3b3b", justify=RIGHT, foreground ='white')
visor.place(x=0,y=0, height=74, width=350)



#função dos botões

def click_soma():
   primeiro_numero = visor.get()
   global p_numero
   global matematica
   matematica = "soma"
   p_numero = float(primeiro_numero)
   visor.delete(0, END)

def click_sub():
   primeiro_numero = visor.get()
   global p_numero
   global matematica
   matematica = "subtracao"
   p_numero = float(primeiro_numero)
   visor.delete(0, END)

def deletar():
   visor.delete(0, END)

def click_ponto():
   visor.insert(END, ".")


def click_mult():
   primeiro_numero = visor.get()
   global p_numero
   global matematica
   matematica = "multiplicao"
   p_numero = float(primeiro_numero)
   visor.delete(0, END)


def click_divi():
   primeiro_numero = visor.get()
   global p_numero
   global matematica
   matematica = "divisao"
   p_numero = float(primeiro_numero)
   visor.delete(0, END)

def click_igual():
   segundo_numero = visor.get()
   visor.delete(0, END)
   if matematica == 'soma':
      visor.insert(0, p_numero + float(segundo_numero))

   if matematica == 'subtracao':
      visor.insert(0, p_numero - float(segundo_numero))

   if matematica == 'multiplicao':
      visor.insert(0, p_numero * float(segundo_numero))

   if matematica == 'divisao':
      if segundo_numero != 0:
         visor.insert(0, p_numero / float(segundo_numero))


def click_button(numero):
   #visor.delete(0, END)
   atual = visor.get()
   visor.delete(0, END)
   visor.insert(END, str(atual) + str(numero))
   

#numeros
bt0= Button(root, text="0", command=lambda: click_button(0), font="Helvetica", width=16, height=3, bg="#FEFFFF")
bt0.place(x=0,y=396)
bt1= Button(root, text="1", command=lambda: click_button(1), font="Helvetica", width=8, height=4, bg="#FEFFFF")
bt1.place(x=0,y=310)
bt2= Button(root, text="2", command=lambda: click_button(2), font="Helvetica", width=8, height=4, bg="#FEFFFF")
bt2.place(x=80,y=310)
bt3= Button(root, text="3", command=lambda: click_button(3), font="Helvetica", width=8, height=4, bg="#FEFFFF")
bt3.place(x=160,y=310)
bt4= Button(root, text="4", command=lambda: click_button(4), font="Helvetica", width=8, height=4, bg="#FEFFFF")
bt4.place(x=0,y=226)
bt5= Button(root, text="5", command=lambda: click_button(5), font="Helvetica", width=8, height=4, bg="#FEFFFF")
bt5.place(x=80,y=226)
bt6= Button(root, text="6", command=lambda: click_button(6), font="Helvetica", width=8, height=4, bg="#FEFFFF")
bt6.place(x=160,y=226)
bt7= Button(root, text="7", command=lambda: click_button(7), font="Helvetica", width=8, height=4, bg="#FEFFFF")
bt7.place(x=0,y=142)
bt8= Button(root, text="8", command=lambda: click_button(8), font="Helvetica", width=8, height=4, bg="#FEFFFF")
bt8.place(x=80,y=142)
bt9= Button(root, text="9", command=lambda: click_button(9), font="Helvetica", width=8, height=4, bg="#FEFFFF")
bt9.place(x=160,y=142)
bt10= Button(root, text=".", command=lambda: click_button('.'), font="Helvetica", width=10, height=3, bg="#FEFFFF")
bt10.place(x=142,y=396)

#operações

bt11= Button(root, text="=", command=click_igual, font="Helvetica", width=11, height=3, bg="#f19533")
bt11.place(x=242,y=396)
bt12= Button(root, text="+",  command=click_soma, font="Helvetica", width=11, height=4, bg="#f19533")
bt12.place(x=242,y=310)
bt13= Button(root, text="-",  command=click_sub, font="Helvetica", width=11, height=4, bg="#f19533")
bt13.place(x=242,y=226)
bt14= Button(root, text="*",  command=click_mult, font="Helvetica", width=11, height=4, bg="#f19533")
bt14.place(x=242,y=142)
bt15= Button(root, text="/",  command=click_divi, font="Helvetica", width=11, height=3, bg="#f19533")
bt15.place(x=242,y=74)
bt17= Button(root, text="C",  command=deletar, font="Helvetica", width=26, height=3, bg="#f19533")
bt17.place(x=-1.8,y=74)

root.mainloop()

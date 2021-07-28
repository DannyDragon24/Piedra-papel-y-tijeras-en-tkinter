from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.geometry("500x500")
root.title("Piedra, papel, tijeras")
root.resizable(0,0)

img_paper = ImageTk.PhotoImage(Image.open("papel.jpg"))
img_rock = ImageTk.PhotoImage(Image.open("roca.png"))
img_scissor = ImageTk.PhotoImage(Image.open("tijeras.png"))
img_versus = ImageTk.PhotoImage(Image.open("versus.jpg"))
img_interrogacion = ImageTk.PhotoImage(Image.open("interrogacion.jpg"))


def resultados(opcion):
	if opcion == 1 and aleatorio == 1:
		label_resultado = Label(root,text="Empate",bg="light gray",width=40,height=2,font=("Impact",17))
		label_resultado.grid(row=4,column=0,pady=60,columnspan=4)
		boton_papel = Button(root,image=img_paper,state="disabled")
		boton_papel.grid(row=1,column=0)
		boton_roca = Button(root,image=img_rock)
		boton_roca.grid(row=2,column=0)
		boton_tijeras = Button(root,image=img_scissor)
		boton_tijeras.grid(row=3,column=0)
		boton_papel_bot = Button(root,image=img_paper)
		boton_papel_bot.grid(row=1,column=2)
	elif opcion == 1 and aleatorio == 2:
		label_resultado = Label(root,text="Ganaste",bg="light gray",width=40,height=2,font=("Impact",17))
		label_resultado.grid(row=4,column=0,pady=60,columnspan=4)
		boton_papel = Button(root,image=img_paper,state="disabled")
		boton_papel.grid(row=1,column=0)
		boton_roca = Button(root,image=img_rock)
		boton_roca.grid(row=2,column=0)
		boton_tijeras = Button(root,image=img_scissor)
		boton_tijeras.grid(row=3,column=0)
		boton_roca_bot = Button(root,image=img_rock)
		boton_roca_bot.grid(row=2,column=2)
	elif opcion == 1 and aleatorio == 3:
		label_resultado = Label(root,text="Perdiste",bg="light gray",width=40,height=2,font=("Impact",17))
		label_resultado.grid(row=4,column=0,pady=60,columnspan=4)
		boton_papel = Button(root,image=img_paper,state="disabled")
		boton_papel.grid(row=1,column=0)
		boton_roca = Button(root,image=img_rock)
		boton_roca.grid(row=2,column=0)
		boton_tijeras = Button(root,image=img_scissor)
		boton_tijeras.grid(row=3,column=0)
		boton_tijeras_bot = Button(root,image=img_scissor)
		boton_tijeras_bot.grid(row=3,column=2)
	elif opcion == 2 and aleatorio == 1:
		label_resultado = Label(root,text="Perdiste",bg="light gray",width=40,height=2,font=("Impact",17))
		label_resultado.grid(row=4,column=0,pady=60,columnspan=4)
		boton_roca = Button(root,image=img_rock,state="disabled")
		boton_roca.grid(row=2,column=0)
		boton_papel = Button(root,image=img_paper)
		boton_papel.grid(row=1,column=0)
		boton_tijeras = Button(root,image=img_scissor)
		boton_tijeras.grid(row=3,column=0)
		boton_papel_bot = Button(root,image=img_paper)
		boton_papel_bot.grid(row=1,column=2)
	elif opcion == 2 and aleatorio == 2:
		label_resultado = Label(root,text="Empate",bg="light gray",width=40,height=2,font=("Impact",17))
		label_resultado.grid(row=4,column=0,pady=60,columnspan=4)
		boton_roca = Button(root,image=img_rock,state="disabled")
		boton_roca.grid(row=2,column=0)
		boton_papel = Button(root,image=img_paper)
		boton_papel.grid(row=1,column=0)
		boton_tijeras = Button(root,image=img_scissor)
		boton_tijeras.grid(row=3,column=0)
		boton_roca_bot = Button(root,image=img_rock)
		boton_roca_bot.grid(row=2,column=2)
	elif opcion == 2 and aleatorio == 3:
		label_resultado = Label(root,text="Ganaste",bg="light gray",width=40,height=2,font=("Impact",17))
		label_resultado.grid(row=4,column=0,pady=60,columnspan=4)
		boton_roca = Button(root,image=img_rock,state="disabled")
		boton_roca.grid(row=2,column=0)
		boton_papel = Button(root,image=img_paper)
		boton_papel.grid(row=1,column=0)
		boton_tijeras = Button(root,image=img_scissor)
		boton_tijeras.grid(row=3,column=0)
		boton_tijeras_bot = Button(root,image=img_scissor)
		boton_tijeras_bot.grid(row=3,column=2)
	elif opcion == 3 and aleatorio == 1:
		label_resultado = Label(root,text="Ganaste",bg="light gray",width=40,height=2,font=("Impact",17))
		label_resultado.grid(row=4,column=0,pady=60,columnspan=4)
		boton_tijeras = Button(root,image=img_scissor,state="disabled")
		boton_tijeras.grid(row=3,column=0)
		boton_papel = Button(root,image=img_paper)
		boton_papel.grid(row=1,column=0)
		boton_roca = Button(root,image=img_rock)
		boton_roca.grid(row=2,column=0)
		boton_papel_bot = Button(root,image=img_paper)
		boton_papel_bot.grid(row=1,column=2)
	elif opcion == 3 and aleatorio == 2:
		label_resultado = Label(root,text="Perdiste",bg="light gray",width=40,height=2,font=("Impact",17))
		label_resultado.grid(row=4,column=0,pady=60,columnspan=4)
		boton_tijeras = Button(root,image=img_scissor,state="disabled")
		boton_tijeras.grid(row=3,column=0)
		boton_papel = Button(root,image=img_paper)
		boton_papel.grid(row=1,column=0)
		boton_roca = Button(root,image=img_rock)
		boton_roca.grid(row=2,column=0)
		boton_roca_bot = Button(root,image=img_rock)
		boton_roca_bot.grid(row=2,column=2)
	elif opcion == 3 and aleatorio == 3:
		label_resultado = Label(root,text="Empate",bg="light gray",width=40,height=2,font=("Impact",17))
		label_resultado.grid(row=4,column=0,pady=60,columnspan=4)
		boton_tijeras = Button(root,image=img_scissor,state="disabled")
		boton_tijeras.grid(row=3,column=0)
		boton_roca = Button(root,image=img_rock)
		boton_roca.grid(row=2,column=0)
		boton_roca_bot = Button(root,image=img_rock)
		boton_roca_bot = Button(root,image=img_rock)
		boton_papel = Button(root,image=img_paper)
		boton_papel.grid(row=1,column=0)
		boton_tijeras_bot = Button(root,image=img_scissor)
		boton_tijeras_bot.grid(row=3,column=2)
		
def juego():
	global boton_papel_bot
	global boton_roca_bot
	global boton_tijeras_bot
	global boton_papel
	global boton_roca
	global boton_tijeras
	global aleatorio
	aleatorio = randint(1,3)
	root.geometry("530x550")
	barramenu = Menu(root)
	root.config(menu=barramenu)
	opcionesmenu = Menu(barramenu,tearoff=0)
	opcionesmenu.add_command(label="Intentar de nuevo",command=juego)
	opcionesmenu.add_separator()
	opcionesmenu.add_command(label="Salir",command=root.destroy)
	barramenu.add_cascade(label="OPCIONES",menu=opcionesmenu)
	
	label_titulo.grid_forget()
	boton_comenzar.grid_forget()
	label_jugador = Label(root,text="Jugador:",font=("Arial",17))
	label_jugador.grid(row=0,column=0,pady=30,padx=70)
	#--------------BOTONES_JUGADOR--------------------------------------
	boton_papel = Button(root,image=img_paper,command=lambda:resultados(1))
	boton_papel.grid(row=1,column=0)
	boton_roca = Button(root,image=img_rock,command=lambda:resultados(2))
	boton_roca.grid(row=2,column=0)
	boton_tijeras = Button(root,image=img_scissor,command=lambda:resultados(3))
	boton_tijeras.grid(row=3,column=0)
	label_versus = Label(root,image=img_versus)
	label_versus.grid(row=2,column=1)
	label_bot = Label(root,text="Bot:",font=("Arial",17))
	label_bot.grid(row=0,column=2,pady=30,padx=70)
	#--------------BOTONES-BOT------------------------------------------
	boton_papel_bot = Button(root,image=img_interrogacion)
	boton_papel_bot.grid(row=1,column=2)
	boton_roca_bot = Button(root,image=img_interrogacion)
	boton_roca_bot.grid(row=2,column=2)
	boton_tijeras_bot = Button(root,image=img_interrogacion)
	boton_tijeras_bot.grid(row=3,column=2)
	label_resultado = Label(root,bg="light gray",width=40,height=2)
	label_resultado.grid(row=4,column=0,pady=60,columnspan=4)
	
	
def pantalla_inicio():
	global label_titulo
	global boton_comenzar
	label_titulo = Label(root,text="PIEDRA , PAPEL Y TIJERAS",font=("Comic Sans MS",19))
	label_titulo.grid(row=0,column=0,padx=80,pady=140)
	boton_comenzar = Button(root,text="Comenzar",width=15,height=3,font=("Lucida Console",16),command=juego)
	boton_comenzar.grid(row=1,column=0)

pantalla_inicio()


root.mainloop()

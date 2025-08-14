
from tkinter import*
import random
from tkinter import messagebox

# cuando el usuario elige piedra 
def piedra_usuario():
    messagebox.showinfo("el usuario eligio PIEDRA")
    # opcion de la maquina
    maq = random.randint(1,3)
    if maq == 1: 
        resultado = "empate, la computadora escogio piedra"
    elif maq == 2:
        resultado = "perdiste, la computadora escogio papel"
    else:
        resultado = "ganaste, la computadora escogio tijera"
    t_resultados.insert(INSERT, resultado + "\n")
# cuando el usuario elige papel
def papel_usuario():
    messagebox.showinfo("el usuario eligio PAPEL")
    # opcion de la maquina
    maq = random.randint(1,3)
    if maq == 1: 
        resultado = "ganaste, la computadora escogio piedra"
    elif maq == 2:
        resultado = "empate, la computadora escogio papel"
    else:
        resultado = "perdiste, la computadora escogio tijera"
    t_resultados.insert(INSERT, resultado + "\n")

# cuando el usuario elige tijera
def tijera_usuario():
    messagebox.showinfo("el usuario eligio TIJERA")
    # opcion de la maquina
    maq = random.randint(1,3)
    if maq == 1: 
        resultado = "perdiste, la computadora escogio piedra"
    elif maq == 2:
        resultado = "ganaste, la computadora escogio papel"
    else:
        resultado = "empate, la computadora escogio tijera"
    t_resultados.insert(INSERT, resultado + "\n")

ventana = Tk()
ventana.title("piedra papel o tijeras")
ventana.geometry("800x500")
ventana.resizable(0,0)
ventana.config(bg="white")

frame_1= Frame(ventana)
frame_1.config(bg="ivory2", width=780,height=240)
frame_1.place(x=10,y=10)

# imagen logo de la app
logo = PhotoImage(file="img/logo.png")
Label_logo=Label(frame_1,image=logo)
Label_logo.place(x=10,y=10)
# etiqueta para el titulode la app
titulo = Label(frame_1,text=" Colegio San José de Guanenta")
titulo.config(bg="yellow", fg="blue",font=("arial",16))
titulo.place(x=390,y=10)
# Etiqueta para sunbtitulo 1 de la app
subtitulo1 = Label(frame_1,text="  Especialidad en sistemas")
subtitulo1.config(bg="yellow",fg="blue",font=("arial",12))
subtitulo1.place(x=390,y=40)
#Etiqueta subtitulo2
subtitulo2 = Label(frame_1,text="PIDRA PAPEL O TIJERAS")
subtitulo2.config(bg="ivory2",fg="blue",font=("arial",15),anchor=CENTER)
subtitulo2.place(x=390,y=70)

#_-------------------------
# frame 2 - panel de operaciones
#--------------------------
frame_2= Frame(ventana)
frame_2.config(bg="ivory2", width=780,height=120)
frame_2.place(x=10,y=260)
img_bt_piedra = PhotoImage(file="img/piedra.png")
bt_piedra = Button(frame_2, image = img_bt_piedra, width = 105, height = 105, command=piedra_usuario)
bt_piedra.place(x =166, y = 7)
img_bt_papel = PhotoImage(file="img/papel.png")
bt_papel = Button(frame_2, image = img_bt_papel, width = 105, height = 105, command=papel_usuario)
bt_papel.place(x =337, y = 7)
img_bt_tijeras = PhotoImage(file="img/tijeras.png")
bt_papel = Button(frame_2, image = img_bt_tijeras, width = 105, height = 105, command=tijera_usuario)
bt_papel.place(x = 558, y = 7)


#--------------------------
# frame 3 -Resultado
#--------------------------
frame_3= Frame(ventana)
frame_3.config(bg="ivory2", width=780,height=100)
frame_3.place(x=10,y= 390)
# area de texto
t_resultados = Text(frame_3, width=50, height=3)
t_resultados.config(bg="green", fg="white", font=("Courier", 20))
t_resultados.pack()
#Metodo principal quedespiega la ventana en pantalla
ventana.mainloop()

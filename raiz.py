from tkinter import *
from tkinter import messagebox




#---------------------
# Ventana Principal
#---------------------

#Se declara una variable que llamamos ventana_principal y que adquiere las caracteristicas de un objeto Tk
ventana_principal=Tk()

#Titulo de la ventana
ventana_principal.title("David Mayorga")

#Establecer tamaño a la pantalla
ventana_principal.geometry("800x500")

#Icono de la ventana principal

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#Color de fondo de la ventana principal
ventana_principal.config(bg="snow")

#---------------------
# Funciones de la App
#---------------------

def sumar ():
    z=pow(int(n.get()),1/int(x.get()))
    t_resultado.insert(INSERT, "Resultados:\n La raiz del número "+n.get()+" es "+str(z)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    x.set("")
    n.set("")
    t_resultado.delete("1.0", "end")

def salir():
    messagebox.showinfo("Suma 1.0", "La App se cerrará...")
    ventana_principal.destroy()


#---------------------
# Variables Globales
#---------------------  
x=StringVar()
n=StringVar()
z=IntVar()

#---------------------
# Frame Entrada
#---------------------
frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="ivory2", width=800, height=800)
frame_entrada.place(x=10,y=10)

#Etiqueta para el titulo de la app
titulo = Label(frame_entrada, text= "Ejercicio 2")
titulo.config(bg="slategray2", fg="black" , font=("Arial", 20))
titulo.place(x=130, y=10)

#Etiqueta para el subtitulo de la app
subtitulo = Label(frame_entrada,  text='Especialidad en Sistemas')
subtitulo.config(bg="blue", fg="black" , font=("Arial", 13))
subtitulo.place(x=130, y=50)

#Etiqueta para subtitulo2 de la app
subtitulo2 = Label(frame_entrada,  text="Calculador de raiz")
subtitulo2.config(bg="slategray2", fg="black" , font=("Arial", 15))
subtitulo2.place(x=130, y=80)

logo= PhotoImage(file="img_raiz/Logo.png")
etiq_logo=Label(frame_entrada, image=logo)
etiq_logo.config(bg="ivory2")
etiq_logo.place(x=10,y=10)

logo1= PhotoImage(file="")
etiq_logo1=Label(frame_entrada, image=logo1)
etiq_logo1.config(bg="ivory2")
etiq_logo1.place(x=600,y=50)

etiq_a=Label(frame_entrada, text="Valor de x: = ")
etiq_a.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_a.place(x=130, y=130)

entry_a=Entry(frame_entrada, width=7, textvariable=x)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=250,y=125)

etiq_b=Label(frame_entrada, text="Valor de N = ")
etiq_b.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_b.place(x=130, y=200)

entry_b=Entry(frame_entrada, width=7, textvariable=n)
entry_b.config(font=("Arial", 20), justify=CENTER)
entry_b.focus_set()
entry_b.place(x=250,y=195)


#---------------------
# Frame Operaciones
#---------------------

frame_operaciones=Frame(frame_entrada)
frame_operaciones.config(bg="yellow2", width=200, height=60)
frame_operaciones.place(x=500,y=80)

frame_operaciones=Frame(frame_entrada)
frame_operaciones.config(bg="blue", width=200, height=60)
frame_operaciones.place(x=500,y=120)

frame_operaciones=Frame(frame_entrada)
frame_operaciones.config(bg="red", width=200, height=40)
frame_operaciones.place(x=500,y=160)



bt_sum= PhotoImage(file="img_raiz/raiz.png")
bt_sumar= Button(frame_entrada, image=bt_sum, width=105, height=105, command=sumar)
bt_sumar.place(x=116, y=250)


bt_bor= PhotoImage(file="img_raiz/borrar.png")
bt_borrar= Button(frame_entrada, image=bt_bor, width=105, height=105, command=borrar)
bt_borrar.place(x=337, y=250)


bt_sal= PhotoImage(file="img_raiz/salida.png")
bt_salir= Button(frame_entrada, image=bt_sal, width=105, height=105, command=salir)
bt_salir.place(x=585, y=250)


#---------------------
# Frame Resultados
#---------------------

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="", width=780, height=100)
frame_resultados.place(x=10,y=390)

t_resultado=Text(frame_resultados, width=77, height=5)
t_resultado.config(bg="white", fg="white", font=("Courier", 12))
t_resultado.pack(expand=True)


ventana_principal.mainloop()
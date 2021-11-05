from tkinter import *
from tkinter import messagebox
import os
from tkinter import scrolledtext
def botonabrir():
    ru=ubicacion.get()
    ruta=os.path.isfile(ru)
    if ruta:
        print("el archivo existe")
        messagebox.showinfo('Hecho!','Archivo abierto con éxito')

    else:
        print("el archivo no existe")
        messagebox.showerror('Error','El archivo no existe')

def botoncontenido():
    tarea.deiconify()
    ventan2=Toplevel()
    ventan2.title("CONTENIDO")
    ventan2.config(bg="purple")
    ventan2.geometry("700x600")
    ru=ubicacion.get()
    ruta=os.path.isfile(ru)
    archivo=open(ru,'r+')
    linea=archivo.readline()
    while len(linea)>0:
        print(linea, end='')
        textoarchivo=scrolledtext.ScrolledText(ventan2)
        textoarchivo = Text(ventan2,width=80,height=0) 
        textoarchivo.insert(0.0,linea)
        textoarchivo.focus()
        textoarchivo.pack()
        linea=archivo.readline()
    archivo.close()
    cerrarventana2=Button(ventan2, text="Cerrar",command=ventan2.destroy,bg="Pink")
    cerrarventana2.grid(row=0, column=0, padx=15, pady=15)

def botondatos():
    tarea.deiconify()
    ventanaa2=Toplevel()
    ventanaa2.title("DATOS PERSONALES")
    ventanaa2.config(bg="purple")
    nombree=Label(ventanaa2,text="NOMBRE: Andrea Desiré Cruz Castillo ")
    nombree.grid(row=0,column=0,padx=0,pady=0)

    fecha=Label(ventanaa2,text="FECHA DE NACIMIENTO: 11 de Mayo de 2003 ")
    fecha.grid(row=1,column=0,padx=0,pady=0)

    carrera=Label(ventanaa2,text="CARRERA: Ingenieria en Sistamas ")
    carrera.grid(row=2,column=0,padx=0,pady=0)
    
    seccion=Label(ventanaa2,text="SECCION: A ")
    seccion.grid(row=3,column=0,padx=0,pady=0)
    
    carne=Label(ventanaa2,text="CARNÉ: 7690-21-8692")
    carne.grid(row=4,column=0,padx=0,pady=0)

    cerrarventana2=Button(ventanaa2, text="Cerrar",command=ventanaa2.destroy,bg="Pink")
    cerrarventana2.grid(row=5, column=3, padx=15, pady=15)

def botonsalir():
        tarea.destroy()

tarea=Tk()
tarea.config(bg="purple", )
tarea.title("ARCHIVOS")
tarea.geometry("300x150")

ventana=Frame(tarea, width=100, height=100)
ventana.pack()

ubicacion=Entry(ventana)
ubicacion.grid(row=0,column=1,padx=10,pady=10)

texto=Label(ventana,text="Archivo")
texto.grid(row=0,column=0,padx=10,pady=10)


datoss=Button(ventana, text="Abrir",bg='Pink',command=botonabrir)
datoss.grid(row=0, column=2, padx=10, pady=10)

textto=Label(ventana,text=" Contenido")
textto.grid(row=1,column=0,padx=10,pady=10)

contenido=Button(ventana,text="Mostrar Contenido",bg='Pink',command=botoncontenido)
contenido.grid(row=1, column=1, padx=10, pady=10)


datos=Button(ventana, text="Datos",bg='Pink',command=botondatos)
datos.grid(row=3,column=1,padx=10,pady=10)

datos2=Button(ventana, text="Modificar",bg='Pink')
datos2.grid(row=3,column=0,padx=10,pady=10)

datos3=Button(ventana, text="Salir",bg='Pink',command=botonsalir)
datos3.grid(row=3, column=2, padx=10, pady=10)

tarea.mainloop()
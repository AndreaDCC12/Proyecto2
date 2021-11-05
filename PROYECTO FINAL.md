# PROYECTO FINAL
## _Aplicación Lectura de Archivo_
Para el desarrollo del programa con interfaz gráfica, se hizo uso se Tkinter.
Para ello se utilizó lo siguiente:
1. Modulos para el desarollo de la aplicación
```sh
from tkinter import *
from tkinter import messagebox
import os
from tkinter import scrolledtext
```

2. Creación de la ventana principal de la interfaz grafica:
```sh
tarea=Tk()
tarea.config(bg="purple", )
tarea.title("ARCHIVOS")
tarea.geometry("300x150")
```
3. Creación del texto, cajas de texto en las que el usuario puede ingresar datos y botones. Se asigna un tamaño y color a los botones.

```sh
ventana=Frame(tarea, width=100, height=100)
ventana.pack()
ubicacion=Entry(ventana)
ubicacion.grid(row=0,column=1,padx=10,pady=10)
texto=Label(ventana,text="Archivo")
texto.grid(row=0,column=0,padx=10,pady=10)
datoss=Button(ventana, text="Abrir",bg='Pink',command=botonabrir)
datoss.grid(row=0, column=2, padx=10, pady=10)
```
4. Se utilizaron una serie de funciones, las cuales hacen que el programa cumpla con su objetivo.
```
botonabrir() - "Abrir" 
botondatos() - "Datos" 
botoncontenido() - "mostrar contenido" 
botonsalir() - "salir" 
```
5. Al empezar a ejecutar el programa, aparecerá una ventana en la que se mostrarán las siguientes opciones: 


Se permitirá buscar el archivo por ruta en el espacio en blanco, al seleccionar "Abrir" el archivo podrá verse presionando el botón "Mostrar Contenido", si el archivo no existe aparecerá un mensaje de error, por el contrario aparecerá un mensaje de "Archivo abierto con éxito".
En el botón datos, se muestran los datos personales del alumno.
"salir" es el botón utilizado para cerrar la ventana principal del programa.






#Librerías
import tkinter as tk
from tkinter import *
from tkinter import ttk
import download_zip_py
import extract_files_py
import unifying_files_py
import insert_files_py

#Función para mostrar la ventana de descargar ficheros
def mostrar_download_zip():
    principal.pack_forget()
    download_zip_py.pack(side="top", fill="both", expand=True)

#Función para mostrar la ventana de extraer ficheros
def mostrar_extract_files():
    principal.pack_forget()
    extract_files_py.pack(side="top", fill="both", expand=True)
    
#Función para mostrar la ventana de unificar ficheros
def mostrar_unifying_files():
    principal.pack_forget()
    unifying_files_py.pack(side="top", fill="both", expand=True)

#Función para mostrar la ventana de insertar ficheros en base de datos
def mostrar_insert_files():
    principal.pack_forget()
    insert_files_py.pack(side="top", fill="both", expand=True)    

#Función para mostrar la ventana principal
def mostrar_principal():
    download_zip_py.pack_forget()
    extract_files_py.pack_forget()
    unifying_files_py.pack_forget()
    insert_files_py.pack_forget()
    principal.pack(side="top", fill="both", expand=True)


root = tk.Tk()

#Style
background_blue = "#e1f5fe"
background_white=  'white'
font_bold_label_title = 'Helvetica 14 bold'
font_bold_label_description = 'Helvetica 11 bold'

#Título de la ventana al abrirse
root.title("GESTIÓN DE CITIBIKE")
root.config(width=800, height=800)
root.maxsize(width=800, height=800)
root.minsize(width=800, height=800)
root.wm_attributes("-alpha", 0.97)

#Creamos el frame de la ventana principal
principal = tk.Frame(root)
principal.configure(background=background_blue)

#Etiqueta Label Header
label_header = Label(principal,width=100, height=6,background=background_white)
label_header.place(x=0, y=0)
label_header.config(width=200)

#Etiqueta título
label_title = ttk.Label(principal,text="GESTIÓN DE FICHEROS",background=background_white,font=font_bold_label_title)
label_title.place(x=280, y=40)

#Imagen título
img_utad_lbl = tk.PhotoImage(file='./images/u-tadlogo.png')
img_utad = img_utad_lbl.zoom(25) 
img_utad = img_utad_lbl.subsample(3) 
label_img_title = ttk.Label(principal,image = img_utad,background=background_white,font=font_bold_label_title)
label_img_title.place(x=600, y=0)

#Etiqueta Label Footer
label_footer = Label(principal,width=100, height=6,background=background_white)
label_footer.place(x=0, y=700)
label_footer.config(width=200)

#Etiqueta Título Footer
label_title_footer = ttk.Label(principal,text="© Alvaro Grisolía Vaquero Co. 2022",background=background_white,font=font_bold_label_title)
label_title_footer.place(x=230, y=750)

#Etiqueta de descargar ficheros
label_description_download_zip = ttk.Label(principal,text="Descargar archivos",background=background_blue,font=font_bold_label_description)
label_description_download_zip.place(x=150, y=300)

#Boton de descargar ficheros
img_btn = tk.PhotoImage(file='./images/download_btn_white.png')
img = img_btn.zoom(25) 
img = img_btn.subsample(4) 
boton = tk.Button(principal, image = img, command=mostrar_download_zip,background='#d7ebf2',borderwidth=0.4)
boton.place(x=155, y=150)

#Etiqueta de extraer ficheros
label_description_extract_files = ttk.Label(principal,text="Extraer ficheros",background=background_blue,font=font_bold_label_description)
label_description_extract_files.place(x=470, y=300)

#Botón de extraer ficheros
img_extract_btn = tk.PhotoImage(file='./images/zip_btn.png')
img_extract = img_extract_btn.zoom(25) 
img_extract = img_extract_btn.subsample(4) 
boton_2 = tk.Button(principal, image = img_extract, command=mostrar_extract_files,background='#d7ebf2',borderwidth=0.4)
boton_2.place(x=470, y=150)

#Etiqueta de unificar ficheros
label_description_unifying_files = ttk.Label(principal,text="Unificar ficheros",background=background_blue,font=font_bold_label_description)
label_description_unifying_files.place(x=160, y=600)
#Botón unificar archivos
img_unifying_btn = tk.PhotoImage(file='./images/excel_btn.png')
img_unifying = img_unifying_btn.zoom(25) 
img_unifying = img_unifying_btn.subsample(4) 
boton_3 = tk.Button(principal, image=img_unifying, command=mostrar_unifying_files,background='#d7ebf2',borderwidth=0.4)
boton_3.place(x=155, y=450)

#Etiqueta de insertar ficheros en la base de datos
label_description_insert_files = ttk.Label(principal,text="Ingesta de datos",background=background_blue,font=font_bold_label_description)
label_description_insert_files.place(x=470, y=600)

#Botón ingestar ficheros
img_insert_btn = tk.PhotoImage(file='./images/ingestar_btn.png')
img_insert = img_insert_btn.zoom(25) 
img_insert = img_insert_btn.subsample(4) 
boton_4 = tk.Button(principal, image=img_insert, command=mostrar_insert_files,background='#d7ebf2',borderwidth=0.4)
boton_4.place(x=470, y=450)

#Botón salir del programa
img_exit_btn = tk.PhotoImage(file='./images/exit_icon_btn.png')
img_exit = img_exit_btn.zoom(25) 
img_exit = img_exit_btn.subsample(9) 
boton_5 = tk.Button(principal,text='Salir', image=img_exit, command=root.destroy,background='white',borderwidth=0.4, compound='top')
boton_5.place(x=25, y=10)

#Llamada a las distintas ventanas
download_zip_py = download_zip_py.ventana_download_zip(root, mostrar_principal)
extract_files_py = extract_files_py.ventana_extract_files(root,mostrar_principal)
unifying_files_py = unifying_files_py.ventana_unifying_files(root,mostrar_principal)
insert_files_py = insert_files_py.ventana_insert_files(root,mostrar_principal)

#Función que se ejecuta primero al iniciar el programa
mostrar_principal()

root.mainloop()
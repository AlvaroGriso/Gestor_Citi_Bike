import functools
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os, zipfile
import pandas as pd
import glob
import os



def ventana_unifying_files(master, callback=None, args=(), kwargs={}):
    def unifying_files():
        file_name = 'citibike_final.csv'

        files = os.path.join("C:\\Users\Alvaro\Desktop\TFM\programa", "20*.csv")
        files = glob.glob(files)

        print("Creando el archivo final (UNIFICADO)");

        df = pd.concat(map(pd.read_csv, files), ignore_index=True)
        print(df)

        df.to_csv(file_name, sep='\t')
        lbl_pr = Label(main_frame, text="Fichero unificado correctamente",font=font_bold_label_description,background=background_blue)
        lbl_pr.place(x=280, y=385)
        lbl_pr_2 = Label(main_frame, text="citibike_final.csv",font=font_bold_label_description,background=font_background_green)
        lbl_pr_2.place(x=200, y=250)
        

    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    #Style
    background_blue = "#e1f5fe"
    background_white=  'white'
    font_background_green = "#76ba5e"
    font_bold_label_title = 'Helvetica 14 bold'
    font_bold_label_description = 'Helvetica 11 bold'    
    font_cursive_label_table= 'Helvetica 9 normal' 

    main_frame = tk.Frame(master)
    main_frame.configure(background=background_blue)

    #Etiqueta Label Header
    label_header = Label(main_frame,width=100, height=6,background=background_white)
    label_header.place(x=0, y=0)
    label_header.config(width=200)

    #Etiqueta título
    label_title = ttk.Label(main_frame,text="Unificación de ficheros CSV",background=background_white,font=font_bold_label_title)
    label_title.place(x=265, y=40)

    #Etiqueta de descripción de las columnas - layout:
    lbl_title_box_zip = ttk.Label(main_frame,text="Los ficheros CSV serán unificados con el siguiente layout de columnas: ",background=background_blue,font=font_bold_label_description)
    lbl_title_box_zip.place(x=100, y=145)

    #Etiqueta que muestra información sobre las columnas del dataset
    label_table_download = ttk.Label(main_frame,text="'tripduration','starttime','stoptime','start station id','start station name','start station latitude','start station longitude'\n,'end station id','end station name','end station latitude','end station longitude','bikeid','usertype','birth year','gender'",background=background_white,font=font_cursive_label_table,borderwidth=2, relief="solid")
    label_table_download.place(x=100, y=185)

    #Etiqueta de nombre final del fichero final
    lbl_title_box_zip = ttk.Label(main_frame,text="Fichero final: ",background=background_blue,font=font_bold_label_description)
    lbl_title_box_zip.place(x=100, y=250)

    #Etiqueta Label body
    label_body = Label(main_frame,width=100, height=6,background=background_white)
    label_body.place(x=0, y=350)
    label_body.config(width=200)

    #Botón para unificar los ficheros CSV
    boton_unifying = tk.Button(main_frame, text="Iniciar unificación", command=unifying_files,background='#d7ebf2',font=font_bold_label_description)
    boton_unifying.place(x=250, y=540)
    
    #Botón para volver a la ventana principal
    boton_volver = tk.Button(main_frame, text="Volver al menú principal", command=callback,background='#d7ebf2',font=font_bold_label_description)
    boton_volver.place(x=420, y=540)

    #Etiqueta Label Footer
    label_footer = Label(main_frame,width=100, height=6,background=background_white)
    label_footer.place(x=0, y=700)
    label_footer.config(width=200)

    #Etiqueta Título Footer
    label_title_footer = ttk.Label(main_frame,text="© Alvaro Grisolía Vaquero Co. 2022",background=background_white,font=font_bold_label_title)
    label_title_footer.place(x=230, y=750)

    return main_frame


    
import functools
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os, zipfile
import pandas as pd
import glob
import os
import csv
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, types

def ventana_insert_files(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    def insert_files():
        #Crear la conexión con la base de datos
        engine = create_engine('mysql://root:''@localhost/tfm') # enter your password and database names here

        #Leer el csv final
        df = pd.read_csv("citibike_final.csv",sep='\t',quotechar='\'',encoding='utf8')

        #Limpiar la columna vacía que se crea por defecto en el dataset
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        #Insertar en la tabla
        df.to_sql('citibike',con=engine,index=False,if_exists='append')
        lbl_pr = Label(main_frame, text="Fichero insertado en base de datos",font=font_bold_label_description,background=background_blue)
        lbl_pr.place(x=280, y=385)   

    def connect_bbdd():
        lbl_pr = Label(main_frame, text="Conexión realizada",font=font_bold_label_description,background=background_blue,fg="#76ba5e")
        lbl_pr.place(x=590, y=190)       

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
    label_title = ttk.Label(main_frame,text="Ingesta de datos en BBDD",background=background_white,font=font_bold_label_title)
    label_title.place(x=265, y=40)

    #Etiqueta de descripción de la conexión:
    lbl_title_connection = ttk.Label(main_frame,text="Conexión a la base de datos: ",background=background_blue,font=font_bold_label_description)
    lbl_title_connection.place(x=20, y=120)

    #Etiqueta del esquema:
    lbl_title_connection = ttk.Label(main_frame,text="Conectarse al esquema: ",background=background_blue,font=font_bold_label_description)
    lbl_title_connection.place(x=20, y=170)

    #Caja donde escribir el esquema de la conexión:
    input_schema_connection = ttk.Entry(main_frame)
    input_schema_connection.place(x=250, y=170, width=150)

    #Etiqueta de la tabla:
    lbl_title_connection = ttk.Label(main_frame,text="Conectarse a la tabla: ",background=background_blue,font=font_bold_label_description)
    lbl_title_connection.place(x=20, y=220)

    #Caja donde escribir la tabla de la conexión:
    input_table_connection = ttk.Entry(main_frame)
    input_table_connection.place(x=250, y=220, width=150)

    #Etiqueta Label body
    label_body = Label(main_frame,width=100, height=6,background=background_white)
    label_body.place(x=0, y=350)
    label_body.config(width=200)

    #Botón para conectarse a la base de datos
    boton_connect = tk.Button(main_frame, text="Conectar", command=connect_bbdd,background='#d7ebf2',font=font_bold_label_description)
    boton_connect.place(x=470, y=190)

    #Botón para insertar los datos en base de datos
    boton_insert = tk.Button(main_frame, text="Iniciar ingesta", command=insert_files,background='#d7ebf2',font=font_bold_label_description)
    boton_insert.place(x=250, y=540)

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
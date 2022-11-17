import functools
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tabnanny import check
import os, zipfile



def ventana_extract_files(master, callback=None, args=(), kwargs={}):
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

    def extract_files():
        dir_name = 'C:\\Users\Alvaro\Desktop\TFM\programa'

        os.chdir(dir_name) 

        for item in os.listdir(dir_name): 
            if item.endswith('.zip'): 
                file_name = os.path.abspath(item) 
                zip_ref = zipfile.ZipFile(file_name) 
                zip_ref.extractall(dir_name) 
                zip_ref.close() 
                lbl_pr = Label(main_frame, text="Ficheros extraídos correctamente",font=font_bold_label_description,background=background_blue)
                lbl_pr.place(x=280, y=385)
                
    #Etiqueta Label Header
    label_header = Label(main_frame,width=100, height=6,background=background_white)
    label_header.place(x=0, y=0)
    label_header.config(width=200)

    #Etiqueta título
    label_title = ttk.Label(main_frame,text="Extraer CSV desde archivos ZIP",background=background_white,font=font_bold_label_title)
    label_title.place(x=250, y=40)

    #Etiqueta de descripción de extraer ficheros
    lbl_title_2_box_zip = ttk.Label(main_frame,text="Se han encontrado un total de ",background=background_blue,font=font_bold_label_description)
    lbl_title_2_box_zip.place(x=52, y=170)

    #Etiqueta de descripción 2 de extraer ficheros
    lbl_title_3_box_zip = tk.Label(main_frame,text=" 6 ",background=background_blue,fg=font_background_green,font=font_bold_label_description)
    lbl_title_3_box_zip.place(x=268, y=170)

    #Etiqueta de descripción 3 de extraer ficheros
    lbl_title_3_box_zip = ttk.Label(main_frame,text="archivos ZIP ",background=background_blue,font=font_bold_label_description)
    lbl_title_3_box_zip.place(x=290, y=170)

    #Etiqueta de descripción 4 de extraer ficheros
    lbl_title_box_zip = ttk.Label(main_frame,text="Ficheros ZIP encontrados: ",background=background_blue,font=font_bold_label_description)
    lbl_title_box_zip.place(x=50, y=220)

    #Etiqueta de extraer ficheros
    lbl_box_zip = ttk.Label(main_frame,text="year_month-citibike-tripdata.zip\nyear_month-citibike-tripdata.csv.zip\nyear_month-citibike-tripdata.csv.zip\nyear_month-citibike-tripdata.zip\nyear_month-citibike-tripdata.zip\nyear_month-citibike-tripdata.zip",background=background_white,font=font_cursive_label_table)
    lbl_box_zip.place(x=280, y=220)
    lbl_box_zip.config(width=65)

    #Etiqueta Label body
    label_body = Label(main_frame,width=100, height=6,background=background_white)
    label_body.place(x=0, y=350)
    label_body.config(width=200)

    #Botón para extraer los ficheros CSV de los ZIP
    btn_extract = tk.Button(main_frame, text="Iniciar extracción", command=extract_files,background='#d7ebf2',font=font_bold_label_description)
    btn_extract.place(x=250, y=540)

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
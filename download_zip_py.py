#Librerías
import functools
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tabnanny import check
import requests
import urllib
import shutil
import requests


def ventana_download_zip(master, callback=None, args=(), kwargs={}):

    #Función para descargar los archivos encontrados
    def download_zip_files(url,file_name):


        output_file = file_name
        with urllib.request.urlopen(url) as response, open(output_file, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

    #Función para detectar si la url introducida existe
    def check_if_url_exists(url,file_name):

        print(url)

        response = requests.get(url)

        if response.status_code == 200:
            print('El sitio al que intenta acceder, SI EXISTE')
            download_zip_files(url,file_name)
        else:
            print('Error: ', response.status_code) 

    #Función principal del programa, es el 'main'    
    def main():

        llave = True
        anio = input_year_download.get()  
        mes='00'
        count = 0
        url_file_name =anio+mes

        while llave == True:

            count = count+1


            url_file_name = int(url_file_name)+1

            if int(anio) > 2016:
                url = 'https://s3.amazonaws.com/tripdata/'+str(url_file_name)+'-citibike-tripdata.csv.zip'
            else:
                url = 'https://s3.amazonaws.com/tripdata/'+str(url_file_name)+'-citibike-tripdata.zip'    


            extract_month= url[38:]
            print(extract_month)

            file_name = url.replace('https://s3.amazonaws.com/tripdata/','')

            if '13' in extract_month:
                llave = False
                print('Descarga finalizada')
                lbl_pr = Label(main_frame, text="Ficheros descargados correctamente",font=font_bold_label_description,background=background_blue)
                lbl_pr.place(x=280, y=435)
            else:    
                check_if_url_exists(url,file_name)

    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    #Style
    background_blue = "#e1f5fe"
    background_blue_title = "#5687ba"
    background_white=  'white'
    background_white_title = 'white'
    font_bold_label_title = 'Helvetica 14 bold'
    font_bold_label_description = 'Helvetica 11 bold'    
    font_bold_label_table = 'Helvetica 11'
    font_cursive_label_table= 'Helvetica 9 normal' 
    main_frame = tk.Frame(master)
    main_frame.configure(background=background_blue)

    #Etiqueta Label Header
    label_header = Label(main_frame,width=100, height=6,background=background_white)
    label_header.place(x=0, y=0)
    label_header.config(width=200)

    #Etiqueta título
    label_title = ttk.Label(main_frame,text="Descargar archivos desde la WEB",background=background_white,font=font_bold_label_title)
    label_title.place(x=250, y=40)

    #Etiqueta 1 que muestra información sobre la fuente de datos
    label_table_download = ttk.Label(main_frame,text="  NOMBRE DEL FICHERO GENÉRICO  ",background=background_blue_title,font=font_bold_label_description,borderwidth=2, relief="solid")
    label_table_download.place(x=20, y=140)
    #Etiqueta 2 que muestra información sobre la fuente de datos
    label_table_download = ttk.Label(main_frame,text="  FUENTE OFICIAL  ",background=background_blue_title,font=font_bold_label_description,borderwidth=2, relief="solid")
    label_table_download.place(x=300, y=140)
    #Etiqueta 3 que muestra información sobre la fuente de datos
    label_table_download = ttk.Label(main_frame,text="  ENLACE DE DESCARGA                                    ",background=background_blue_title,font=font_bold_label_description,borderwidth=2, relief="solid")
    label_table_download.place(x=444, y=140)
    #Etiqueta 4 que muestra información sobre la fuente de datos
    label_table_download = ttk.Label(main_frame,text="  year_month-citibike-tripdata.zip                ",background=background_white_title,font=font_bold_label_table,borderwidth=2, relief="solid")
    label_table_download.place(x=20, y=163)
    #Etiqueta 5 que muestra información sobre la fuente de datos
    label_table_download = ttk.Label(main_frame,text="  CITI BIKE                 ",background=background_white_title,font=font_bold_label_table,borderwidth=2, relief="solid")
    label_table_download.place(x=300, y=163)
    #Etiqueta 6 que muestra información sobre la fuente de datos
    label_table_download = ttk.Label(main_frame,text="  https://s3.amazonaws.com/tripdata/index.html    ",background=background_white_title,font=font_bold_label_table,borderwidth=2, relief="solid")
    label_table_download.place(x=444, y=163)
    #Etiqueta 7 que muestra información sobre la fuente de datos
    label_table_download = ttk.Label(main_frame,text="  year_month-citibike-tripdata.csv.zip         ",background=background_white_title,font=font_bold_label_table,borderwidth=2, relief="solid")
    label_table_download.place(x=20, y=185)
    #Etiqueta 8 que muestra información sobre la fuente de datos
    label_table_download = ttk.Label(main_frame,text="  CITI BIKE                 ",background=background_white_title,font=font_bold_label_table,borderwidth=2, relief="solid")
    label_table_download.place(x=299, y=185)
    #Etiqueta 9 que muestra información sobre la fuente de datos
    label_table_download = ttk.Label(main_frame,text="  https://s3.amazonaws.com/tripdata/index.html    ",background=background_white_title,font=font_bold_label_table,borderwidth=2, relief="solid")
    label_table_download.place(x=444, y=185)

    #Etiqueta oficial información citi bike que muestra información sobre la fuente de datos
    label_table_download = ttk.Label(main_frame,text="  This data is provided according to the Citi Bike Data Use Policy.    ",background=background_blue,font=font_cursive_label_table)
    label_table_download.place(x=210, y=215)

    #Etiqueta que muestra información
    label_year_download = ttk.Label(main_frame,text="Año que desea descargar :",background=background_blue,font=font_bold_label_description)
    label_year_download.place(x=20, y=297)

    #Caja donde escribir el año que deseas descargar
    input_year_download = ttk.Entry(main_frame)
    input_year_download.place(x=250, y=297, width=150)

    #Etiqueta Label body
    label_body = Label(main_frame,width=100, height=6,background=background_white)
    label_body.place(x=0, y=400)
    label_body.config(width=200)
    
    #Botón que activa la función main() con el parámetro ''command''
    btn_download = tk.Button(main_frame,text="Iniciar descarga", command=main,background='#d7ebf2',font=font_bold_label_description)
    btn_download.place(x=250, y=580)
    
    #Botón para volver a la ventana principal
    boton_volver = tk.Button(main_frame, text="Volver al menú principal", command=callback,background='#d7ebf2',font=font_bold_label_description)
    boton_volver.place(x=420, y=580)

    #Etiqueta Label Footer
    label_footer = Label(main_frame,width=100, height=6,background=background_white)
    label_footer.place(x=0, y=700)
    label_footer.config(width=200)

    #Etiqueta Título Footer
    label_title_footer = ttk.Label(main_frame,text="© Alvaro Grisolía Vaquero Co. 2022",background=background_white,font=font_bold_label_title)
    label_title_footer.place(x=230, y=750)

    return main_frame



   





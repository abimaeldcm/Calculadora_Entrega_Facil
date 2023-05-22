# BIBLIOTECAS UTILIZADAS NO PROJETO. PARA INSTALA-LAS É NECESSÁRIO EXECUTAR O COMANDO "PIP INSTALL" + O NOME DA BIBLIOTECA NO TERMINAL
import customtkinter 
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import informacoes
from random import randint

caminho = ""
def button_event():
    caminho = filedialog.askopenfilename(title="Selecione um arquivo excel", filetypes=(("Arquivos Excel", "*.xlsx"), ("Todos os arquivos", "*.*")))
    #janela.update()

    if caminho != "":
        print("deu certo")
        informacoes.janela2(caminho)
        
    
#CUSTOMIZAÇÃO DA TELA
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


#CONFIGURAÇÃO DA TELA
janela = customtkinter.CTk()
janela.geometry("900x650")
janela.title("Calculadora Entrega Fácil")
janela.iconbitmap("icone.ico")
janela.resizable(False, False)

#BOTÃO DE BUSCA
Labelbusca = customtkinter.CTkButton(master=janela, width=263, height=60, fg_color="#fb0414", text="SELECIONAR ARQUIVO", font = ('Roboto ', 18),corner_radius=20, hover_color="#a9100d", command=button_event) 
Labelbusca.place(x=330, y=325)

#AJUSTANDO A IMAGEM NA TELA
#FOTO BASE
img = PhotoImage(file="fotos/base.png")
Label_img = customtkinter.CTkLabel(master=janela, image=img, text="")
Label_img.place(x= 0, y=480)

img = PhotoImage(file="fotos/voador.png")
Label_voador = customtkinter.CTkLabel(master=janela, image=img, text="")
Label_voador.place(x= 10, y=20)

img = PhotoImage(file="fotos/DiscoVoador.png")
Label_discovoador = customtkinter.CTkLabel(master=janela, image=img, text="")
Label_discovoador.place(x= 680, y=20)

#LOGOS IFOOD QUE APARECERÃO ALEATORIAMENTE QUANDO O PROGRAMA DOR ABERTO

a = randint(0,2)
if a == 1:
    #LOGO IFOOD REDONDA
    imgifood = PhotoImage(file="fotos/ifoodRedoda.png")
    Label_img = customtkinter.CTkLabel(master=janela, image=imgifood, text="")
    Label_img.place(x= 410, y=200)

elif a == 2:
    #LOGO IFOOD SEM FUNDO
    imgifood = PhotoImage(file="fotos/semfundo.png")
    Label_img = customtkinter.CTkLabel(master=janela, image=imgifood, text="")
    Label_img.place(x= 410, y=225)

else:
    #LOGO QUADRADA
    imgifood = PhotoImage(file="fotos/ifoodQuadrada.png")
    Label_img = customtkinter.CTkLabel(master=janela, image=imgifood, text="")
    Label_img.place(x=410, y=200)



#TÍTULO 
Labeltitulo = customtkinter.CTkLabel(master=janela, text="Calculadora Entrega Fácil",  font = ('Roboto ', 30, 'bold'), text_color= ('red'),compound = "center" )
Labeltitulo.place(x=275, y=150)

#INSTUÇÃO DE BUSCA 
Labelaviso = customtkinter.CTkLabel(master=janela, text=(f"Busque o arquivo excel com os pedidos que serão analisados"),  font = ('Roboto ', 12), text_color= ('red'))
Labelaviso.place(x=275, y=400)

janela.mainloop()
import customtkinter 
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas as pd
import numpy as np


def destruir():
    janela3.destroy()

def  janelaErro():
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("dark-blue")

    global janela3
    janela3 = customtkinter.CTk()
    janela3.geometry("900x650")
    janela3.title("Calculadora Entrega Fácil")
    janela3.iconbitmap("icone.ico")
    janela3.resizable(False, False)

    # imgerro = PhotoImage(file="fotos/erro.png")
    # Label_erro = customtkinter.CTkLabel(master=janela3, image=imgerro, height=30, width=30).place(x=10, y=200)

    Labeltitulo = customtkinter.CTkLabel(master=janela3, text="Ops!! Algo saiu fora do planejado",  font = ('Roboto ', 30, 'bold'), text_color= ('red'),compound = "center" )
    Labeltitulo.place(x=275, y=80)

    Labelsubtitulo = customtkinter.CTkLabel(master=janela3, text="Abaixo você pode ver algumas soluções:",  font = ('Roboto ', 12, 'bold'), text_color= ('red'),compound = "center" )
    Labelsubtitulo.place(x=275, y=120)

    Labeltext = customtkinter.CTkLabel(master=janela3, text="1 - Verifique se o arquivo que você selecionou está correto; \n\n2 - Abra a planilha do Excel e veja se os títulos das colunas estão nesta sequência: \nID DA LOJA, LOJA, TIPO DE LANÇAMENTO, CANAL DE VENDAS,	N° PEDIDO, DATA, \nDATA CONCLUSÃO, DATA DE PAGAMENTO, TIPO DE PEDIDO, FORMAS DE PAGAMENTO, TOTAL DO \nPEDIDO VALOR DOS ITENS , TAXA DE ENTREGA, TAXA DE SERVIÇO, INCENTIVO PROMOCIONAL\nDO IFOOD, INCENTIVO PROMOCIONAL DA LOJA, PERCENTUAL COMISSÃO, VALOR COMISSÃO, \nPERCENTUAL TAXA DE TRANSAÇÃO, VALOR TAXA DE TRANSAÇÃO, PERCENTUAL, TAXA PLANO DE\nREPASSE EM 1 SEMANA, VALOR TAXA PLANO DE REPASSE EM 1 SEMANA, BASE CALCULO, \nTAXA POR ENTREGA VIA IFOOD, VALOR LIQUIDO, VALOR OCORRENCIA, MOTIVO \nOCORRÊNCIAS"
,  font = ('Roboto ', 12, 'bold'), text_color= ('red'), justify="left" )
    Labeltext.place(x=275, y=160)

    global Labelbusca
    Labelbusca = customtkinter.CTkButton(master=janela3, width=263, height=60, fg_color="#a9100d", text="SELECIONAR ARQUIVO", font = ('Roboto ', 18),corner_radius=20, hover_color="#930000", command=destruir)    
    Labelbusca.place(x=330, y=325)

    
    janela3.mainloop()
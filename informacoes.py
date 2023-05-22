import customtkinter 
from tkinter import *
from tkinter import filedialog
import pandas as pd
import numpy as np
import ErroJl
from PIL import Image
import pyperclip as pc





def janela2(caminho):
    try:
        arquivo = pd.read_excel(caminho)

        #QUANTIDADE DE PEDIDOS CANCELADOS
        ocorrenciaEF = 0
        for lancamento, MotivoOcorrencia in zip(arquivo['TIPO DE LANÇAMENTO'], arquivo['MOTIVO OCORRÊNCIAS']):
            maiusculo = str(MotivoOcorrencia).upper()
            if lancamento == "Ocorrência por pedido" and any(x in maiusculo for x in ["ENTREGA FÁCIL - DÉBITO DE FRETE PARA PEDIDO CANCELADO"]) :
                ocorrenciaEF +=1
        print(f"Quantidade de pedidos cancelados {ocorrenciaEF}")


        print()

        #VALOR DO FRETE DOS PEDIDOS CANCELADOS
        VOcorrencia = 0
        for lancamento, MotivoOcorrencia, ValorOcorrencia in zip(arquivo['TIPO DE LANÇAMENTO'], arquivo['MOTIVO OCORRÊNCIAS'], arquivo['VALOR OCORRENCIA']):
            maiusculo = str(MotivoOcorrencia).upper()
            if lancamento == "Ocorrência por pedido" and any(x in maiusculo for x in ["ENTREGA FÁCIL - DÉBITO DE FRETE PARA PEDIDO CANCELADO"]) :
                VOcorrencia += ValorOcorrencia
        lab1 = (f"Valor do frete dos pedidos cancelados R$ {VOcorrencia}")	

        print()


        #TOTAL DE PEDIDOS NO PERÍODO
        conta = 0
        for i in arquivo['ID DA LOJA']:
            if i != "":
                conta +=1
        print(f"Você fez no período {conta} Pedidos") 


        print()


        #VALOR TOTAL DOS PEDIDOS
        item = 0
        for i in arquivo["VALOR LIQUIDO"]:
            if np.isnan(i):
                continue
            if type(i) == float: 
                item += i
                # print(type(item))
            else:
                continue
            
        print (f"Totalizando R$ {item:.2f} em vendas.")

        print()


        #PEDIDOS FEITOS COM O ENTREGA FÁCIL
        ContadorEF = 0
        for i in arquivo['CANAL DE VENDAS']:
            if i == "POS":
                ContadorEF += 1
            else:
                continue
        print(f"Desses pedidos,	{ContadorEF} eram pedidos Entrega Fácil.") 
        print()



        #QUE SOMAM
        TaxaEntrega = 0
        for canal, taxa in zip(arquivo['CANAL DE VENDAS'], arquivo['TAXA POR ENTREGA VIA IFOOD']):
            if canal == "POS":
                TaxaEntrega += taxa
        print(f"Que somam  R$ {TaxaEntrega:.2f} de frete.")

        print()

        #VALOR DEVOLVIDO DOS MULTIPEDIDOS

        Multipedidos = 0
        for lancamento, MotivoOcorrencia in zip(arquivo['TIPO DE LANÇAMENTO'], arquivo['MOTIVO OCORRÊNCIAS']):
            maiusculo = str(MotivoOcorrencia).upper()
            if  any(x in maiusculo for x in ["CRÉDITO DE INCENTIVO MULTIPEDIDOS"]) :
                Multipedidos += ValorOcorrencia

        if np.isnan(Multipedidos):
            Multipedidos = 0
        print(f"Nós te devolvemos R$ {Multipedidos} para os casos de multipedidos." )


        print()


        #PEDIDOS CANCELADOS EF
        cancelamentosEF = 0
        for canal, lancamento in zip(arquivo['CANAL DE VENDAS'], arquivo['TIPO DE LANÇAMENTO']):
            if canal == "POS" and lancamento == "Cancelamento de pedido":
                cancelamentosEF += 1
        print(f"Você teve {cancelamentosEF} pedidos cancelados")


        print()

        # VALOR DOS FRETES CANCELADOS
        valorLiquido = 0
        for canal, lancamento, liquido in zip(arquivo['CANAL DE VENDAS'], arquivo['TIPO DE LANÇAMENTO'], arquivo['VALOR LIQUIDO']):
            if canal == "POS" and lancamento == "Cancelamento de pedido":
                valorLiquido += liquido
        print(f"Seus Fretes EF cancelados somam R$ {valorLiquido:.2f}.")

        print()
        #Seu custo com frete EF nesse período foi de


        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")

        janela2 = customtkinter.CTk()
        janela2.geometry("900x650")
        janela2.title("Calculadora Entrega Fácil")
        janela2.iconbitmap("icone.ico")
        # janela2.resizable(False, False)
        
        # Quantidade de pedidos cancelados		
        Label1 = customtkinter.CTkButton(master=janela2, width=350, height=60, fg_color="#a9100d", text=(f"Quantidade de pedidos cancelados: \n{ocorrenciaEF}"), font = ('Roboto ', 18),corner_radius=5, hover_color="#930000", command=l1(ocorrenciaEF))
        Label1.place(x=100, y=80)

        VOcorrenciaFlot = (f"{VOcorrencia:.2f}")
        Label2 = customtkinter.CTkButton(master=janela2, width=350, height=60, fg_color="#a9100d", text=(f"Valor do frete dos pedidos cancelados: \n R$ {VOcorrenciaFlot}"), font = ('Roboto ', 18),corner_radius=5, hover_color="#930000", command=l1(VOcorrenciaFlot))
        Label2.place(x=470, y=80)

        # Você fez no período
        Label3 = customtkinter.CTkButton(master=janela2, width=350, height=60, fg_color="#a9100d", text=(f"Você fez no período: \n {conta} Pedidos"), font = ('Roboto ', 18),corner_radius=5, hover_color="#930000")
        Label3.place(x=100, y=160)
        
        # totalizando
        Label4 = customtkinter.CTkButton(master=janela2, width=350, height=60, fg_color="#a9100d", text=(f"Totalizando: \n R$ {item:.2f} em vendas."), font = ('Roboto ', 18),corner_radius=5, hover_color="#930000")
        Label4.place(x=470, y=160)

        Label5 = customtkinter.CTkButton(master=janela2, width=350, height=60, fg_color="#a9100d", text=(f"Desses pedidos, {ContadorEF}\neram pedidos Entrega Fácil."), font = ('Roboto ', 18),corner_radius=5, hover_color="#930000")
        Label5.place(x=100, y=240)

        # Valor do frete dos pedidos cancelados			
        Label6 = customtkinter.CTkButton(master=janela2, width=350, height=60, fg_color="#a9100d", text=(f"Que somam  : \nR$ {TaxaEntrega:.2f} de frete."), font = ('Roboto ', 18),corner_radius=5, hover_color="#930000")
        Label6.place(x=470, y=240)

        Label7 = customtkinter.CTkButton(master=janela2, width=350, height=60, fg_color="#a9100d", text=(f"Nós te devolvemos : \nR$ {Multipedidos} para os casos de multipedidos."), font = ('Roboto ', 18),corner_radius=5, hover_color="#930000")
        Label7.place(x=100, y=320)

        Label8 = customtkinter.CTkButton(master=janela2, width=350, height=60, fg_color="#a9100d", text=(f"Você teve: \n {cancelamentosEF} pedidos cancelados"), font = ('Roboto ', 18),corner_radius=5, hover_color="#930000")
        Label8.place(x=470, y=320)

        Label9 = customtkinter.CTkButton(master=janela2, width=350, height=60, fg_color="#a9100d", text=(f"Seus Fretes EF cancelados somam: \n R$ {valorLiquido:.2f}."), font = ('Roboto ', 18),corner_radius=5, hover_color="#930000")
        Label9.place(x=100, y=400)

        Label10 = customtkinter.CTkButton(master=janela2, width=350, height=60, fg_color="#a9100d", text=(), font = ('Roboto ', 18),corner_radius=5, hover_color="#930000")
        Label10.place(x=470, y=400)


        #AJUSTANDO A IMAGEM NA TELA
        # img = PhotoImage(file="fotos/imagem11.png")
        # Label_img = customtkinter.CTkLabel(master=janela2, image=img, text="")
        # Label_img.place(x= 10, y=480)

        # img = PhotoImage(file="fotos/imagem11.png")
        # a = Image.open("fotos/base.png")
        # Label_img = customtkinter.CTkImage(light_image=a, size=(30, 30))
        # Label_img.place(x= 10, y=480)

        

        #FRAMES título
        Labeltitulo = customtkinter.CTkLabel(master=janela2, text="Calculadora Entrega Fácil",  font = ('Roboto ', 30, 'bold'), text_color= ('red'),compound = "center" )
        Labeltitulo.place(x=275, y=0)

        Labelaviso = customtkinter.CTkLabel(master=janela2, text=(f"Clique em cima dos botões para copiar as informações"),  font = ('Roboto ', 12), text_color= ('red') )
        Labelaviso.place(x=320, y=600)

        janela2.mainloop()
    except:
       ErroJl.janelaErro()

def l1(ocorrenciaEF):
    pc.copy(f"Valor do frete dos pedidos cancelados R$ {ocorrenciaEF}")
def l2(VOcorrenciaFlot):
    pc.copy(f"Quantidade de pedidos cancelados: \n{VOcorrenciaFlot}")
    
# def l3()
# def l4()
# def l5()
# def l6()
# def l7()
# def l8()
# def l9()
# def l10()
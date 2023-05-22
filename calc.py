import pandas as pd
import numpy as np

arquivo = pd.read_excel("pedidos.xlsx")

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
print(f"Valor do frete dos pedidos cancelados R$ {VOcorrencia}")	

print()


#TOTAL DE PEDIDOS NO PERÍODO
print(f"Você fez no período {arquivo['VALOR LIQUIDO'].count()} Pedidos") 


print()


#VALOR TOTAL DOS PEDIDOS
item = 0
for i in arquivo["TOTAL DO PEDIDO"]:
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






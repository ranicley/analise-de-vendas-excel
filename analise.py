import pandas as pd
from pyautogui import display

tabela = pd.read_excel("Vendas.xlsx")
display(tabela)

faturamento_total = tabela["Valor Final"].sum()
print(faturamento_total)

# faturamento por loja
faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
display(faturamento_por_loja)

faturamento_por_produto = tabela[["ID Loja","Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
display(faturamento_por_produto)

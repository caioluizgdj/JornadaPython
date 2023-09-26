import pyautogui
import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no link
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2) # tempo para carregar a página

# Passo 2: Fazer login
pyautogui.click(x=683, y=586)
pyautogui.write("caioluizgdj@gmail.com")
pyautogui.press("tab")
pyautogui.write("A senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

# Passo 3: Importar tabela
import pandas

tabela = pandas.read_csv("produtos.csv")
print

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=685, y=410)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter") # Envia cadastro

    pyautogui.scroll(5000) # Sobe a página até o início




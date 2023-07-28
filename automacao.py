# Passo a passo do projeto

import pyautogui
import time
import pandas as pd
pyautogui.PAUSE = 0.3

# Passo 1: entrar no servidor
# Abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
# Entrar no link
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(2)

# Passo 2: Fazer login
# Selecionar campo email
pyautogui.click(x=437, y=397)
# Digitar o email
pyautogui.write('martinsprogramador@gmail.com')
# Proximo campo e digitar senha
pyautogui.press('tab')
pyautogui.write('minhasenha')
pyautogui.press('tab')
pyautogui.press('enter')

# Passo 3: importar a base

tabela = pd.read_csv('produtos.csv')

print(tabela)

# Passo 4: cadastrar os produtos
for linha in tabela.index:
    # Clicar no campo do codigo
    pyautogui.click(x=424, y=279)
    # Pegar da tabela o valor do campo que vai preencher
    codigo = tabela.loc[linha, 'codigo']
    # Escrever o codigo
    pyautogui.write(str(codigo))
    # Ir ao proximo campo
    pyautogui.press('tab')
    # Escrever os proximos campos
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    # Clicar em enviar
    pyautogui.press('enter')
    # Scroll tudo pra cima
    pyautogui.scroll(3000)
    # Passo 5: Repetir o processo de cadatro novamente
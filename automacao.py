# Avisos: Código somente será funcional em resolução: 1366 x 768 
# e caso o navegador ja fique em tela cheia por padrão.
# Para parar a automação, basta manter o cursor do mouse no canto superior da tela
# e aguardar 2 segundos.

# Import de bibliotecas

import pyautogui 
import time
import pandas

# Passo 1: Entrar no Navegador

pyautogui.PAUSE = 0.7     # Dá um intervalo de segundos entre cada código

# Abrir o navegador

pyautogui.press("win")    # Aperta a tecla "win"
pyautogui.write("Edge")   # Digita "Edge"
pyautogui.press("enter")  # Aperta "enter"

# Passo 2: Fazer login no sistema
# Entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # Escreve o link do sistema
pyautogui.press("enter")  # Aperta "enter"

time.sleep(2.5)                              # Pausa de 2.5 segundos

pyautogui.click(x=560, y=365)                # Clica na posição indicada (email)
pyautogui.write("sistema.py@gmail.com")      # Escreve o email
pyautogui.press("tab")                       # Aperta tab para passar para a área de senha
pyautogui.write("12345678")                  # Escreve a senha
pyautogui.press("tab")                       # Clica na posição indicada (logar)
pyautogui.press("enter")                     # Aperta "enter" na aba de login

time.sleep(1)                                # Pausa de 1 segundo

# Passo 3: Importar a base de dados

tabela = pandas.read_csv("produtos.csv") # Utiliza o pandas para ler o arquivo .csv chamado "produtos.csv"

# Passo 4: Cadastrar um produto

linha = 0

for linha in tabela.index:

    pyautogui.click(x=626, y=245) # Faz clicar na primeira coluna de cadastro
    
    # (tabela.loc[linha, "codigo"]) procura na linha da tabela onde esta o "codigo" e escreve,
    # Assim sucessivamente para as outras variáveis.
    
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): # Cria uma condição para a variavel "obs"
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # Clicar no botão enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000) # Scrola 5000 pixeis para cima

# Passo 5: Repetir o processo de cadastro até acabar os produtos.
# Foi usado o "if not pandas.isna". Ele diz que se a variavel "obs" não estiver vazio é para preencher
# Se estiver vazio o python ja entende que deve pular essa etapa.
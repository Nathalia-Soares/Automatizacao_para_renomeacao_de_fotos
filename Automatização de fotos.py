# Automatização de fotos

import pyautogui
import time

pyautogui.PAUSE = 2

caminhoOrigem = (input("Digite a pasta de origem"))
quantidadeFotos = int(input("Quantas fotos existem no total?"))

# Acessando a pasta de origem

pyautogui.click(x=988, y=1054)
pyautogui.click(x=326, y=60)
pyautogui.write(caminhoOrigem)
pyautogui.press("enter")

time.sleep(3)

# Copiando as imagens da pasta

pyautogui.click(x=318, y=212)
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")

# Acessando a pasta de destino

pyautogui.click(x=1338, y=60)
pyautogui.write("F:\RC Morph\RC MORPH")
pyautogui.press("enter")

# Apagando as fotos anteriores

pyautogui.click(x=1900, y=989)
pyautogui.click(x=318, y=212)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("del")

time.sleep(15)

# Colando as fotos na pasta de destino

pyautogui.click(x=1900, y=989)
pyautogui.hotkey("ctrl", "v")
time.sleep(15)

# Selecionando a primeira foto

pyautogui.click(x=348, y=172)

# Repetição para renomear as fotos 

for nomes in range(1 , quantidadeFotos + 1):
    pyautogui.press("f2")
    if nomes < 10:
      pyautogui.write("0" + str(nomes))
    else:
      pyautogui.write(str(nomes))
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("right")




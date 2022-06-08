import pyautogui as spam
import time

limite_msg = input("Enter n de msgs: ")
msg = input("Coloque a msg: ")

i = 0

time.sleep(3)

while i<int(limite_msg):
    spam.typewrite(msg)
    spam.press("Enter")
    
    i+=1

#Para funcionar abra o terminar do próprio vs e digite python spanwhats.py
#Obs: Após digitar o n e a msg clique na caixa de texto do whats pra quem você for mandar
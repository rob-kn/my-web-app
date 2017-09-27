import pyautogui as pag

print(pag.position())

print(pag.size())

img_rect = pag.locateCenterOnScreen('imger.PNG')

pag.click(img_rect)


#Cr. JT Pentester
import pyautogui,time
import webbrowser

webbrowser.open('http://popcat.click')
time.sleep(5)
pyautogui.press('z', presses=500)

'''
ถ้าต้องการแบบวนลูป (loop)

webbrowser.open('http://popcat.click')
time.sleep(5)

while True:
    pyautogui.press('z', presses=10)
    
'''

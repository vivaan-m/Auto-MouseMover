#! python3

from typing import Counter
import pyautogui,time,random





print('Press Ctrl-C to quit.')
print('Change value according to screen and need .')

Counter = 0
dev = False
try:
    while True:
        if dev==False:
            Counter = Counter+1
            up = random.randint(-5,10)
            uptime = random.randint(1,4)
            mouseX = random.randint(230,1300)
            mouseY = random.randint(120,550)
            time.sleep(uptime)
            pyautogui.scroll(up)
            pyautogui.moveTo(x=mouseX,y=mouseY)
            pyautogui.click()
            downtime = random.randint(1,4)
            down = random.randint(-5,10)
            mouseX = random.randint(230,1300)
            mouseY = random.randint(120,550)
            time.sleep(downtime) 
            pyautogui.scroll(down) 
            pyautogui.moveTo(x=mouseX,y=mouseY)
            pyautogui.click()
            if Counter==5:
                print("changing file")
                Counter = 0
                mouseX = random.randint(59,86)
                mouseY = random.randint(106,354)
                pyautogui.moveTo(x=mouseX,y=mouseY)
                pyautogui.doubleClick()
                mouseX = random.randint(230,1300)
                mouseY = random.randint(120,550)
                pyautogui.moveTo(x=mouseX,y=mouseY)

        else:
            print(pyautogui.position())

           






except KeyboardInterrupt:
    print('\n')
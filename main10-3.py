import pyautogui
import time
import pyperclip

pyautogui.moveTo(2815,-1097,0.2)
pyautogui.click()
time.sleep(0.5)
pyperclip.copy("서울 날씨")
pyautogui.hotkey("ctrl","v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start_x = 2494
start_y = -1075

end_x = 3332
end_y = -565

pyautogui.screenshot(r'서울날씨.png',region=(start_x,start_y,end_x-start_x,end_y-start_y))

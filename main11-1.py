import pyautogui

picPosition = pyautogui.locateAllOnScreen(r'C:\python40\kakao1.png')
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateAllOnScreen(r'C:\python40\kakao3.png')
    print(picPosition)
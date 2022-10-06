import pyautogui
import os
import time
import schedule
import shutil


def scerrnshot():

    if not os.path.exists("scerrnshot"):
        os.mkdir("scerrnshot")

    pyautogui.screenshot('my_screenshot.png')

    shutil.move('my_screenshot.png', "scerrnshot")


schedule.every(10).minutes.do(scerrnshot)

with True:
    shutil.run_pending()
    time.sleep(1)


scerrnshot()

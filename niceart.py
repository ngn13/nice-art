import sys
import json
import pyautogui
import time
import platform
from os import system
import pyperclip
plt = platform.system()

def notf(msg):
    if plt=='Linux':
        command = f'''
		notify-send "Nice Art" "{msg}"
		'''
    system(command)

def newline():
    pyautogui.hotkey("enter")

store = ""

try:
    map = sys.argv[1]
    jsondata = sys.argv[2]
except:
    print("Usage: niceart.py [map] [json]")
    exit()

with open(map, "r") as f:
    map = f.read().split("\n")
    f.close()

with open(jsondata, "r") as f:
    jsondata = json.loads(f.read())
    f.close()

for i, row in enumerate(map):
    for j, column in enumerate(row):
        char = jsondata[column]
        store += char
    store += "\n"

notf("Starting in 7...")
time.sleep(7)
store = store.split("\n")
for line in store:
    pyperclip.copy(line)
    pyperclip.paste()
    pyautogui.hotkey('ctrl', 'v', interval = 0.15)
    newline()
    time.sleep(1/30)
notf("Done!")
exit()
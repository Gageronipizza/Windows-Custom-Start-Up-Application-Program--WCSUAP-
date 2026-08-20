import time
import json
import subprocess



files = []


with open("files.json", "r") as file:
    files = json.load(file)

print(f"{files}")
print(f"{files[0]}")






for i in range(len(files)):

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = 7
    subprocess.Popen([r"file[i]"], startupinfo=startupinfo)


    time.sleep(0.15)
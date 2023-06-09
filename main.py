import keyboard
import time

now = time

def on_key_press(event):
    print(event.name  + '  ' + str(now.localtime().tm_hour) + '.' + str(now.localtime().tm_min) + '.' + str(now.localtime().tm_sec))
    text = event.name  + '  ' + str(now.localtime().tm_hour) + '.' + str(now.localtime().tm_min) + '.' + str(now.localtime().tm_sec)
    with open("datasheet.txt", "a") as file:
        file.write(text)
        file.write('\n')


keyboard.on_press(on_key_press)
keyboard.wait('esc')
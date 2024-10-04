from pynput import keyboard

stringa = ""
i = 0

def on_press(key):
    global stringa, i
    
    try:
        print(f"Tasto premuto: {key.char}")
        stringa += key.char
        i += 1

    except AttributeError:
        print(f"Tasto speciale premuto: {key}")
        stringa += f"[{key}]"
        i += 1
        
    if(i % 50 == 0):
        print(stringa)
    

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
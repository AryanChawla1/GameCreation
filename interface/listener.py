from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.esc:
        return False
    try:
        k = key.char # single-char keys
    except:
        k = key.name
    if k == '1':
        print('Spawn Knight')
    if k == '2':
        print('Spawn Archer')

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
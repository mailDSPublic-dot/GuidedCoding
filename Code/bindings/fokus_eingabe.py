# Fokus auf Eingabefeld
def fokus_eingabe(eingabefeld):
    if eingabefeld.get(1.0, "end") == "Hier den Code eingeben...\n": # Wenn Hier Code eingeben... im Feld steht
        eingabefeld.delete(1.0, "end") # Lösche den Text

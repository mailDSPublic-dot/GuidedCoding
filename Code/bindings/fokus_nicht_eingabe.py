# Fokus nicht auf Eingabefeld
def fokus_nicht_eingabe(eingabefeld):
    if eingabefeld.get(1.0, "end") == "\n": # Wenn kein Code eingegeben wurd
        eingabefeld.insert(1.0, "Hier den Code eingeben...") # füge Hier Code eingeben ein

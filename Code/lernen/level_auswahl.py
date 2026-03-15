"""
Bekommt eine Zahl und gibt dann für diese Zahl einen Text zurück
"""
def level_auswahl(level):
    import ttkbootstrap as tb
    ausgabe = None
    if level == "Datentypbestimmung":
        ausgabe = None
    elif level == "Alterskontrolle":
        ausgabe = "Schreibe ein Programm, dass ein Alter abfragt. Wenn das Alter über 18 ist, gib aus du bist Volljährig, sonst gib aus, dass die Person noch minderjährig ist."
    elif level == "Notenrechner":
        ausgabe = "Schreibe ein Programm, dass eine Punktzal von 0-100 als Eingabe fordert und dann bei 100-95 Sehr gut, von 80-95 gut, von 60-80 befriedigend, von 40-60 ausreichend von 20-40 ausreichend und von 0-20 ungenügend ausgibt."
    elif level == "Passwort abfrage":
        ausgabe = "Schreibe ein Programm, dass einen Benutzername und ein Passwort als Eingabe fordert. Wenn der Benutzername 'Max' ist und das Passwort 'passwort' ist, gib Anmeldung erfolgreich aus, sonst Anmeldung fehlgeschlagen."

    return ausgabe
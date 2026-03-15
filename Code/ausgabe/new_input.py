"""
Das Programm bekommt einen String übergebn, zeigt den in einem neuen Fenster an und erwartet eine Eingabe
Diese Eingabe wird dann zurückgegeben. Soll die Input-funktion immitieren.
"""
def new_input(string):
    import ttkbootstrap as tb

    #Toplevel Fenster erstellen
    root = tb.Toplevel()
    root.title("Input")
    root.geometry("400x285")
    rueckgabe = [""]

    #Durch root.grab_set() kann man nicht mehr auf andere tkinter zugreifen, bis dieses Fenster geschlossen wurde
    root.grab_set()

    #holt sich die Eingabe des Users und speichert die in rueckgabe. Dann schließt sich das Fenster
    def bestaetigen(r):
        r[0] = eingabe_e.get()

        root.destroy()

    #Label, was den übergeben string anzeigt
    ueberschrift_l = tb.Label(root, text = string, font = ("Helvetica", 12))
    ueberschrift_l.pack(pady = 10)

    #eingabe_textfeld
    eingabe_e = tb.Entry(root, font= ("Helvetica", 12))
    eingabe_e.pack(pady = 20)

    #Button, welcher dei funktion bestaetigen aufruft
    bestaetigen_b = tb.Button(root, text = "bestätigen", command=lambda: bestaetigen(rueckgabe))
    bestaetigen_b.pack(pady = 30)

    #das Programm wartet solange mit der Rückgabe des Wertes, bis das Fenster geschlossen ist
    root.wait_window()

    #gibt die eingabe des Users zurück
    return rueckgabe[0]

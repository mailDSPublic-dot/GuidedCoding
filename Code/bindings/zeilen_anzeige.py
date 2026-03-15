import ttkbootstrap as tb
def zeilen_anzeige(textfeld: tb.Text, zeilenfeld:tb.Text):
    textfeld.edit_modified(False) # setzt Modified auf False, dmit beim nächten Tastendruck Modified wieder umspringt und das Programm erneut ausfgerufen wird
    zeilenfeld.config(state = "normal") # Damit man das Feld kurz bearbeiten kann
    zeilenfeld.delete(1.0, "end") # Löscht alles in dem Feld
    letzte_zeile_textfeld = int(textfeld.index("end-1c").split(".")[0]) # Gibt eine Zahl zurück, wie lang das Textfeld ist
    zeilen_nummern = "\n".join(str(i) for i in range(1, letzte_zeile_textfeld + 1)) # gibt eine Liste mit allen zahlen in der range, vom Textfeld zurück
    zeilenfeld.insert(1.0, zeilen_nummern) # Fügt alle Zeilen in das Textfeld ein

    font = ("Helvetica", 12) # Die Schrift = Helvetica

    # Gleichsetzten der Abstände im Text und Zeilenfeld, damit die Zeilen synchron sind
    textfeld.configure(font=font, spacing1=0, spacing2=0, spacing3=0, padx=0, pady=0)
    zeilenfeld.configure(font=font, spacing1=0, spacing2=0, spacing3=0, padx=0, pady=0)

    # Alle Zahlen in die Mitte des Textfeldes schreiben
    zeilenfeld.tag_configure("center", justify="center")
    zeilenfeld.tag_add("center", 1.0, "end")
    
    # Wenn im Zeilenfeld gescrollt wird, scrollt das Programm auch das Textfeld und umgedreht
    zeilenfeld.config(yscrollcommand= lambda *a: textfeld.yview_moveto(a[0]))
    textfeld.config(yscrollcommand= lambda *a: zeilenfeld.yview_moveto(a[0]))

    zeilenfeld.config(state = "disabled") # Setzt den Status der Zeilen wieder auf nicht bearbeiten
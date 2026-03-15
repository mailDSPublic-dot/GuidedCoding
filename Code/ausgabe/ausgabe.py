# Ausgabe der Ki-Antwort/ Programmausgabe
def ausgabe(eingabe:str, ausgabe_programm, ausgabe_ki, eingabetextfeld):
    from ausgabe.ausgabe_generieren import ausgabe_generieren
    from ausgabe.input_ersetzten import input_ersetzten
    import threading

    ausgabe_programm.config(state="normal") # setzt den Status auf bearbeitbar
    ausgabe_programm.delete(1.0, "end") # Löscht die vorherige Antwort
    ausgabe_programm.insert(1.0, "Die Antwort wird generiert \n...") # Schreib einen Text damit der User weiß, dass die Ki läuft
    ausgabe_programm.config(state="disabled") # Setzt anschließen wieder auf Status: nicht bearbeitbar
    ausgabe_programm.update_idletasks() # Führt die Vorherigen Commands aus


# ------------------------------------------------------------------------------------------------------------
    # Führt das Programm aus und gibt das Ergebnis/ die Fehlermeldung zurück
    def programm_ergebnis():
        nonlocal eingabe
        
        eingabe = input_ersetzten(eingabe)

        ausgabe, zeile = ausgabe_generieren(eingabe, ausgabe_ki)

        ausgabe_programm.config(state="normal") # setzt den Status auf bearbeitbar
        ausgabe_programm.delete(1.0, "end") # Löscht die vorherige Antwort
        ausgabe_programm.insert(1.0, ausgabe) # gibt die Ausgabe des Programmes aus
        ausgabe_programm.config(state="disabled") # Setzt anschließen wieder auf Status: nicht bearbeitbar
        ausgabe_programm.update_idletasks() # Führt die Vorherigen Commands aus
        
        if zeile != None: # Wenn die Zeile nicht nichts ist
            try: # Dann probiere
                eingabetextfeld.tag_configure("error_line", background="#FF6363") # Die Zeile mit dem falschen Code
                eingabetextfeld.tag_add("error_line", f"{zeile}.0", f"{zeile}.end") # zu highlighten
            except: # Wenn das nicht geht(z.B. der User hat die Zeile schon gelöscht), dann
                pass # mache nichts



# ------------------------------------------------------------------------------------------------------------
    # Im Hintergund wird das Programm ausgeführt
    current_thread = threading.Thread(target = programm_ergebnis, daemon = True)
    current_thread.start()
    return None # Gibt NONE zurück, da der aufruf eine Rückmeldung braucht
def ausgabe_generieren(eingabe, ausgabefeld_ki):
    import io
    import contextlib
    # Damit der Code nicht in irgendwo anderes angezeigt wird, wird er abgefangen.
    stdout = io.StringIO() # Speichert den Output in eine Variable um(STanDartOUTput)
    try:
        with contextlib.redirect_stdout(stdout): # Leitet den Output in stdout um
            exec(eingabe) # führt den Code aus
            return stdout.getvalue(), None
        
    except Exception as fehler: # Wenn ein Fehler entsteht
        from ausgabe.chatbot import AI
        ki = AI()
        import threading

        zeile = None # Zeile wird initialisiert

        try: # es wird probiert 
            zeile = fehler.lineno # die Zeile auszulesen
        except:
            pass

        def ki_aufruf(fehler):
            ausgabefeld_ki.config(state="normal") # setzt den Status auf bearbeitbar
            ausgabefeld_ki.delete(1.0, "end") # Löscht die vorherige Antwort
            ausgabefeld_ki.see("end")
            for ausgabe in ki.chatbot(eingabe, fehler):
                ausgabefeld_ki.insert("end", ausgabe) # Gibt die Ausgabe der Ki in das Textfeld einausgabe =  # Speichert die Programmausgabe            
            ausgabefeld_ki.config(state="disabled") # Setzt anschließen wieder auf Status: nicht bearbeitbar

        thread = threading.Thread(target = ki_aufruf, args = (fehler,), daemon = True)
        thread.start()

        return fehler, zeile# Es wird der Fehler und die Zeile zurückgegen
        


        
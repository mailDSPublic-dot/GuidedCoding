def on_close(root, eingabefeld):
    from tkinter import messagebox
    import main_programms.menubar_commands as menucom

    current_file = menucom.current_file # übernimmt die Variable current_file aus dem menu_commands Programm 

    # Prüfen, ob gespeichert wurde
    if eingabefeld.get(1.0, "end") == "Hier den Code eingeben...\n" or eingabefeld.get(1.0, "end") == "\n": # Wenn kein Text eingegeben wurde
        root.destroy() # Schließe das Fenster
    else:
        if current_file != None:
            root.destroy()
        elif not messagebox.askyesno("Speichern?", "Änderungen speichern bevor geschlossen wird?"): # Wenn Nein angeklickt wird
            root.destroy() # Schließe das Fenster
            return
        else:
            menucom.speichern(eingabefeld) # Sonst speichere den Code ab.
            root.destroy() # Und schließe das Fenster

    return None
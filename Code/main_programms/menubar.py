def menubar(root, eingabe_code_t):
    import ttkbootstrap as tb
    import main_programms.menubar_commands as menucom
    from lernen.erklärungen import erklärungen
    from lernen.level_auswahl import level_auswahl

    # Anzeigen des jeweiligen Levels
    def level_weitergabe(string, status):
        if status == "a": # aufgabe
            ausgabe = level_auswahl(string) # Speichert den Text der Angezeigt werden soll
        elif status == "e": # erklärungen
            ausgabe = erklärungen(string)
            
        win = tb.Toplevel()
        win.title(string)
        win.resizable(False, False)

        text_l = tb.Label(win, text=ausgabe, justify="left", anchor="w", font = ("Helvetica", 12))
        text_l.pack(padx=20, pady=10, fill="both")

        ok_b = tb.Button(win, text="OK", command=win.destroy)
        ok_b.pack(pady=10)
        win.update_idletasks()  # Das Fenster anzeigen, um 

        window_width = win.winfo_width() # die größe vom Bildschirm und Fenster
        window_height = win.winfo_height() # berechnen zu können, 
        screenwidth = win.winfo_screenwidth() # um zu wissen, wo das Fenster 
        screenheight = win.winfo_screenheight() # angezeigt werden soll
        x_postion = int((screenwidth - window_width) // 2)
        y_position = int((screenheight - window_height) // 2.5) # leicht über der mitte des Bildschirms 

        win.geometry(f"{window_width}x{window_height}+{x_postion}+{y_position}") # wird das Fenster plaziert

        win.mainloop()

    # Menübar
    menubar = tb.Menu(root) # Erstellen einer Menubar 

    #File Menu
    file_menu = tb.Menu(menubar, tearoff=0) # Hinzufügen des File-Menus zur Menubar
    file_menu.add_command(label = "Neu", command = lambda: menucom.neu(eingabe_code_t)) # Buttons zum File-Menu hinzufügen
    file_menu.add_command(label = "Öffnen", command = lambda : menucom.oeffnen(eingabe_code_t))
    file_menu.add_command(label = "Speichern", command = lambda : menucom.speichern(eingabe_code_t))
    file_menu.add_command(label = "Speichern unter", command = lambda : menucom.speichern_unter(eingabe_code_t))
    menubar.add_cascade(label = "File", menu = file_menu) # Anzeigen des File Menus auf der Menuleiste


    # Edit Menu
    edit_menu = tb.Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Ausschneiden", command = lambda : menucom.cut(eingabe_code_t))
    edit_menu.add_command(label="Kopieren", command = lambda : menucom.copy(eingabe_code_t))
    edit_menu.add_command(label="Einfügen", command = lambda : menucom.paste(eingabe_code_t))
    edit_menu.add_command(label="Undo", command = lambda : menucom.undo(eingabe_code_t))
    edit_menu.add_command(label = "Redo", command = lambda : menucom.redo(eingabe_code_t))
    menubar.add_cascade(label = "Edit", menu = edit_menu)


    # Level Auswahl Menu
    lernen_menu = tb.Menu(menubar, tearoff = 0)

    # 
    lernen_untermenu = tb.Menu(lernen_menu, tearoff = 0)
    rechenoperationen_m = tb.Menu(lernen_menu, tearoff = 0)
    listen_m = tb.Menu(lernen_menu, tearoff = 0)
    

    lernen_untermenu.add_command(label = "Datentypen", command = lambda : level_weitergabe("Datentypen", "e")) # gibt den namen und ob aufgabe(a) oder erklärung (e) weiter
    lernen_untermenu.add_command(label = "Variablen", command = lambda : level_weitergabe("Variablen", "e"))
    lernen_untermenu.add_command(label = "print()", command = lambda : level_weitergabe("print", "e"))
    lernen_untermenu.add_cascade(label = "Rechenarten", menu = rechenoperationen_m)
    rechenoperationen_m.add_command(label = "Rechenoperatoren", command = lambda:level_weitergabe("Rechenoperatoren", "e"))
    rechenoperationen_m.add_command(label = "Mathematische RO", command = lambda:level_weitergabe("Mathematische Rechenoperatoren", "e"))
    rechenoperationen_m.add_command(label = "RO mit Strings", command = lambda:level_weitergabe("Rechenoperationen mit Strings", "e"))
    lernen_untermenu.add_command(label = "input()", command = lambda : level_weitergabe("input", "e"))
    lernen_untermenu.add_command(label = "if, else", command = lambda : level_weitergabe("if-Bedingung, else", "e"))
    lernen_untermenu.add_command(label = "elif", command = lambda : level_weitergabe("elif-Bedingung", "e"))
    lernen_untermenu.add_command(label = "while", command = lambda : level_weitergabe("while-Schleife", "e"))
    lernen_untermenu.add_command(label = "for", command = lambda : level_weitergabe("for-Schleife", "e"))
    lernen_untermenu.add_cascade(label = "Listen", menu = listen_m)
    listen_m.add_command(label = "Listen Überblick", command= lambda: level_weitergabe("Listen Überblick", "e"))
    listen_m.add_command(label = "Listen-Zugriff", command= lambda: level_weitergabe("Listen-Zugriff", "e"))
    listen_m.add_command(label = "Listen-Zugriff mit for", command = lambda : level_weitergabe("Listen-Zugriff mit for", "e"))
    listen_m.add_command(label = "Listen-Befehle", command= lambda: level_weitergabe("Listen-Befehle", "e"))



    komplexe_aufgaben_menu = tb.Menu(lernen_menu, tearoff = 0)
    komplexe_aufgaben_menu.add_command(label = "Notenrechner", command = lambda : level_weitergabe("Notenrechner", "a"))
    komplexe_aufgaben_menu.add_command(label = "Notenrechner", command = lambda : level_weitergabe("Notenrechner", "a"))
    komplexe_aufgaben_menu.add_command(label = "Login", command = lambda : level_weitergabe("Passwort abfrage", "a"))
    
    lernen_menu.add_cascade(label = "Lernen", menu = lernen_untermenu)
    lernen_menu.add_cascade(label = "Komplexe Aufgabe", menu = komplexe_aufgaben_menu)
    menubar.add_cascade(label = "Lernen", menu = lernen_menu)

    # Hilfe Menu
    hilfe = tb.Menu(menubar, tearoff=0)
    hilfe.add_command(label = "Shortcuts", command = menucom.alle_shortcuts)
    hilfe.add_command(label = "About", command =  menucom.about)
    hilfe.add_command(label = "Tutorials", command = menucom.tutorials)
    menubar.add_cascade(label = "Hilfe", menu = hilfe)

    return menubar
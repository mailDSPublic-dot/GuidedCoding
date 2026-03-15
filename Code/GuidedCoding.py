from tkinter import *
import ttkbootstrap as tb
from PIL import Image, ImageTk
import os
import main_programms.menubar_commands as menucom
from main_programms.highlight_code import highlight_code
from main_programms.menubar import menubar
from main_programms.on_close import on_close
from bindings.tabulator import tabulator
from bindings.enter import enter
from ausgabe.ausgabe import ausgabe
from bindings.fokus_nicht_eingabe import fokus_nicht_eingabe
from bindings.fokus_eingabe import fokus_eingabe
from bindings.zeilen_anzeige import zeilen_anzeige



class Bildschirm():
    def __init__(self):
        #Logodatei finden
        skript_ordner = os.path.dirname(os.path.abspath(__file__))
        bildpfad = os.path.join(skript_ordner, "Logo.webp")
        img = Image.open(bildpfad)


# ------------------------------------------------------------------------------------------------------------
        #Hauptbildschirm anpassen
        self.root = tb.Window(themename="darkly") # Dem Fenster das Thema darkly zuweisen
        self.root.title("Coden mit KI") # Programmtitel
        icon = ImageTk.PhotoImage(img) # Programmicon einer Variablen zuweisen
        self.root.iconphoto(False, icon) # Programmeicon einfügen
        self.root.protocol("WM_DELETE_WINDOW", lambda : on_close(self.root, self.eingabe_code_t)) # Wenn das Fenster geschlossen werden soll wird stattdessen die Funktion on_close aufgerufen

        self.root.columnconfigure(0, weight=1) # Die Spalte 0 bekommt den ganzen Platz
        self.root.rowconfigure(0, weight=1) # Die Zeilen 0
        self.root.rowconfigure(1, weight=2) # und 1 teilen sich den Platz 1 zu 2



# ------------------------------------------------------------------------------------------------------------
    # Generieren der Ausgabe
    def ausgabe_aufruf(self, code):
        # Übergibt der Funktion den eingegeben Code, beide Ausgabefelder, das Eingabefeld und die ausgewählte KI
        ausgabe(code, self.ausgabe_programm_t, self.ausgabe_ki_t, self.eingabe_code_t)


# ------------------------------------------------------------------------------------------------------------
    def oberfläche(self):
        # FRAME für alle Eingabefelder
        eingabe_f = tb.Frame(self.root)
        eingabe_f.grid(row=0, column=0, sticky="nsew") # sticky = ausbreiten in Richtung (North, South, East, West)
        eingabe_f.columnconfigure(0, weight=0)
        eingabe_f.columnconfigure(1, weight = 0)
        eingabe_f.columnconfigure(2, weight = 1)
        eingabe_f.rowconfigure(0, weight = 1)
        eingabe_f.rowconfigure(1, weight = 0)

# -----------------------------------------------------------
        # BORDER
        border = tb.Frame(eingabe_f, width=2, bootstyle= "secondary") # bootstyle = secondary = grau
        border.grid(row=0, column=1, sticky="ns") # Der Strick zwischen Zeilen und Eingabefeld

# -----------------------------------------------------------<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # FRAME links eingabe
        zeilennummer_f = tb.Frame(eingabe_f, border= True)
        zeilennummer_f.rowconfigure(0, weight = 1)
        zeilennummer_f.grid(row = 0, column = 0, sticky= "nsew")

# -----------------------------------------------------------
        # TEXT Zeilenfeld
        self.zeilenanzeige_t = tb.Text(zeilennummer_f, width = 4, wrap = NONE, font=("Helvetica", 12))  # wrap = NONE --> kein Umbruch
        self.zeilenanzeige_t.config(background="#191919", foreground="#777", highlightbackground="#191919", highlightcolor="#191919")
        self.zeilenanzeige_t.grid(row = 0, column = 0, sticky = "nsew")
        self.zeilenanzeige_t.config(state = "disabled")

# ----------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # FRAME rechts eingabe
        textbox_f = tb.Frame(eingabe_f)
        textbox_f.grid(row = 0, column = 2, sticky= "nsew")
        textbox_f.columnconfigure(0, weight = 1)
        textbox_f.rowconfigure(0, weight = 1)
        
# -----------------------------------------------------------
        # TEXT Eingabefeld
        self.eingabe_code_t = tb.Text(textbox_f, font=("Helvetica", 12), wrap = WORD, undo = True)  # wrap = WORD --> umbruch nur nach jedem Wort
        self.eingabe_code_t.config(background="#191919", highlightbackground="#191919", highlightcolor="#191919")
        self.eingabe_code_t.grid(row = 0, column= 0, sticky= "nsew")
                                               
# -----------------------------------------------------------|||||||||||||||||||||||||||||||||
        # FRAME unten eingabe
        button_f = tb.Frame(eingabe_f)
        button_f.grid(row = 1, column = 0, sticky= "nsew", columnspan=3)
        button_f.columnconfigure(0, weight = 1)
        button_f.columnconfigure(1, weight = 1)


# -----------------------------------------------------------
        # BUTTON zum ausführen des Codes
        prüfen_b = tb.Button(button_f, text = "ausführen",  command = lambda: self.ausgabe_aufruf(self.eingabe_code_t.get(1.0, "end")))
        prüfen_b.grid(row = 0, column= 1, pady = 10, sticky= "e")

# ------------------------------------------------------------------------------------------------------------
        # FRAME für alle Ausgabefelder
        ausgabe_f = tb.Frame(self.root)
        ausgabe_f.grid(row=1, column=0, sticky="nsew")
        ausgabe_f.columnconfigure(0, weight = 1)
        ausgabe_f.columnconfigure(1, weight = 1)
        ausgabe_f.rowconfigure(0, weight = 1)

# -----------------------------------------------------------------------------------
        # TEXT zur ausgabe der Ausgabe/ausgabe der KI antwort
        self.ausgabe_ki_t = tb.Text(ausgabe_f, wrap = WORD)
        self.ausgabe_ki_t.insert(1.0, "Erklärung der KI (Dauert meist länger)") # für den Anfang wird Ausgabe Angezeigt
        self.ausgabe_ki_t.grid(row = 0, column = 1, sticky="nsew", pady = 20)
        self.ausgabe_ki_t.config(state = "disabled") # Damit der User die Ausgabe nicht bearbeiten kann

# -----------------------------------------------------------
        # AUSGABE des Fehlercodes
        self.ausgabe_programm_t = tb.Text(ausgabe_f, wrap = WORD)
        self.ausgabe_programm_t.grid(row = 0, column = 0, sticky = "nsew", pady = 20)
        self.ausgabe_programm_t.config(state = "disabled") # Damit der User die Ausgabe nicht bearbeiten kann

# -----------------------------------------------------------
        # TASTENKOMBINATIONEN Verknüpfen von Tastenkombinationen mit Funktionen
        self.eingabe_code_t.bind("<KeyRelease>", lambda e: highlight_code(self.eingabe_code_t))
        self.eingabe_code_t.bind("<<Modified>>", lambda e: zeilen_anzeige(self.eingabe_code_t, self.zeilenanzeige_t))
        self.eingabe_code_t.bind("<Tab>", lambda e: tabulator(self.eingabe_code_t))
        self.eingabe_code_t.bind("<Control-z>", lambda e: menucom.undo(self.eingabe_code_t))
        self.eingabe_code_t.bind("<Control-y>", lambda e: menucom.redo(self.eingabe_code_t))
        self.eingabe_code_t.bind("<Control-s>", lambda e: menucom.speichern(self.eingabe_code_t))
        self.eingabe_code_t.bind("<Return>", lambda e: enter(self.eingabe_code_t))
        self.eingabe_code_t.bind("<Control-Return>", lambda e: self.ausgabe_aufruf(self.eingabe_code_t.get(1.0, "end")))

# -----------------------------------------------------------
        # FOKUS Wenn das eingabefeld angeklickt/weggeklickt wird Funktionen
        self.eingabe_code_t.bind("<FocusIn>", lambda e: fokus_eingabe(self.eingabe_code_t))
        self.eingabe_code_t.bind("<FocusOut>", lambda e: fokus_nicht_eingabe(self.eingabe_code_t))
        fokus_nicht_eingabe(self.eingabe_code_t) # damit schon der Text eingefügt wird

# -----------------------------------------------------------
        # MENUBAR
        menu = menubar(self.root, self.eingabe_code_t)
        self.root.config(menu = menu) # Die Menubar anzeigen
        self.root.state("zoomed") # Vollbild

# -----------------------------------------------------------
        # Warmlaufen der Ausgabe und einfügen der ersten Zeilennummer
        self.ausgabe_aufruf("print('Ausgabe Programm')")
        zeilen_anzeige(self.eingabe_code_t, self.zeilenanzeige_t)

        

# ---------------------------------------------------------------------------------------------------------------------------
app = Bildschirm() # Zuweisen der Klasse, init block starten
app.oberfläche() # Oberfläche aufrufen --> Fenster befüllwn
app.root.mainloop() # Startet das Fenster
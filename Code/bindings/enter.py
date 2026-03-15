def enter(textfeld):
    # Automatische einrückung
    index = textfeld.index("insert") # Die aktuelle Courserpoition
    zeilennummer = index.split(".")[0] # Nimmt den ersten Teil des Index(Zeile) z.B. ("5.16") --> 5
    zeile = textfeld.get(f"{zeilennummer}.0", f"{zeilennummer}.end") # Zeileninhalt
    einrückung = len(zeile) - len(zeile.lstrip()) # Gibt die Länge, aller Leerzeichen auf der linken seite zurück

    if zeile.rstrip().endswith(":"): # Wenn das letzte Zeichen abgesehen von leerzeichen ein ":" ist
        textfeld.insert("insert", f"\n{(einrückung + 4) * " " }") # gibt einen zeilenumbruch und die einrückung + 4 Leerzeichen zurück
        return "break" # Damit nicht nochmal umgebrochen wird
    
    elif einrückung > 0:
        textfeld.insert("insert", f"\n{einrückung * " "}") # Gibt die einrückung der Aktuellen Zeile an die nächste weiter
        
        return "break" # Damit nicht nochmal umgebrochen wird
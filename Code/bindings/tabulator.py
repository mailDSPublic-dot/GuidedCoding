def tabulator(eingabefeld):
    #ersetzt tabulator mit 4 Leerzeichen
    eingabefeld.insert("insert", "    ") # insert = aktuelle Stelle des Cursors
    return "break" # man muss break zurückgeben, da sonst 4 Leerzeichen und tabulator aufgeschrieben wird

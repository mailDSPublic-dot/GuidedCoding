"""
Das Programm bekommt ein Text-widget übergeben und highlightet dann verschiedene keywörter
"""

def highlight_code(textfeld):
    # Einer Obergruppe wird eine Farbe zugewiesen
    farb_definition = {"control_flow":"#AD0068",
                "definitions":"#988900",
                "logics":"#7B00FF",
                "imports":"#007E67",
                "values":"#9F3A00",
                "returns":"#CC0000",
                "builtin_funktions":"#AA0000",
                "builtin_typs":"#BB0000",
                "exceptions":"#00AA00",
                "comment": "#007D00", 
                "strings": "#00D9FF",
                "variables": "#0078BE"}
    

    # Definieren der Keywörter und zuweisen zu einem Oberbegriff in einem Dictionary
    listen = {
    "control_flow" : ["if", "else", "elif", "for", "while", "try", "except", "finally", "with"],
    "definitions" : ["def","class", "lambda", "global"],
    "logics" : ["and", "or", "not", "is", "in"],
    "imports" : ["import", "as", "from"],
    "values" : ["True", "False", "None"],
    "returns" : ["return", "break", "pass"],
    "builtin_funktions" : ["print", "len", "open", "min", "max", "input", "dir", "enumerate", "eval", "exec", "format", "round"],
    "builtin_typs" : ["type", "int", "str", "list", "set", "dict", "tupel", "bool", "float", "range"],
    "exceptions" : ["Exception", "ValueError", "TypeError", "KeyError", "indexError", "RuntimeError", "ZeroDivisionError"],
    "comment" : ["#"],
    "strings" : ["'", '"'],
    "variables": []}
    
    zeilen = textfeld.get("1.0", "end").splitlines()# teilt den Text in Zeilen auf

    
    for zeile, string in enumerate(zeilen, start=1): # für jede Zeile in zeilen speichere den Inhalt in String
        for index, zeichen in enumerate(string):
            if zeichen == "=":
                variable = string.split("=")[0] # nimmt den Teil vor dem =
                variable = variable.strip() # entfernt alle Leerzeichen
                if variable.isidentifier(): # wenn die variable eine gültige schreibweise hat
                    listen["variables"].append(variable) # fügt die varibale der Liste hinzu


    # Zuweisen der Obergruppen und Farben zum Textfeld
    for name, farbe in farb_definition.items():
        textfeld.tag_configure(name, foreground=farbe)


    # Entfernen der vorherigen Farben, damit bei löschen eines Buchstaben das Wort nicht trotzdem markiert bleibt
    for name in farb_definition:
        textfeld.tag_remove(f"{name}", "1.0", "end")
    
    textfeld.tag_remove("error_line", "1.0", "end")


#--------------------------------------------------------------------------------------------

    def woerter_trennen(string, zeile):
        woerter_liste = []
        start_index_liste = []
        end_index_liste = []
        aktuelles_wort = ""
        start = 0
        im_string = False

        for index, zeichen in enumerate(string):
        # Schleifen Logik, die Wörter mit index in Listen einfügt und zurüclgibt
            if zeichen in listen["strings"]: # Wenn ein Anführungszeichen im Text ist
                if im_string == True and string[start] == zeichen: # Wenn schon ein Anführungszeichen gefunden wurde und es dem seleben Typ wie dem vorherigen entspricht
                    start_index_liste.append(f"{zeile}.{start}") # Wird der start index der Start_liste hinzugefpgt
                    end_index_liste.append(f"{zeile}.{index +1}") # sowie der Endindex der Endlist
                    woerter_liste.append(zeichen) # Und das Anführungszeichen der Woerterlist
                    im_string = False # Das schon mal ein Afz gefunden wurde wird auf falsch gesetzt, da der string vorbei ist

                elif aktuelles_wort != "":
                    woerter_liste.append(aktuelles_wort) # Das vorherige Wort wird es zur woerterliste hinzugefügt
                    start_index_liste.append(f"{zeile}.{start}") # und der start und
                    end_index_liste.append(f"{zeile}.{index}")  # end index wird in die Indexlist gepackt
                    start = index # Der start_index wird definiert
                    im_string = True # Die Bedingung wird erfüllt, dass schon mal ein "/' gefunden worde

                else:
                    im_string = True #selbe wie drüber, bloß ohne wort hinzufügen
                    start = index
                    
            elif im_string: # solange man im string ist 
                continue # wird einfach übersprungen

            elif zeichen == "#":
                if aktuelles_wort != "": # Wenn ein Wort im Speicher ist
                    woerter_liste.append(aktuelles_wort) # wird es zur woerterliste hinzugefügt
                    start_index_liste.append(f"{zeile}.{start}") # und der start und
                    end_index_liste.append(f"{zeile}.{index}")  # end index wird in die Indexlist gepackt
                woerter_liste.append(zeichen)
                # Hinzufügen des # bevor die Schleife abgebrochen wird
                start_index_liste.append(f"{zeile}.{index}")
                end_index_liste.append(f"{zeile}.{len(string)}")
                break

            else:
                if zeichen.isalnum() or zeichen == "_": # wenn das aktuelle zeiche ein buchstabe/zahl/_ ist
                    if aktuelles_wort == "": # wenn das aktuelle wort nichts ist
                        start = index # wird der start fürs nächste wort festgelegt
                    aktuelles_wort += zeichen # das zeichen wird zum aktuellen wort hinzugenommen
                else:
                    if aktuelles_wort != "": # wenn da aktuelle Wort ein Wort ist
                        woerter_liste.append(aktuelles_wort) # wird es zur woerterliste hinzugefügt
                        start_index_liste.append(f"{zeile}.{start}") # und der strt/end index wird in die Indexlist gepackt
                        end_index_liste.append(f"{zeile}.{index}")
                        aktuelles_wort = "" # zum Schluss wird das Wort aus dem Zwischenspeicher gelöscht 

        if aktuelles_wort != "": # man muss noch das letzte wort in der zeile hinzunehmen, da es nicht durch oben abgefangen wird
            woerter_liste.append(aktuelles_wort) 
            start_index_liste.append(f"{zeile}.{start}")
            end_index_liste.append(f"{zeile}.{len(string)}")

        return woerter_liste, start_index_liste, end_index_liste # Gibt die Liste mit den Wörtern, die Start- und die Endindexliste zurück

#-------------------------------------------------------------------------------------------- 
    
    
    
    for zeile, string in enumerate(zeilen, start=1): # für jede Zeile in zeilen speichere den Inhalt in String
        woerter_liste, start_index_liste, end_index_liste = woerter_trennen(string, zeile) # gib den string und die Zeilennummer an woerter_trennen
        for index, wort in enumerate(woerter_liste): # für jeden eintrag in der Woerterliste speichere die Eintragsnummer in index und den Eintrag in Wort
            for name in farb_definition: # Für jeden Eintrag von farbdefinition
                if wort in listen[name]: # wenn das einer der Listen ist
                    textfeld.tag_add(f"{name}", start_index_liste[index], end_index_liste[index]) # färbe das Wort von start_index bis end_index in der Farbe der jeweiligen Farbe von Farbdefinition
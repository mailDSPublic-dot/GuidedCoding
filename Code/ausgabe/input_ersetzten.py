"""
Das Programm bekommt einen String, welcher dann daruaf überprüft wird, ob er input( enthält. Wenn dies 
der Fall ist, wird inout( mit input_ersetzen( ersetzt und am anfang des Codes wird der Code aus
input_ersetzen eingefügt, bevor der komplette Code zurücgegeben wird.
"""

from pathlib import Path
import os

def input_ersetzten(code:str):
    if "input(" in code: #wenn input( im übergeben Code ist
        dateipfad = Path(__file__).parent #speichert den Dateipfad des Ordners, wo das Programm liegt, in dateipfad
        os.chdir(dateipfad) #Geht zu dem Dateipfad

        code = code.replace("input(", "new_input(") #wird er ersetzt mit input_ersetzen(

        with open("input_ersetzen.py", "r", encoding="utf-8")as input_ersetzen:
            input_ersetzen_text = input_ersetzen.read() #liest die Datei input_ersetzen und speichet sie
        code = input_ersetzen_text + code #als den Code, welcher zurückgegeben werden soll
        return code #Dann wird der Code zurückgegeben 
    
    return code # Sonst gib den Code einfach wieder so zurück

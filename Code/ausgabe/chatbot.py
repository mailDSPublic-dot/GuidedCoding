"""
Das Programm bekommt einen String übergeben und gibt ihn an code_ersetzen weiter.
Die Rückgabe probiert es dann auszuführen. Wenn dies klappt, gibt es das Ergebnis zurück.
Wenn nicht, wird die Fehlermeldung der KI (hier: Phi3 über Transformers) übergeben.
Diese wertet sie dann aus und gibt einen Tipp zurück. Dieser Tipp wird dann zurückgegeben.
"""
class AI():
    def __init__(self):
        from openai import OpenAI
        api_key_1 = "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"
        api_key_2 = "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"
        try:
            self.client = OpenAI(
                api_key=api_key_1,
                base_url="https://openrouter.ai/api/v1"
            )
        except:
            try:
                self.client = OpenAI(
                    api_key=api_key_2,
                    base_url="https://openrouter.ai/api/v1"
                )
            except:
                self.client = None


    def ask_ai_openrouter(self, prompt: str):
        import time
        if self.client != None: # Wenn eine KI geladen werden konnte
            try:
                response = self.client.chat.completions.create( 
                    model="arcee-ai/trinity-large-preview:free",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    stream = True
                )
                
                for chunk in response: # generiere eine Antwort 
                    yield chunk.choices[0].delta.content # und streame die Antwort
                    time.sleep(0.1) # damit RAM gespart wird wird nicht ständig, sondern nur alle 0.1 sek
            except Exception as e:
                return f"Es gab ein Problem bei der Anfrage der KI, probiere es später wieder\n{e}"
        
        else:
            return "Die Ki konnte nicht angesprochen werden (max 100 Anfragen am Tag)"




    def fehler_fuer_ki(self, fehler_typ, linie, code, code_zeile):
        return (f"Du bist eine KI, die Python-Laufzeitfehler erklärt.\n\n"
            f"Fehlertyp: {fehler_typ}\n"
            f"Zeile: {linie}\n"
            f"Code: {code}\n"
            f"Codezeile: {code_zeile}\n\n"
            f"Du bist ein Lehrer, sage keine Lösung vor, sondern erkläre, was der Fehler ist. Nutze keine Markierungen")

    def chatbot(self, code: str, fehler: Exception):
        fehler_typ = fehler.__class__.__name__
        code_zeile = None
        linie = None
        if isinstance(fehler, SyntaxError):
            linie = fehler.lineno
            zeilen = code.splitlines()
            code_zeile = zeilen[linie - 1]

            prompt = self.fehler_fuer_ki(fehler_typ, linie, code, code_zeile)

        
        else:
            try:
                linie = fehler.lineno
                zeilen = code.splitlines()
                code_zeile = zeilen[linie - 1]

            except:
                pass
            
            prompt = self.fehler_fuer_ki = (fehler_typ, linie, code, code_zeile)

        antwort = self.ask_ai_openrouter(prompt)
        return antwort
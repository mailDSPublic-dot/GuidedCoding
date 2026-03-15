import tkinter as tk
import subprocess
import sys
import threading
import os
import time

projekt_ordner = os.path.dirname(os.path.abspath(__file__))
current_step = None
step_start_time = None

# ---------------------------------------------------------
# GGUF MODEL DOWNLOAD
# ---------------------------------------------------------

GGUF_MODELS = {
    "phi3-mini": {
        "repo": "microsoft/Phi-3-mini-4k-instruct-gguf",
        "file": "Phi-3-mini-4k-instruct-q4_k_m.gguf"
    },
    "phi3-small": {
        "repo": "microsoft/Phi-3-small-8k-instruct-gguf",
        "file": "Phi-3-small-8k-instruct-q4_k_m.gguf"
    }
}

# ---------------------------------------------------------
# Phi‑3 GGUF Modelle (offizielle Microsoft-Links)
# ---------------------------------------------------------
MODELS = {
    "phi-3-mini-4k-instruct-q4.gguf":
        "https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/phi-3-mini-4k-instruct-q4.gguf",

    "phi-3-small-8k-instruct-q4.gguf":
        "https://huggingface.co/microsoft/Phi-3-small-8k-instruct-gguf/resolve/main/phi-3-small-8k-instruct-q4.gguf"
}




# ---------------------------------------------------------
# TIMER
# ---------------------------------------------------------

def update_timer():
    if current_step and step_start_time:
        elapsed = time.time() - step_start_time
        timer_label.config(text=f"{current_step} läuft seit {elapsed:.1f} Sekunden")
    else:
        timer_label.config(text="")
    root.after(200, update_timer)

# ---------------------------------------------------------
# INSTALLATION
# ---------------------------------------------------------

def ausfuehren(schritt: str):
    global current_step, step_start_time

    current_step = schritt
    step_start_time = time.time()

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", schritt])


        dauer = time.time() - step_start_time
        text.insert(tk.END, f"✔ Fertig: {schritt} (Dauer: {dauer:.2f}s)\n")
        text.see(tk.END)

    except Exception as e:
        dauer = time.time() - step_start_time
        text.insert(tk.END, f"❌ Fehler bei {schritt}: {e}\n")
        text.insert(tk.END, f"   Dauer bis Fehler: {dauer:.2f}s\n")
        text.see(tk.END)

    finally:
        current_step = None
        step_start_time = None


# ---------------------------------------------------------
# THREAD
# ---------------------------------------------------------

def herunterladen():
    def worker():
        for schritt in schritte:
            ausfuehren(schritt)
        

        text.insert(tk.END, "\n✔ Alle Schritte abgeschlossen\n")
        text.see(tk.END)

    threading.Thread(target=worker, daemon=True).start()

# ---------------------------------------------------------
# GUI
# ---------------------------------------------------------

root = tk.Tk()
root.title("Installer für KI")
root.geometry("600x450")

schritte = [
    "ttkbootstrap",
    "openai"
]

text = tk.Text(root, wrap="word", height=12)
text.pack(expand=True, fill="both")
text.insert(tk.END, "Die folgenden Pakete und Modelle werden automatisch installiert:\n\n")
text.insert(tk.END, "\n".join(schritte))
text.insert(tk.END, "\n\nKlicke auf 'Herunterladen', um zu starten.\n")

timer_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
timer_label.pack(pady=5)

button = tk.Button(root, text="Herunterladen", command=herunterladen)
button.pack(pady=10)

update_timer()
root.mainloop()










if __name__ == "__main__":
    herunterladen()
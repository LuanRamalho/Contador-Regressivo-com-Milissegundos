import tkinter as tk
from tkinter import messagebox
from time import sleep

def start_countdown():
    try:
        total_seconds = float(entry.get())  # Aceita valores decimais
        countdown(total_seconds)
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido!")

def countdown(total_seconds):
    while total_seconds > 0:
        minutos, segundos = divmod(int(total_seconds), 60)
        milesimos = int((total_seconds - int(total_seconds)) * 1000)
        label_timer.config(text=f"{minutos:02}:{segundos:02}:{milesimos:03}")
        root.update()
        sleep(0.001)  # Espera 1 milissegundo
        total_seconds -= 0.011

    label_timer.config(text="00:00:000")
    messagebox.showinfo("Fim", "A contagem regressiva terminou!")

# Configuração da janela principal
root = tk.Tk()
root.title("Contagem Regressiva")
root.geometry("400x300")
root.configure(bg="lightblue")

# Estilo da interface
label_title = tk.Label(
    root, text="Contagem Regressiva", font=("Arial", 20, "bold"), bg="lightblue"
)
label_title.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 16), justify="center")
entry.pack(pady=10)

button_start = tk.Button(
    root, text="Iniciar", font=("Arial", 16, "bold"), bg="green", fg="white", command=start_countdown
)
button_start.pack(pady=20)

label_timer = tk.Label(
    root, text="00:00:000", font=("Arial", 30, "bold"), bg="lightblue", fg="red"
)
label_timer.pack(pady=20)

# Loop principal da interface
root.mainloop()

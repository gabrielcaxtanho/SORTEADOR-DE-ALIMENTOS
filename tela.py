import random
import tkinter as tk

def sortear_alimento():
    alimentos = input_entry.get()
    alimentos = alimentos.split(",")

    alimento_sorteado = random.choice(alimentos)
    resultado_label.config(text="O Lanche da noite selecionado foi: {}".format(alimento_sorteado))

root = tk.Tk()
root.title("Sorteador de Alimentos")

title_label = tk.Label(root, text="Sorteador de Alimentos", font=("Arial", 20, "bold"))
title_label.pack(pady=80)

input_label = tk.Label(root, text="Quais Alimentos você gostaria de sortear para decidir o final (separados por vírgula):")
input_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()

sortear_button = tk.Button(root, text="Sortear", command=sortear_alimento)
sortear_button.pack(pady=50)

resultado_label = tk.Label(root, text="", font=("Arial", 20))
resultado_label.pack()

root.mainloop()

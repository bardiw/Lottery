import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import random


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text File", "*.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(tk.END, file_path)


def select_winners():
    file_path = file_entry.get()
    try:
        num = int(winners_entry.get())
        if num <= 0:
            messagebox.showwarning("wrong number", "Incorrect number!")
            return
    except ValueError:
        messagebox.showwarning("wrong number", "Please enter a number!")
        return

    try:
        with open(file_path, "r") as file:
            name_list = file.read().splitlines()
            if len(name_list) < num:
                messagebox.showwarning("wrong number", "The selected number is more than the number of people!")
                return
            winners_list = random.sample(name_list, num)
            top_window = tk.Toplevel()
            top_window.title("List of winners")
            top_window.geometry("400x600")
            top_window.resizable(1, 1)
            top_window.configure(background="#9E4784")
            win_label = ttk.Label(top_window, text="Lottery winners", font=("Arial", 14),
                                  background="#7A3E65", foreground="white")
            win_label.pack(pady=15)
            winners_list = [f"{i + 1} - {j}" for i, j in enumerate(winners_list)]
            winners = "\n".join(winners_list)
            show_winners = ttk.Label(top_window, text=winners, font=("Arial", 14),
                                     background="#7A3E65", foreground="white")
            show_winners.pack(pady=15)
            top_window.mainloop()

    except FileNotFoundError:
        messagebox.showwarning("No file", "File not found!")
    except Exception as e:
        messagebox.showwarning("error", str(e))


window = tk.Tk()
window.title("Lottery program")
window.geometry("500x500")
window.resizable(True, True)
window.configure(background="#2D2727")

file_label = ttk.Label(window, text="Select the participants file.", font=("Arial", 14),
                       background="#413543", foreground="#FFD966")
file_label.pack(pady=20)

style = ttk.Style()
style.configure("TFrame", background="#19A7CE")
file_frame = ttk.Frame(window, style="TFrame")
file_frame.pack()

file_entry = ttk.Entry(file_frame, font=("Arial", 12))
file_entry.grid(row=0, column=0, padx=5, pady=5)

file_button = ttk.Button(file_frame, text="Select file", command=select_file)
file_button.grid(row=0, column=1, padx=5, pady=5)

winners_label = ttk.Label(window, text="Select the number of participants.", font=("Arial", 14),
                          background="#413543", foreground="#FFD966")
winners_label.pack(pady=20)

winners_entry = ttk.Entry(window, font=("Arial", 12), width=5)
winners_entry.pack()

select_button = ttk.Button(window, text="Select Winners", command=select_winners)
select_button.pack(pady=5)

window.mainloop()

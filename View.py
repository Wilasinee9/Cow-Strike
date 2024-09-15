import tkinter as tk
from tkinter import messagebox

class CowStrikeView:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Cow Strike")
        self.window.geometry("600x400")  # Set smaller window size

        # Create the pages
        self.pages = {}
        self.current_page = None

        self.create_welcome_page()
        self.create_input_page()
        self.create_result_page()
        self.create_goat_page()

        self.show_page("welcome")

    def create_welcome_page(self):
        page = tk.Frame(self.window, bg="white")
        tk.Label(page, text="Welcome to Cow Strike", font=("Helvetica", 18, "bold"), bg="white", fg="black").pack(pady=20)
        tk.Button(page, text="Start", font=("Helvetica", 14), command=lambda: self.show_page("input"), bg="white", fg="black", relief=tk.RAISED).pack(pady=10)
        self.pages["welcome"] = page

    def create_input_page(self):
        page = tk.Frame(self.window, bg="white")
        tk.Label(page, text="Enter Animal ID:", font=("Helvetica", 14), bg="white", fg="black").pack(pady=20)
        self.entry = tk.Entry(page, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        tk.Button(page, text="Submit", font=("Helvetica", 14), command=self.on_submit, bg="white", fg="black", relief=tk.RAISED).pack(pady=10)
        tk.Button(page, text="Back", font=("Helvetica", 14), command=lambda: self.show_page("welcome"), bg="white", fg="black", relief=tk.RAISED).pack(pady=10)
        self.pages["input"] = page

    def create_result_page(self):
        page = tk.Frame(self.window, bg="white")
        self.result_label = tk.Label(page, text="", font=("Helvetica", 14), bg="white", fg="black", wraplength=550)
        self.result_label.pack(pady=20)
        tk.Button(page, text="Back", font=("Helvetica", 14), command=self.go_back_to_input, bg="white", fg="black", relief=tk.RAISED).pack(pady=10)
        self.pages["result"] = page

    def create_goat_page(self):
        page = tk.Frame(self.window, bg="white")

        tk.Label(page, text="Goat Handling", font=("Helvetica", 18, "bold"), bg="white", fg="black").pack(pady=20)
        self.goat_message = tk.Label(page, text="", font=("Helvetica", 14), bg="white", fg="black")
        self.goat_message.pack(pady=20)

        button_frame = tk.Frame(page, bg="white")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Eject Goat", font=("Helvetica", 14), command=self.eject_goat, bg="white", fg="black", relief=tk.RAISED).pack(pady=10)
        tk.Button(button_frame, text="Back", font=("Helvetica", 14), command=lambda: self.show_page("input"), bg="white", fg="black", relief=tk.RAISED).pack(pady=10)

        self.pages["goat"] = page

    def show_page(self, page_name):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.pages[page_name]
        self.current_page.pack(fill="both", expand=True)
        
        # Reset entry field if switching to input page
        if page_name == "input":
            self.entry.delete(0, tk.END)

    def on_submit(self):
        animal_id = self.entry.get()
        self.controller.process_animal(animal_id)

    def show_result(self, message):
        self.result_label.config(text=message)
        self.show_page("result")

    def show_goat_message(self, message):
        self.goat_message.config(text=message)
        self.show_page("goat")

    def eject_goat(self):
        self.show_page("input")
        messagebox.showinfo("Goat Ejected", "Goat has been ejected from the milking machine.")

    def go_back_to_input(self):
        self.show_page("input")
        self.entry.delete(0, tk.END)
        
    def run(self):
        self.window.mainloop()

import tkinter as tk
from tkinter import ttk

# --------------------------
# Calculator App
# --------------------------
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Premium Calculator")
        self.root.geometry("350x500")
        self.root.resizable(False, False)

        self.expression = ""

        # Display
        self.input_text = tk.StringVar()

        input_frame = tk.Frame(self.root, bd=0, bg="#1e1e1e")
        input_frame.pack(expand=True, fill="both")

        input_field = tk.Entry(
            input_frame,
            textvariable=self.input_text,
            font=("Segoe UI", 28),
            bg="#1e1e1e",
            fg="white",
            border=0,
            justify=tk.RIGHT,
        )
        input_field.pack(expand=True, fill="both", padx=20, pady=20)

        # Buttons
        btns_frame = tk.Frame(self.root, bg="#1e1e1e")
        btns_frame.pack(expand=True, fill="both")

        btn_style = {
            "font": ("Segoe UI", 18),
            "bd": 0,
            "fg": "white",
            "activebackground": "#333",
            "activeforeground": "white",
            "bg": "#2a2a2a",
        }

        # Button layout
        buttons = [
            ["C", "←", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="],
        ]

        # Correctly indented loop
        for row in buttons:
            row_frame = tk.Frame(btns_frame, bg="#1e1e1e")
            row_frame.pack(expand=True, fill="both")

            for btn_text in row:
                button = tk.Button(
                    row_frame,
                    text=btn_text,
                    **btn_style,
                    command=lambda t=btn_text: self.on_button_click(t)
                )
                button.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    # Button Logic
    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "←":
            self.expression = self.expression[:-1]
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += str(char)

        self.input_text.set(self.expression)

# --------------------------
# Run App
# --------------------------
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()

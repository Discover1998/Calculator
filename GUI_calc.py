import tkinter as tk
from tkinter import ttk, StringVar, messagebox

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Discovers Calculator")
        self.root.geometry("600x300")

        self.v = StringVar(self.root, "1") 

        header = tk.Label(self.root, text="Welcome to our calculator", font=("Arial", 18))
        header.grid(row=0, column=0, columnspan=3, pady=(10, 5))

        tk.Label(self.root, text="Input value:", font=("Arial", 12)).grid(row=1, column=0, sticky="e", padx=(10,5), pady=5)
        self.value = tk.Entry(self.root, font=("Arial", 14), width=28)
        self.value.grid(row=1, column=1, columnspan=2, sticky="w", padx=(0,10), pady=5)

        options = {
            "Binary -> Decimal": "1",
            "Decimal -> Binary": "2",
            "Hex -> Decimal":    "3",
        }
        r = 2
        for text, val in options.items():
            tk.Radiobutton(self.root, text=text, variable=self.v, value=val).grid(row=r, column=0, columnspan=3, sticky="w", padx=10, pady=3)
            r += 1

        ttk.Button(self.root, text="Calculate", command=self.calculate).grid(row=r, column=0, pady=15, padx=10, sticky="w")
        ttk.Button(self.root, text="Quit", command=self.root.destroy).grid(row=r, column=1, pady=15, sticky="w")

        self.result_var = tk.StringVar(value="Result: ")
        tk.Label(self.root, textvariable=self.result_var, font=("Arial", 12, "bold")).grid(row=r+1, column=0, columnspan=3, sticky="w", padx=10)

        self.root.grid_columnconfigure(1, weight=1)

        self.root.mainloop()


    @staticmethod
    def binary_to_decimal(binary: str):
        s = binary.strip().replace(" ", "")
        if not s or any(ch not in "01" for ch in s):
            return None
        try:
            return int(s, 2)
        except ValueError:
            return None


    @staticmethod
    def decimal_to_binary(decimal_str: str):
        s = decimal_str.strip()
        if not s.isdigit():
            return None
        n = int(s)
        if n < 0 or n > 255:
            return None
        return bin(n)[2:]


    @staticmethod
    def hex_to_decimal(hex_str: str):
        s = hex_str.strip().replace("0x", "").replace("0X", "")
        try:
            return int(s, 16)
        except ValueError:
            return None



    def calculate(self):
        raw = self.value.get()
        choice = self.v.get()
        if choice == "1":  # Bin -> Dec
            out = self.binary_to_decimal(raw)
            label = "Binary → Decimal"
        elif choice == "2":  # Dec -> Bin
            out = self.decimal_to_binary(raw)
            label = "Decimal → Binary"
        else:  # "3" Hex -> Dec
            out = self.hex_to_decimal(raw)
            label = "Hex → Decimal"

        if out is None:
            messagebox.showerror("Invalid input", "Please enter a valid value for the selected conversion.")
            self.result_var.set("Result: (error)")
        else:
            self.result_var.set(f"Result ({label}): {out}")

if __name__ == "__main__":
    MyGUI()

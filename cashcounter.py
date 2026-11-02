import tkinter as tk
from tkinter import ttk

class CashCounterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CashCounter - Instant Breakdown")
        self.geometry("500x550")
        self.configure(bg="#f0f4f8")

        # Modern, clean variables
        self.total_amount = tk.StringVar()
        self.denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
        self.colors = {
            2000: "#2d3436", 500: "#6c5ce7", 200: "#e17055", 100: "#00b894",
            50: "#fdcb6e", 20: "#0984e3", 10: "#d63031", 5: "#00cec9",
            2: "#b2bec3", 1: "#ffeaa7"
        }
        
        self._build_ui()

    def _build_ui(self):
        # 1. Header
        header = tk.Label(self, text="💵 Cash Denomination Breakdown", 
                          font=("Segoe UI", 16, "bold"), bg="#f0f4f8", fg="#2d3436")
        header.pack(pady=20)

        # 2. Input Section
        input_frame = tk.Frame(self, bg="#f0f4f8")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter Total Amount (₹):", 
                 font=("Segoe UI", 12), bg="#f0f4f8").pack(side=tk.LEFT, padx=10)
        
        entry = tk.Entry(input_frame, textvariable=self.total_amount, 
                         font=("Segoe UI", 14), width=15, justify='right')
        entry.pack(side=tk.LEFT)
        
        # Bind 'KeyRelease' to calculate instantly as you type
        self.total_amount.trace('w', self.calculate)

        # 3. Results Section (Grid)
        self.results_frame = tk.Frame(self, bg="#ffffff", bd=1, relief="solid")
        self.results_frame.pack(pady=20, padx=20, fill="x")

        # Headers for the grid
        tk.Label(self.results_frame, text="Denomination", font=("Segoe UI", 11, "bold"), 
                 bg="#ffffff", fg="#636e72").pack(anchor="w", padx=20, pady=(10, 0))
        tk.Label(self.results_frame, text="Count", font=("Segoe UI", 11, "bold"), 
                 bg="#ffffff", fg="#636e72").pack(anchor="w", padx=20, pady=(10, 0))

        # Store labels so we can update them later
        self.note_labels = {}
        for den in self.denominations:
            row = tk.Frame(self.results_frame, bg="#ffffff")
            row.pack(fill="x", padx=20, pady=5)
            
            lbl_den = tk.Label(row, text=f"₹{den}", font=("Segoe UI", 10), bg="#ffffff", fg="#2d3436")
            lbl_count = tk.Label(row, text="0", font=("Segoe UI", 10, "bold"), bg="#ffffff", fg="#2d3436")
            
            lbl_den.pack(side="left", anchor="w")
            lbl_count.pack(side="right", anchor="e")
            
            self.note_labels[den] = lbl_count

        # 4. Visualizer Section (Canvas)
        self.canvas = tk.Canvas(self, height=150, bg="#ffffff", bd=0, highlightthickness=0)
        self.canvas.pack(pady=10, padx=20, fill="x")

    def calculate(self, *args):
        try:
            amount = int(self.total_amount.get())
            if amount < 0:
                amount = 0
        except ValueError:
            amount = 0

        remaining = amount
        counts = {}

        # Standard greedy algorithm for Indian currency
        for den in self.denominations:
            count = remaining // den
            counts[den] = int(count)
            remaining %= den

        # Update UI
        for den, count in counts.items():
            self.note_labels[den].config(text=str(count))

        # Redraw the visual stack
        self._draw_notes(counts)

    def _draw_notes(self, counts):
        self.canvas.delete("all")
        
        # Find the highest denomination present to scale the drawing
        max_den = max((d for d, c in counts.items() if c > 0), default=100)
        
        # Note dimensions
        note_w = 300
        note_h = 40
        stack_y = 10
        gap = 2
        
        # Draw a "stack" for the top denomination
        # (Drawing all 10 types stacked vertically would be too cluttered)
        for den, count in counts.items():
            if count > 0:
                color = self.colors.get(den, "#b2bec3")
                for i in range(count):
                    # Draw note box
                    y_pos = stack_y - (i * gap)
                    self.canvas.create_rectangle(10, y_pos, 10 + note_w, y_pos + note_h, 
                                                 fill=color, outline="#2d3436", width=1)
                    
                    # Draw text inside the top note
                    if i == count - 1:
                        self.canvas.create_text(10 + note_w // 2, y_pos + note_h // 2, 
                                                text=f"₹{den} x {count}", 
                                                fill="white", font=("Segoe UI", 12, "bold"))
                    
                    # Stack offset effect (shift slightly to left for lower notes)
                    stack_y -= 2 

if __name__ == "__main__":
    app = CashCounterApp()
    app.mainloop()
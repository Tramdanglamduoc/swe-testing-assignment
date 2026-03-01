from quick_calc.calculator import Calculator
import tkinter as tk

# ---------- Theme ----------
BG = "#5B8CCB"          # outer background (blue)
CARD = "#EAF2FF"        # card background
DISPLAY_BG = "#CFE3FF"  # display panel
BTN_NUM = "#D8E9FF"     # number buttons
BTN_OP = "#BBD7FF"      # operator buttons
BTN_EQ = "#3F78B8"      # equals button
TXT_DARK = "#16324F"    # dark text
TXT_LIGHT = "#FFFFFF"   # light text


class QuickCalcApp:
    def __init__(self, root: tk.Tk):
        self.calculator = Calculator()

        self.root = root
        self.root.title("Quick-Calc")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        # state
        self.expr = "0"

        # ---- Outer padding frame ----
        outer = tk.Frame(root, bg=BG, padx=18, pady=18)
        outer.pack()

        # ---- Card ----
        card = tk.Frame(outer, bg=CARD, padx=18, pady=18)
        card.pack()

        # ---- Display ----
        display_frame = tk.Frame(card, bg=DISPLAY_BG, padx=14, pady=12)
        display_frame.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 14))

        self.display = tk.Label(
            display_frame,
            text=self.expr,
            bg=DISPLAY_BG,
            fg=TXT_DARK,
            anchor="e",
            font=("Segoe UI", 28, "bold"),
            width=12
        )
        self.display.pack(fill="x")

        # Make columns even
        for c in range(4):
            card.grid_columnconfigure(c, weight=1)

        # ---- Buttons layout (ONLY these buttons) ----
        # Keep positions stable: 7-8-9-/, 4-5-6-*, 1-2-3--, C-0-=-+
        layout = [
            [("7", "num"), ("8", "num"), ("9", "num"), ("/", "op")],
            [("4", "num"), ("5", "num"), ("6", "num"), ("*", "op")],
            [("1", "num"), ("2", "num"), ("3", "num"), ("-", "op")],
            [("C", "op"),  ("0", "num"), ("=", "eq"),  ("+", "op")],
        ]

        for r, row in enumerate(layout, start=1):
            for c, (text, kind) in enumerate(row):
                self._make_button(card, text, kind, r, c)

        self._refresh()

        # Optional: keyboard support (still no extra UI buttons)
        self.root.bind("<Return>", lambda e: self._on_press("="))
        self.root.bind("<BackSpace>", lambda e: self._backspace())
        self.root.bind("<Escape>", lambda e: self._clear())

    # ---------- UI helpers ----------
    def _make_button(self, parent, text: str, kind: str, r: int, c: int):
        if kind == "num":
            bg, fg = BTN_NUM, TXT_DARK
        elif kind == "eq":
            bg, fg = BTN_EQ, TXT_LIGHT
        else:
            bg, fg = BTN_OP, TXT_DARK

        btn = tk.Button(
            parent,
            text=text,
            bg=bg,
            fg=fg,
            activebackground=self._shade(bg, -0.06),
            activeforeground=fg,
            relief="flat",
            bd=0,
            font=("Segoe UI", 16, "bold"),
            width=5,
            height=2,
            command=lambda t=text: self._on_press(t),
        )
        btn.grid(row=r, column=c, padx=8, pady=8, sticky="nsew")

        # Hover effect
        btn.bind("<Enter>", lambda e, b=btn, col=bg: b.configure(bg=self._shade(col, -0.04)))
        btn.bind("<Leave>", lambda e, b=btn, col=bg: b.configure(bg=col))

    def _shade(self, hex_color: str, delta: float) -> str:
        # delta < 0 => darker, delta > 0 => lighter
        hex_color = hex_color.lstrip("#")
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        def clamp(x): return max(0, min(255, x))
        r = clamp(int(r * (1 + delta)))
        g = clamp(int(g * (1 + delta)))
        b = clamp(int(b * (1 + delta)))
        return f"#{r:02X}{g:02X}{b:02X}"

    def _refresh(self):
        self.display.config(text=self.expr)

    # ---------- Calculator behavior ----------
    def _clear(self):
        self.expr = "0"
        self._refresh()

    def _backspace(self):
        if len(self.expr) <= 1:
            self.expr = "0"
        else:
            self.expr = self.expr[:-1]
        self._refresh()

    def _on_press(self, key: str):
        if key == "C":
            self._clear()
            return

        if key == "=":
            self._evaluate()
            return

        # prevent starting with operator (except minus as negative if you want)
        if self.expr == "0" and key in "0123456789":
            self.expr = key
        elif self.expr == "0" and key in "+*/":
            # ignore +*/ at start
            return
        else:
            # avoid repeating operators like "12++3"
            if key in "+-*/" and self.expr[-1] in "+-*/":
                self.expr = self.expr[:-1] + key
            else:
                self.expr += key

        self._refresh()

    def _evaluate(self):
        try:
        # Simple parsing for two-number expressions like "5+3"
            for op in "+-*/":
                if op in self.expr:
                    left, right = self.expr.split(op, 1)  # split only once
                    a = float(left)
                    b = float(right)

                    if op == "+":
                        result = self.calculator.add(a, b)
                    elif op == "-":
                        result = self.calculator.subtract(a, b)
                    elif op == "*":
                        result = self.calculator.multiply(a, b)
                    else:  # op == "/"
                        result = self.calculator.divide(a, b)

                    # show integers nicely
                    if isinstance(result, float) and result.is_integer():
                        result = int(result)

                    self.expr = str(result)
                    break
            else:
                # No operator found (e.g., just "123")
                self.expr = str(int(float(self.expr))) if float(self.expr).is_integer() else str(float(self.expr))

        except ValueError:
            # includes divide by zero (Calculator raises ValueError)
            self.expr = "Error"

        self._refresh()


if __name__ == "__main__":
    root = tk.Tk()
    QuickCalcApp(root)
    root.mainloop()
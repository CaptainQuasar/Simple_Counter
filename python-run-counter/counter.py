import tkinter as tk


class RunCounterOverlay:

  def __init__(self, root):
    self.root = root
    self.root.title("Run Counter")

    # Window settings for overlay
    self.root.overrideredirect(True)  # Removes window borders/title bar
    self.root.attributes("-topmost", True)  # Stays always on top
    self.root.attributes(
        "-alpha", 0.85
    )  # Semi-transparent background (0.0 to 1.0)
    self.root.configure(bg="#18181b")  # Dark modern gaming theme

    # Initial window size and position (width x height + X + Y)
    self.root.geometry("140x95+50+50")

    self.count = 0

    # Drag offset variables
    self.offset_x = 0
    self.offset_y = 0

    self.setup_ui()

  def setup_ui(self):
    # Main container frame
    self.main_frame = tk.Frame(self.root, bg="#18181b")
    self.main_frame.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)

    # Bind dragging to the background frame and title
    self.main_frame.bind("<Button-1>", self.start_move)
    self.main_frame.bind("<B1-Motion>", self.do_move)

    # Header / Title (Neutralized)
    self.lbl_title = tk.Label(
        self.main_frame,
        text="RUN COUNTER",
        font=("Segoe UI", 8, "bold"),
        fg="#a1a1aa",
        bg="#18181b",
    )
    self.lbl_title.pack(anchor="n", pady=(2, 0))
    self.lbl_title.bind("<Button-1>", self.start_move)
    self.lbl_title.bind("<B1-Motion>", self.do_move)

    # Counter Display (Left-click to increment, Right-click to decrement)
    self.lbl_count = tk.Label(
        self.main_frame,
        text="0",
        font=("Segoe UI", 26, "bold"),
        fg="#fafafa",
        bg="#18181b",
        cursor="hand2",
    )
    self.lbl_count.pack(expand=True)
    self.lbl_count.bind("<Button-1>", self.increment)
    self.lbl_count.bind("<Button-3>", self.decrement)  # Right click to decrease

    # Bottom control bar (Reset & Close buttons)
    btn_frame = tk.Frame(self.main_frame, bg="#18181b")
    btn_frame.pack(fill="x", anchor="s")

    self.btn_reset = tk.Button(
        btn_frame,
        text="Reset",
        font=("Segoe UI", 7),
        command=self.reset,
        bg="#27272a",
        fg="#d4d4d8",
        bd=0,
        relief="flat",
        activebackground="#3f3f46",
        activeforeground="#ffffff",
    )
    self.btn_reset.pack(side=tk.LEFT, expand=True, fill="x", padx=(0, 2))

    self.btn_close = tk.Button(
        btn_frame,
        text="✕",
        font=("Segoe UI", 7, "bold"),
        command=self.root.quit,
        bg="#3f1d1d",
        fg="#fca5a5",
        bd=0,
        relief="flat",
        activebackground="#7f1d1d",
        activeforeground="#ffffff",
    )
    self.btn_close.pack(side=tk.RIGHT, padx=(2, 0))

  def start_move(self, event):
    self.offset_x = event.x
    self.offset_y = event.y

  def do_move(self, event):
    x = self.root.winfo_x() + (event.x - self.offset_x)
    y = self.root.winfo_y() + (event.y - self.offset_y)
    self.root.geometry(f"+{x}+{y}")

  def increment(self, event=None):
    self.count += 1
    self.lbl_count.config(text=str(self.count))

  def decrement(self, event=None):
    if self.count > 0:
      self.count -= 1
      self.lbl_count.config(text=str(self.count))

  def reset(self):
    self.count = 0
    self.lbl_count.config(text=str(self.count))


if __name__ == "__main__":
  root = tk.Tk()
  app = RunCounterOverlay(root)
  root.mainloop()
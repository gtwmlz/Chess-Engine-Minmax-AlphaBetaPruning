import tkinter as tk
from gui.chess_ui import ChessUI

if __name__ == "__main__":
    root = tk.Tk()
    app = ChessUI(root)
    root.mainloop()

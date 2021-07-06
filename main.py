from Gui import Gui
import tkinter as tk


def main():
    """Wrapper function"""
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()


if __name__ == '__main__':
    main()

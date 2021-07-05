import tkinter as tk


class Gui:
    def __init__(self, root):
        self.root = root
        root.title("Type Speed Tester")

        self.text_entry_box_title = tk.Label(
            root, text="Type here to start").pack()
        self.text_entry_box = tk.Entry(root).pack()
        self.reset_button = tk.Button(root, text="Reset",
                                      command=self.reset).pack(side="bottom")


    def reset(self):
        return


def main():
    root = tk.Tk()
    app = Gui(root)
    root.mainloop()


if __name__ == '__main__':
    main()

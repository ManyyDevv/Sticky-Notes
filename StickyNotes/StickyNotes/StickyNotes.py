import tkinter
import os

main_window = tkinter.Tk()

BASE_DIR = os.path.dirname(__file__)
icon_path = os.path.join(BASE_DIR, "Icon", "StickyNotesIcon.png")

icon = tkinter.PhotoImage(file=icon_path)
main_window.iconphoto(False, icon)

main_window.title("Sticky Notes")
main_window.minsize(300, 300)
main_window.maxsize(300, 300)

text_widget = tkinter.Text(main_window, font=("Arial", 12))
text_widget.insert("insert", "Add some text!")
text_widget.pack(anchor="w", padx=5, pady=5)

main_window.mainloop()

from tkinter import *
from PIL import Image, ImageTk
import webbrowser

class Helpsupport:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # Background image
        bg1 = Image.open(r"D:\bbhagya_project\Python_Test_Projects\Images_GUI\bg4.png")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # Set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=0, width=1366, height=768)

        # Title section
        title_lb1 = Label(bg_img, text="Help Support", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Email (Gmail) button
        hlp_img_btn = Image.open(r"D:\bbhagya_project\Python_Test_Projects\Images_GUI\gmail.png")
        hlp_img_btn = hlp_img_btn.resize((180, 180), Image.LANCZOS)
        self.hlp_img1 = ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img, command=self.gmail, image=self.hlp_img1, cursor="hand2")
        hlp_b1.place(x=560, y=200, width=180, height=180)

        hlp_b1_1 = Button(bg_img, command=self.gmail, text="Gmail", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        hlp_b1_1.place(x=560, y=380, width=180, height=45)

    def gmail(self):
        self.new = 1
        self.url = "mailto:bhagyashreehandi@gmail.com?subject=Help%20Support"
        webbrowser.open(self.url, new=self.new)

if __name__ == "__main__":
    root = Tk()
    obj = Helpsupport(root)
    root.mainloop()

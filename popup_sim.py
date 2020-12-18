import sys
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import image_similarity
# import image_diff1

class openGUI:

    def __init__(self):
        self.root = Tk()

        self.root.geometry("470x220+550+300")
        self.root.title("We can help you organize your photos using image similarity!")

        Label(self.root, text="불러올 경로 :").place(x=10, y=10, width=90, height=30)
        self.depot = Entry(self.root)
        self.depot.place(x=110, y=10, width=200, height=30)
        Button(self.root, text="경로 선택", command=self.call1).place(x=330, y=10, width=100, height=30)

        Label(self.root, text="저장할 경로 :").place(x=10, y=50, width=90, height=30)
        self.depot2 = Entry(self.root)
        self.depot2.place(x=110, y=50, width=200, height=30)
        Button(self.root, text="저장할 위치", command=self.call2).place(x=330, y=50, width=100, height=30)

        Button(self.root, text="정리", command=self.org_img).place(x=70, y=100, width=100, height=30)
        Button(self.root, text="종료", command=self.root.quit).place(x=180, y=100, width=100, height=30)

        self.root.mainloop()

    def call1(self):
        name = filedialog.askdirectory(initialdir='.')
        self.depot.insert(0, str(name))

    def call2(self):
        name = filedialog.askdirectory(initialdir='.')
        self.depot2.insert(0, str(name))

    def org_img(self):
        image_similarity.sim_set(str(self.depot.get() + '/'), str(self.depot2.get() + '/'))
        tkinter.messagebox.showinfo('메세지 상자', '사진 정리가 완료되었습니다.\n(Organizing is complete.)')




if __name__ == "__main__":
    Example = openGUI()
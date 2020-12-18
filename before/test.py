from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from before import info_list
import os
import shutil
import datetime

class openGUI:

    def __init__(self):
        self.root = Tk()

        self.root.geometry("470x220+550+300")
        self.root.title("We can help you organize your photos!")

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
        info_list.organize_img(str(self.depot.get() + '/'), str(self.depot2.get() + '/'))
        messagebox.showinfo('메세지 상자', '사진 정리가 완료되었습니다.\n(Organizing is complete.)')

def get_imageinfo(file_name):
    date_time = os.path.getmtime(file_name)
    ftime = datetime.datetime.fromtimestamp(date_time)
    return ftime.strftime('%Y-%m-%d %H:%M:%S')

#경로 2개를 받아서 사진이 있는 폴더에서 사진을 리스트화
#for문 이용하여 날짜 정보 추출 + 분류
def organize_img(path1, path2):
    i = 0
    images_list = os.listdir(path1)
    for each_img in images_list:
        num = each_img.find('.')
        file_name = each_img[:num]

        #image 포맷을 가진 파일들만
        if each_img[num+1:] in ['jpeg', 'jpg', 'png', 'gif']:
            #해당 폴더안에 파일들만
            if each_img.find('.') != -1:
                img_info = get_imageinfo(path1 + each_img)
                img_info_m = img_info[:10]
                dic1 = img_info_m[:4]

            #생성할 디렉토리 경로와 중복되는 것이 있는지 검사 후 없으면 해당 경로에 디렉토리 생성
            if not os.path.exists(path2 + dic1 + '/' + img_info_m):
                os.makedirs(path2 + dic1 + '/' + img_info_m)
                i = 0
                shutil.copyfile(path1 + each_img, path2 + dic1 + '/' + img_info_m + '/' + str(i) + '_' + file_name + '.jpg')
            else:
                shutil.copyfile(path1 + each_img, path2 + dic1 + '/' + img_info_m + '/' + str(i) + '_' + file_name + '.jpg')
            i += 1

        #image 파일 아닌 것들
        else:
            if not os.path.exists(path2 + 'notimage_files'):
                os.makedirs(path2 + 'notimage_files')
                shutil.copyfile(path1 + each_img, path2 + 'notimage_files' + '/' + each_img)
            else:
                shutil.copyfile(path1 + each_img, path2 + 'notimage_files' + '/' + each_img)

if __name__ == "__main__":
    Example = openGUI()

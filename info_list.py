from PIL import Image
from PIL.ExifTags import TAGS
import os
import shutil

#사진 정보(날짜)를 추출
def get_imageinfo(file_name):
    img = {}
    i = Image.open(file_name)
    info = i._getexif()
    if info == None:
        return None
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        img[decoded] = value

    return img["DateTime"]

#경로 2개를 받아서 사진이 있는 폴더에서 사진을 리스트화
#for문 이용하여 날짜 정보 추출 + 분류
def organize_img(path1, path2):
    i = 0
    images_list = os.listdir(path1)
    #에러 남
    for each_img in images_list:
        img_info = get_imageinfo(path1 + each_img)
        img_info_m = img_info[:10].replace(':', '-') #날짜를 -로 바꿈
        dic1 = img_info_m[:4]

        #생성할 디렉토리 경로와 중복되는 것이 있는지 검사 후 없으면 해당 경로에 디렉토리 생성
        if not os.path.exists(path2 + dic1 + '/' + img_info_m):
            os.makedirs(path2 + dic1 + '/' + img_info_m)
            i = 0
            shutil.copyfile(path1 + each_img, path2 + dic1 + '/' + img_info_m + '/' + img_info_m + '' + str(i) + '.jpg')
        else:
            shutil.copyfile(path1 + each_img, path2 + dic1 + '/' + img_info_m + '/' + img_info_m + '' + str(i) + '.jpg')
        i += 1
from PIL import Image
from PIL.ExifTags import TAGS
import os
import shutil
import time
import datetime

#사진 정보(날짜)를 추출
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
        if each_img[num+1:] in ['jpeg', 'jpg', 'png', 'gif', 'PNG', 'JPG', 'JPEG', 'GIF']:
            #해당 폴더안에 파일들만
            if each_img.find('.') != -1:
                img_info = get_imageinfo(path1 + each_img)
                img_info_m = img_info[:10]

            #생성할 디렉토리 경로와 중복되는 것이 있는지 검사 후 없으면 해당 경로에 디렉토리 생성
            if not os.path.exists(path2 + img_info_m):
                os.makedirs(path2 + img_info_m)
                i = 0
                shutil.copyfile(path1 + each_img,
                                path2 + img_info_m + '/' + str(i) + '_' + file_name + '.jpg')
            else:
                shutil.copyfile(path1 + each_img,
                                path2 + img_info_m + '/' + str(i) + '_' + file_name + '.jpg')
            i += 1

        #image 파일 아닌 것들
        else:
            if not os.path.exists(path2 + 'notimage_files'):
                os.makedirs(path2 + 'notimage_files')
                shutil.copyfile(path1 + each_img, path2 + 'notimage_files' + '/' + each_img)
            else:
                shutil.copyfile(path1 + each_img, path2 + 'notimage_files' + '/' + each_img)
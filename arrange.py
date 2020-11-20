import glob
import os
import time
import shutil

targerdir = "C:/Users/hansung/Desktop" #불러오는 경로

files = os.listdir(targerdir)
condition = '*.jpg'
files_list = [x for x in files if(x.endswith(".jpg")==True)]

for i in range(0,len(files_list)):
        filepath = os.getcwd()
        k = files_list[i]
        t = os.path.getmtime(k)  #파일의 수정시간 가져오기 11231234 형태
        tc = time.ctime(t)  #
        timestr = time.strptime(tc)
        directoryName = time.strftime("%Y-%m-%d",timestr) #yyyy-mm-dd 형태의 폴더
        #print(os.stat(targerdir).st_mtime) 지정된 경로를 찾을 수 없다고 계속 뜸...



        filePath = os.path.split(k)[0]#날짜
        fileName = os.path.split(k)[1]
        changePathFile = os.path.join(filePath,directoryName,fileName) #target
        targetPath = os.path.join(filePath,directoryName)# 날짜



        if os.path.isdir(k):  # 디렉토리면디렉토리 복사

                if os.path.exists(targetPath): # 해당 날짜 디렉토리가 있을때
                        shutil.copytree(k, os.path.join(targetPath, fileName))
                else:
                        os.mkdir(targetPath)  # 디렉토리생성 및 권한부여
                        shutil.copytree(k, os.path.join(targetPath, fileName))

        else:
                if os.path.exists(targetPath): # 날짜별 디렉토리가 있는지 체크없으면 false
                        shutil.copyfile(k, changePathFile)  # 파일복사(이동 move)
                else:
                        os.mkdir(targetPath)  # 디렉토리생성 및 권한부여
                        shutil.copyfile(k, changePathFile)


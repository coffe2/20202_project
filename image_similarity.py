import opencv as oc
import shutil
import os
import info_list

def sim_set(path1, path2):
    files = os.listdir(path1)
    img_files = []
    for idx in range(len(files)):
        num = files[idx].find('.')
        if files[idx][num+1:] in ['jpeg', 'jpg', 'png', 'gif', 'PNG', 'JPG', 'JPEG', 'GIF']:
            img_files += [files[idx]]

    img_set = []
    simm_file = []
    for img1 in range(len(img_files)-1):
        for img2 in range(img1+1, len(img_files)):
            if info_list.get_imageinfo(path1 + '/' + files[img1]) == info_list.get_imageinfo(path1 + '/' + files[img2]):
                img_set += [(files[img1], files[img2])]
                simm_file += [files[img1], files[img2]]
        print(simm_file)
    num = 0
    for samedate1, samedate2 in img_set:
        ig1 = path1 + '/' + samedate1
        ig2 = path1 + '/' + samedate2
        cc = oc.flann(ig1, ig2)
        if int(cc) > 30:
            if not os.path.exists(path2 + 'sim' + str(num)):
                os.makedirs(path2 + 'sim' + str(num))
                shutil.copyfile(path1 + samedate1, path2 + 'sim' + str(num) + '/' + samedate1)
                shutil.copyfile(path1 + samedate2, path2 + 'sim' + str(num) + '/' + samedate2)
                num += 1
            else:
                shutil.copyfile(path1 + samedate1, path2 + 'sim' + str(num) + '/' + samedate1)
                shutil.copyfile(path1 + samedate2, path2 + 'sim' + str(num) + '/' + samedate2)
        else:
            shutil.copyfile(path1 + samedate1, path2 + samedate1)
            shutil.copyfile(path1 + samedate2, path2 + samedate2)
    simm_file = list(set(simm_file))
    for simm_img in simm_file:
        img_files.remove(simm_img)
    for other in img_files:
        shutil.copyfile(path1 + other, path2 + other)
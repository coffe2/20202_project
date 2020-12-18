import cv2
import numpy as np
import os
import info_list

def flann(img1,img2):
    img1 = cv2.imread(img1, 0)
    img2 = cv2.imread(img2, 0)

    sift = cv2.xfeatures2d.SIFT_create()

    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches1 = flann.knnMatch(des1, des2, k=2)

    # ratio test 적용
    c = 0
    good = []
    for m, n in matches1:
        if m.distance < 0.7 * n.distance:
            good.append(m)
            c +=1
    print(len(good))

    if len(good) > 30:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()

        h, w = img1.shape
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, M)
        img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
        return len(good)
    else:
        #print("Not enough matches are found - %d/%d" % (len(good), 10))
        matchesMask = None
        return 0

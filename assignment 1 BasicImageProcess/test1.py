import cv2
import numpy as np
import matplotlib.pyplot as plt

#1 numpyを使った行列の四則演算
# mat1 = np.matrix([[1,2],[3,4]])
# mat2 = np.random.randint(0,10,(2,2))
# print("matrix1 and matrix2")
# print(mat1)
# print(mat2)
# print("plus")
# mat_plus = mat1 + mat2
# print(mat_plus)
# print("minus")
# mat_minus = mat1 - mat2
# print(mat_minus)
# print("multiply")
# mat_multiply=mat1 * mat2
# print(mat_multiply)
#
# vec1 = np.array([1,2,3])
# vec2 = np.random.randint(0,10,3)
# print("vector1 and vector2")
# print(vec1)
# print(vec2)
# print("inner")
# vec_inner = np.inner(vec1,vec2);
# print(vec_inner);

#2 画像の表示，縮小拡大，回転，二値化
##表示
# img = cv2.imread('4.jpg', cv2.IMREAD_COLOR)
# cv2.imshow('img',img)

##縮小拡大
# imgBig = cv2.resize(img,None,None,1.2,1.2,cv2.INTER_LINEAR )
# imgSml = cv2.resize(img,None,None,0.8,0.8,cv2.INTER_LINEAR )
## cv2.imwrite('imgBig.png', imgBig)
## cv2.imwrite('imgSml.png', imgSml)
# cv2.imshow('imgBig',imgBig)
# cv2.imshow('imgSml',imgSml)
# K =cv2.waitKey(0)

##回転
# imgTrans1 = cv2.transpose(img)
# imgTrans2 = cv2.flip(imgTrans1,1)
# imgTrans3 = cv2.flip(imgTrans1,0)
#
# imgTrans4 = cv2.transpose(imgTrans2)
# imgTrans4 = cv2.flip(imgTrans4,1)
# # cv2.imshow('imgTrans1',imgTrans1)
# # cv2.imwrite('imgTrans2.png', imgTrans2)
# # cv2.imwrite('imgTrans3.png', imgTrans3)
# cv2.imshow('imgTrans2',imgTrans2) #右回り90度
# cv2.imshow('imgTrans3',imgTrans3)#左回り90度
# cv2.imshow('imgTrans4',imgTrans4) #右回り180度



#二値化
def access_pixelsGray(image):
    height, width = image.shape
    print("width:%s,height:%s" % (width, height))

    for row in range(height):
        for list in range(width):
                pv = image[row, list]
                image[row, list] = 255 - pv
    cv2.imshow("AfterDeal", image)
#
# img2 = cv2.imread('flower1.jpg', cv2.IMREAD_COLOR)
# # cv2.imwrite('img2_f.png', img2)
# gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray)
#
# # h, w = gray.shape[:2]
# # m = np.resize(gray, [1, w*h])
# # mean = m.sum() / (w*h)
# # print('mean : ', mean)
#
# # thresholdValue,two_value =cv2.threshold(gray,mean,255,cv2.THRESH_BINARY);
# thresholdValue,two_value =cv2.threshold(gray,100,255,cv2.THRESH_BINARY);
# # print('thresholdValue %s :' % (thresholdValue))
# cv2.imwrite('gray.png', gray)
# cv2.imwrite('two_value.png', two_value)
# cv2.imshow("two_value",two_value)
# # access_pixelsGray(two_value)

#3 差分画像作成

def access_pixels(image):
    height, width, channels = image.shape
    print("width:%s,height:%s,channels:%s" % (width, height, channels))

    for row in range(height):
        for list in range(width):
            for c in range(channels):
                pv = image[row, list, c]
                image[row, list, c] = 255 - pv
    cv2.imshow("AfterDeal", image)

# img1 = cv2.imread('4-1.png', cv2.IMREAD_COLOR)
# img2 = cv2.imread('4-2.png', cv2.IMREAD_COLOR)
# cv2.imshow("img1",img1)
# cv2.imshow("img2",img2)

#method1

# err = cv2.absdiff(img2,img1)
# cv2.imshow("err",err)
# access_pixels(err)

#method2
#
# im_diff =img1.astype(int)-img2.astype(int)
# im_diff_abs = np.abs(im_diff)
#
# # b,g,r = cv2.split(im_diff_abs)
# # img_err = cv2.merge([r,g,b])
# #
# # plt.imshow(img_err)
# # plt.show()
#
# cv2.imwrite('img_diff.png', im_diff_abs)
#
#
# img_diff = cv2.imread('img_diff.png', cv2.IMREAD_COLOR)
# cv2.imshow("im_diff",img_diff)
# access_pixels(img_diff)

#4 画像の特徴量抽出と図示

# #ヒストグラム
# img_gray = cv2.imread('4.jpg',0)
# # img = cv2.imread('4.jpg',1)
# # cv2.imshow('img_gray',img_gray)
# hist0 = cv2.calcHist([img_gray],[0],None,[256],[0,256]) #グレースける画像
# # histB = cv2.calcHist([img],[0],None,[256],[0,256]) #カラー画像 Bの色相
# # histG = cv2.calcHist([img],[1],None,[256],[0,256]) #カラー画像 Gの色相
# # histR = cv2.calcHist([img],[2],None,[256],[0,256]) #カラー画像 Rの色相
# hist1,bins = np.histogram(img_gray.ravel(),256,[0,256])
# plt.subplot(221),plt.imshow(img_gray,'gray')
# # b,g,r = cv2.split(img)
# # img2 = cv2.merge([r,g,b])
#
# # plt.subplot(221),plt.imshow(img2)
# plt.subplot(222),plt.plot(hist0)
# plt.subplot(223),plt.plot(hist1)
# # plt.subplot(222),plt.plot(histB)
# # plt.subplot(223),plt.plot(histG)
# # plt.subplot(224),plt.plot(histR)
# plt.show()

#ORB
# img_smP1 = cv2.imread('flower1.jpg',1) #花
# # img_smP1 = cv2.imread('cat1.jpg',1)　#猫
# # img_smP1 = cv2.imread('4.jpg',1)　#
# # img_smP1 = cv2.imread('100_2.jpg',1)　#100円玉
# cv2.imshow('img_smP1',img_smP1)
# orb = cv2.ORB_create()
# kp, des = orb.detectAndCompute(img_smP1, None)
# img_smP1 = cv2.drawKeypoints(img_smP1, kp, None, (0, 0, 255))
# cv2.imshow('kp', img_smP1)

#FAST
# img_smP1 = cv2.imread('flower1.jpg',1)
# fast = cv2.FastFeatureDetector_create(10)
# keypoints = fast.detect(img_smP1, None)
# img_smP1 = cv2.drawKeypoints(img_smP1, keypoints, None, (0, 0, 255))
# cv2.imshow('kp',img_smP1)

#A-KAZE
# img_smP1 = cv2.imread('flower1.jpg',1)
# detector = cv2.AKAZE_create()
# kp, des = detector.detectAndCompute(img_smP1, None)
# img_smP1 = cv2.drawKeypoints(img_smP1, kp, None, (0, 0, 255))
# cv2.imshow('kp',img_smP1)


# match two pictures
# img_flw1 = cv2.imread('flower1.jpg',1)
# img_flw2 = cv2.imread('flower2.jpg',1)
#
# cv2.imshow('img_flw1',img_flw1)
# cv2.imshow('img_flw2',img_flw2)
#
# orb = cv2.ORB_create()
# kp1,des1 = orb.detectAndCompute(img_flw1, None)
# kp2,des2 = orb.detectAndCompute(img_flw2, None)
# bf = cv2.BFMatcher()
# matches = bf.knnMatch(des1,des2,2)
# good = []
# match_param = 0.8
# for m,n in matches:
#     if m.distance < match_param*n.distance:
#         good.append([m])
# img3 = cv2.drawMatchesKnn(img_flw1,kp1,img_flw2,kp2,good, None,2)
# cv2.imshow('img3',img3)



# K =cv2.waitKey(0)

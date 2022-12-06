# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import cv2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    eye_mask = cv2.imread('/Users/xinpang/Desktop/Studium/Informatik M.sc/2.Semester/MPL/project/Data/facemaker_segmentations/eyes_mask.png',0)
    # cv2.imshow('eye mask',eye_mask)
    # cv2.waitKey(0)
    mask_size=(eye_mask.shape[0],eye_mask.shape[1])
    print('Original length:',mask_size[0],'Original height:', mask_size[1])
    target_size=(500,500)
    resized_eye_mask = cv2.resize(eye_mask,target_size)
    print('new length:',resized_eye_mask.shape[0],'new height:', resized_eye_mask.shape[1])
    #first image: 170<x<670 and 20<y<520
    #second image: 710<x<1210 and 20<y<520
    #third image: 1250<x<1750 and 20<y<520
    #forth image: 170<x<670 and

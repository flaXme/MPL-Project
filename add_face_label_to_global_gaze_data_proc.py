#This scritp generates a new csv file with face labels to the training data.
#Where: -1 -> not defined, 1 -> cheeks, 2 -> ears, 3 -> eyes, 4 -> forehead, 5 -> hair, 6 -> jaw, 7 -> mouth, 8 -> nose, -2 -> boundary case
import csv
import cv2
from csv import reader

#first image: 170<x<670 and 20<y<520
def in_image_one(x,y):
    if x > 170 and x < 670 and y > 20 and y < 520:
        return True
    return False
#second image: 710<x<1210 and 20<y<520
def in_image_two(x,y):
    if x > 710 and x < 1210 and y > 20 and y < 520:
        return True
    return False
#third image: 1250<x<1750 and 20<y<520
def in_image_three(x,y):
    if x > 1250 and x < 1750 and y > 20 and y < 520:
        return True
    return False
#forth image: 170<x<670 and 560<y<1060
def in_image_four(x,y):
    if x >170 and x < 670 and y > 560  and y < 1060:
        return True
    return False
#fifth image: 710<x<1210 and 560<y<1060
def in_image_five(x,y):
    if x > 710 and x < 1210 and y > 560 and y < 1060:
        return True
    return False
#sisth image: 1250<x<1750 and 560<y<1060
def in_image_six(x,y):
    if x > 1250 and x < 1750 and y > 560 and y < 1060:
        return True
    return False
# Transform the global coordinates to image coordinates of the corresponding image in the collage.
def global_to_local(x,y):
    if in_image_one(x,y):
        return x - 170, y - 20
    elif in_image_two(x,y):
        return x - 710, y - 20
    elif in_image_three(x,y):
        return x - 1250, y - 20
    elif in_image_four(x,y,):
        return x - 170, y - 560
    elif in_image_five(x,y):
        return x - 710, y - 560
    elif in_image_six(x,y):
        return x - 1250, y - 560
    else:
        return -1
# Determine whether a given image coordinate is in cheeks area.
def in_cheeks_area(x,y):
    if resized_cheeks_mask[x][y] == 0:
        return True
    return False
# Determine whether a given image coordinate is in ears area.
def in_ears_area(x,y):
    if resized_ears_mask[x][y] == 0:
        return True
    return False
# Determine whether a given image coordinate is in eye area.
def in_eye_area(x,y):
    if resized_eye_mask[x][y] == 0:
        return True
    return False
# Determine whether a given image coordinate is in forehead area.
def in_forehead_area(x,y):
    if resized_forehead_mask[x][y] == 0:
        return True
    return False
# Determine whether a given image coordinate is in hair area.
def in_hair_area(x,y):
    if resized_hair_mask[x][y] == 0:
        return True
    return False
# Determine whether a given image coordinate is in jaw area.
def in_jaw_area(x,y):
    if resized_jaw_mask[x][y] == 0:
        return True
    return False
# Determine whether a given image coordinate is in mouth area.
def in_mouth_area(x,y):
    if resized_mouth_mask[x][y] == 0:
        return True
    return False

# Determine whether a given image coordinate is in nose area.
def in_nose_area(x,y):
    if resized_nose_mask[x][y] == 0:
        return True
    return False
# Determine the area on which a given point is.
# Where -1 -> not defined, 1 -> cheeks, 2 -> ears, 3 -> eyes, 4 -> forehead, 5 -> hair, 6 -> jaw, 7 -> mouth, 8 -> nose, -2 -> boundary case
def register_point(x,y):
    image_cor = global_to_local(x,y)
    if image_cor == -1:
        return -1
    elif in_cheeks_area(image_cor[0], image_cor[1]):
        return 1
    elif in_ears_area(image_cor[0],image_cor[1]):
        return 2
    elif in_eye_area(image_cor[0], image_cor[1]):
        return 3
    elif in_forehead_area(image_cor[0],image_cor[1]):
        return 4
    elif in_hair_area(image_cor[0],image_cor[1]):
        return 5
    elif in_jaw_area(image_cor[0],image_cor[1]):
        return 6
    elif in_mouth_area(image_cor[0], image_cor[1]):
        return 7
    elif in_nose_area(image_cor[0],image_cor[1]):
        return 8
    else:
        return -2


if __name__ == '__main__':
    #read eight masks and resize them to 500x500
    path_to_the_masks = '/Users/xinpang/Desktop/Studium/Informatik M.sc/2.Semester/MPL/project/Data/facemaker_segmentations'
    cheeks_mask = cv2.imread(f'{path_to_the_masks}/cheeks_mask.png',0)
    ears_mask = cv2.imread(f'{path_to_the_masks}/ears_mask.png',0)
    eyes_mask = cv2.imread(f'{path_to_the_masks}/eyes_mask.png',0)
    forehead_mask = cv2.imread(f'{path_to_the_masks}/forehead_mask.png',0)
    hair_mask = cv2.imread(f'{path_to_the_masks}/hair_mask.png',0)
    jaw_mask = cv2.imread(f'{path_to_the_masks}/jaw_mask.png',0)
    mouth_mask = cv2.imread(f'{path_to_the_masks}/mouth_mask.png',0)
    nose_mask = cv2.imread(f'{path_to_the_masks}/nose_mask.png',0)


    mask_size=(eyes_mask.shape[0],eyes_mask.shape[1])
    target_size=(500,500)
    resized_cheeks_mask = cv2.resize(cheeks_mask, target_size)
    resized_ears_mask = cv2.resize(ears_mask, target_size)
    resized_eye_mask = cv2.resize(eyes_mask,target_size)
    resized_forehead_mask = cv2.resize(forehead_mask, target_size)
    resized_hair_mask = cv2.resize(hair_mask, target_size)
    resized_jaw_mask = cv2.resize(jaw_mask, target_size)
    resized_mouth_mask = cv2.resize(mouth_mask, target_size)
    resized_nose_mask = cv2.resize(nose_mask, target_size)

    #simple test
    # global_cor = (1028, 356)
    # cor = global_to_local(global_cor[0],global_cor[1])
    # print('local cor:', cor)
    # print("in cheeks area:",in_cheeks_area(cor[0],cor[1]))
    # print('in ears area:', in_ears_area(cor[0],cor[1]))
    # print('in eye area:', in_eye_area(cor[0], cor[1]))
    # print('in forehead area:', in_forehead_area(cor[0],cor[1]))
    # print('in hair area:', in_hair_area(cor[0],cor[1]))
    # print('in jaw area:', in_jaw_area(cor[0],cor[1]))
    # print('in mouth area:', in_mouth_area(cor[0],cor[1]))
    # print('in nose area:', in_nose_area(cor[0], cor[1]))

    #read csv file and generate a new csv file with attached face labels.:
    path_to_the_gaze_data = '/Users/xinpang/Desktop/Studium/Informatik M.sc/2.Semester/MPL/project/Data/gaze_data/train/0'
    with open(f'{path_to_the_gaze_data}/global_gaze_data_proc.csv', 'r') as read_obj:
        global_cor = (-1,-1)
        csv_reader = reader(read_obj)
        with open(f'{path_to_the_gaze_data}/labled_global_gaze_data_proc.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file)
            for row in csv_reader:
                global_cor = (round(float(row[1])),round(float(row[2])))
                area = register_point(global_cor[0],global_cor[1])
                row.append(area)
                csv_writer.writerow(row)
    print('done')
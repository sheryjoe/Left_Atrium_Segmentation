import os
import numpy as np
import nrrd
from PIL import Image


def saveSlice(image, label,
              image_path,
              label_path,
              patient_name, image_name,
              label_name, slice_num):

    image = Image.fromarray(image)
    label = Image.fromarray(label)
    patient_image_iter_path = patient_name + "_" + image_name + "_" + slice_num +'.png'
    patient_label_iter_path = patient_name + "_" + label_name + "_" + slice_num + '.png'

    save_image_path = os.path.join(image_path, patient_image_iter_path)
    save_label_path = os.path.join(label_path, patient_label_iter_path)

    image.save(save_image_path)
    label.save(save_label_path)


PATH = PATH = "../Dataset"
DATA_DIR_TRAIN = "/Training Set"
DATA_DIR_TEST = "/Testing Set"

DATA_DIR_TRAIN = PATH + DATA_DIR_TRAIN
DATA_DIR_TEST = PATH + DATA_DIR_TEST

train_val_patient_list = sorted(os.listdir(DATA_DIR_TRAIN))
test_patient_list = sorted(os.listdir(DATA_DIR_TEST))

print(len(train_val_patient_list))
print(len(test_patient_list))

i=0

for train_val_patient_iter in train_val_patient_list:

    print("Patient: "+str(i))
    train_val_patient_path = os.path.join(DATA_DIR_TRAIN, train_val_patient_iter)
    print(train_val_patient_path)
    train_val_patient_image_path = os.path.join(train_val_patient_path, "lgemri.nrrd")
    train_val_patient_label_path = os.path.join(train_val_patient_path, "laendo.nrrd")

    train_val_patient_image, train_val_patient_image_header = nrrd.read(train_val_patient_image_path)
    train_val_patient_label, train_val_patient_label_header = nrrd.read(train_val_patient_label_path)

    train_val_patient_image = np.transpose(train_val_patient_image, (2, 1, 0))
    train_val_patient_label = np.transpose(train_val_patient_label, (2, 1, 0))

    image_path = train_val_patient_path + "/Images"
    label_path = train_val_patient_path + "/Labels"

    try:
        os.makedirs(image_path, exist_ok=True)
        os.makedirs(label_path, exist_ok=True)
        print("Directory '%s' created successfully" % image_path)
        print("Directory '%s' created successfully" % label_path)
    except OSError as error:
        print("Directory '%s' can not be created" % image_path)
        print("Directory '%s' can not be created" % label_path)

    (dimx, dimy, dimz) = train_val_patient_image.shape

    for slice_num in range(dimx):
        saveSlice(train_val_patient_image[slice_num],
                  train_val_patient_label[slice_num],
                  image_path, label_path, train_val_patient_iter,
                  image_name="image", label_name="mask", slice_num=str(slice_num))

    print("Training image slices saved in '%s'" %image_path)
    print("Training label slices saved in '%s'" %label_path)
    i+=1
    '''print("Patient details: ")
    print(np.max(train_val_patient_image), np.min(train_val_patient_image), train_val_patient_image.shape, type(train_val_patient_image))
    print(np.max(train_val_patient_label), np.min(train_val_patient_label), train_val_patient_label.shape, type(train_val_patient_label))'''

j=0

for test_patient_iter in test_patient_list:

    print("Patient: "+str(j))
    test_patient_path = os.path.join(DATA_DIR_TEST, test_patient_iter)
    print(test_patient_path)
    test_patient_image_path = os.path.join(test_patient_path, "lgemri.nrrd")
    test_patient_label_path = os.path.join(test_patient_path, "laendo.nrrd")

    test_patient_image, test_patient_image_header = nrrd.read(test_patient_image_path)
    test_patient_label, test_patient_label_header = nrrd.read(test_patient_label_path)

    test_patient_image = np.transpose(test_patient_image, (2, 1, 0))
    test_patient_label = np.transpose(test_patient_label, (2, 1, 0))

    image_path = test_patient_path + "/Images"
    label_path = test_patient_path + "/Labels"

    try:
        os.makedirs(image_path, exist_ok=True)
        os.makedirs(label_path, exist_ok=True)
        print("Directory '%s' created successfully" % image_path)
        print("Directory '%s' created successfully" % label_path)
    except OSError as error:
        print("Directory '%s' can not be created" % image_path)
        print("Directory '%s' can not be created" % label_path)

    (dimx, dimy, dimz) = test_patient_image.shape

    for slice_num in range(dimx):
        saveSlice(test_patient_image[slice_num],
                  test_patient_label[slice_num],
                  image_path, label_path, test_patient_iter,
                  image_name="image", label_name="mask", slice_num=str(slice_num))

    print("Testing image slices saved in '%s'" %image_path)
    print("Testing label slices saved in '%s'" %label_path)
    j+=1
    '''print("Patient details: ")
    print(np.max(test_patient_image), np.min(test_patient_image), test_patient_image.shape, type(test_patient_image))
    print(np.max(test_patient_label), np.min(test_patient_label), test_patient_label.shape, type(test_patient_label))'''
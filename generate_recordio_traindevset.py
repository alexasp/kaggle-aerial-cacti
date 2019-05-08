# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:39:12 2019

@author: alexa
"""

import os
import random
import math

# Create image list file, extension .lst
# integer_image_index \t labe2l_index \t path_to_image

# load labels
with open("data/train.csv") as training_labels_file:
    header = training_labels_file.readline()
    training_label_tuples = [line.strip().split(',') for line in training_labels_file.readlines()]

training_labels = {image_name:label for (image_name, label) in training_label_tuples}

print(header)
print(training_labels["0004be2cfeaba1c0361d39e2b000257b.jpg"])

# list all images in train set
images = os.listdir('data/train/train')
random.shuffle(images)
print(images[0])


# write cacti_training_data.lst
def write_lst_file(images, path):
    with open(path, 'w') as cacti_train_file:
        for i in range(len(images)):
            image = images[i]
            label = training_labels[image]
            print(f"{i}\t{label}\t{image}")
            cacti_train_file.write(f"{i}\t{label}\t{image}\n")


train_ratio=0.9
training_samples = math.floor(len(images) * 0.9)

write_lst_file(images[:training_samples], 'cacti_data_train.lst')
write_lst_file(images[training_samples:], 'cacti_data_val.lst')

# im2rec.py parameters: image.lst image_root_dir output.bin resize=256 label_width=4
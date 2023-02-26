import json
import cv2
import os
import matplotlib.pyplot as plt
import shutil

input_path = "D:\sonar\datasets\caltech-data\kenai-train"
output_path = "D:\sonar\datasets\caltech-yolo-data\kenai-train"

file = open("D:\sonar\datasets\caltech-coco-annotations\kenai-train\coco.json")
data = json.load(file)
file.close()

file_names = []

def load_images_from_folder(folder):
    count = 0
    for filename in os.listdir(folder)
        source = os.path.join(folder, filename)
        destination = f"{output_path}images/img{count}.jpg"

        try:
            shutil.copy(source, destination)
            print("File copied successfully.")
        except shutil.SameFileError:
            print("Source and destination represents the same file.")

        file_names.append(filename)
        count += 1

load_images_from_folder('train_images')
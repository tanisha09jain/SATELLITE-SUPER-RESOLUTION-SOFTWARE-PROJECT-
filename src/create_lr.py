import os
import cv2

HR_FOLDER = "../dataset/HR"
LR_FOLDER = "../dataset/LR"

os.makedirs(LR_FOLDER, exist_ok=True)

for filename in os.listdir(HR_FOLDER):

    input_path = os.path.join(HR_FOLDER, filename)

    image = cv2.imread(input_path)

    if image is None:
        continue

    height, width = image.shape[:2]

    new_width = width // 4
    new_height = height // 4

    lr_image = cv2.resize(
        image,
        (new_width, new_height),
        interpolation=cv2.INTER_AREA
    )

    name, extension = os.path.splitext(filename)

    output_filename = name + "_LR" + extension

    output_path = os.path.join(
        LR_FOLDER,
        output_filename
    )

    cv2.imwrite(output_path, lr_image)

    print("Created:", output_filename)

print("4× low-resolution images created successfully.")

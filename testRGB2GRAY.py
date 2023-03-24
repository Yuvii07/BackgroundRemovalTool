import os
import cv2

output_path = os.path.join(os.getcwd(), 'Output_Images')
final_path = os.path.join(os.getcwd(), 'Final_Images')

if not os.path.exists(final_path):
    os.mkdir(final_path)

for file_name in os.listdir(output_path):
    if file_name.endswith('.png'):
        img_path = os.path.join(output_path, file_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        height, width = img.shape[:2]
        new_height = int(height * 0.8)
        new_width = int(width * 0.8)
        img = cv2.resize(img, (new_width, new_height))
        save_path = os.path.join(final_path, file_name)
        cv2.imwrite(save_path, img)

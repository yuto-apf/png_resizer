from PIL import Image
import os


def resize_png(img_folder, new_width, new_height):
    files = [f for f in os.listdir(img_folder) if f.endswith('.png')]
    
    for file in files:
        img = Image.open(os.path.join(img_folder, file))
        resized_img = img.resize((new_width, new_height))
        resized_img.save(os.path.join(img_folder, f'new_{file}'))


def main():
    img_folder_path = './imgs'
    new_width  = int(input("New width >> "))
    new_height = int(input("New height >> "))

    resize_png(img_folder_path, new_width, new_height)
    print(f'Images are resized and saved to {img_folder_path}.')


if __name__ == '__main__':
    main()
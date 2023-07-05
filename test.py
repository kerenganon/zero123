import os
import numpy as np
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
from PIL import Image
import pathlib
from matplotlib.pyplot import imshow

# taken from https://stackoverflow.com/questions/43512615/reshaping-rectangular-image-to-square
def resize_image(image: Image, length: int) -> Image:
    """
    Resize an image to a square. Can make an image bigger to make it fit or smaller if it doesn't fit. It also crops
    part of the image.

    :param image: Image to resize.
    :param length: Width and height of the output image.
    :return: Return the resized image.
    """

    """
    Resizing strategy : 
     1) We resize the smallest side to the desired dimension (e.g. 1080)
     2) We crop the other side so as to make it fit with the same length as the smallest side (e.g. 1080)
    """
    if image.size[0] < image.size[1]:
        # The image is in portrait mode. Height is bigger than width.

        # This makes the width fit the LENGTH in pixels while conserving the ration.
        resized_image = image.resize((length, int(image.size[1] * (length / image.size[0]))))

        # Amount of pixel to lose in total on the height of the image.
        required_loss = (resized_image.size[1] - length)

        # Crop the height of the image so as to keep the center part.
        resized_image = resized_image.crop(
            box=(0, required_loss / 2, length, resized_image.size[1] - required_loss / 2))

        # We now have a length*length pixels image.
        return resized_image
    else:
        # This image is in landscape mode or already squared. The width is bigger than the heihgt.

        # This makes the height fit the LENGTH in pixels while conserving the ration.
        resized_image = image.resize((int(image.size[0] * (length / image.size[1])), length))

        # Amount of pixel to lose in total on the width of the image.
        required_loss = resized_image.size[0] - length

        # Crop the width of the image so as to keep 1080 pixels of the center part.
        resized_image = resized_image.crop(
            box=(required_loss / 2, 0, resized_image.size[0] - required_loss / 2, length))

        # We now have a length*length pixels image.
        return resized_image


def main():
    # folder = 'zero123/views_whole_sphere/Milan_Cathedral/images/'
    folder = 'zero123/views_whole_sphere/Milan_Cathedral/square_centered_images/'
    # new_folder = folder.replace('images', 'square_centered_images')
    # npy_files = [f for f in listdir(folder) if isfile(join(folder, f)) and f.endswith(".npy")]
    image_files = [f for f in listdir(folder) if isfile(join(folder, f)) and not f.endswith(".npy")]
    # for npy_file in npy_files:
    #     old_name = folder + '/' + npy_file
    #     new_name = folder + '/npys/' + npy_file
    #     os.rename(old_name, new_name)
    for image_file in image_files:
        img = plt.imread(folder + image_file)
        if img.ndim < 3:
            print("******* KEREN ******* 2X2 img: " + image_file + "with dimention: " + str(img.ndim))
    #     img.show
    #     square_centered_image = resize_image(img, min(img.height, img.width))
    #     square_centered_image.show
        # new_path = new_folder + image_file.split('.')[0] + '.png'
        # new_path = new_folder + image_file
        # square_centered_image.save(new_path)
            # old_name = folder + '/' + image_file
            # new_name = folder + '/images/' + image_file
            # os.rename(old_name, new_name)
    # filename = 'zero123/views_whole_sphere/0a00b69cc98b45ab9fdd02cf86729909/001.npy'
    # RT = np.load(filename)
    # print('RT from npy: ' + str(RT))
    # # cond_RT = np.load(filename)
    # R, T = RT[:3, :3], RT[:, -1]
    # print('R: ' + str(R))
    # print('T: ' + str(T))


if __name__ == "__main__":
    main()
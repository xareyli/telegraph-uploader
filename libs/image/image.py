from PIL import Image
import os
import shutil


def scaleImage(path, savePath, scale_ratio):
    img = Image.open(path)
    resized_width  = int(img.size[0] * scale_ratio)
    resized_height = int(img.size[1] * scale_ratio)
    img = img.resize((resized_width, resized_height), Image.ANTIALIAS)

    path_split = os.path.basename(path).split('.')
    image_extension = path_split.pop()
    resized_image_path = savePath + '.'.join(path_split) + '.' + image_extension

    img.save(resized_image_path)

    return resized_image_path


def getImageDimensions(path):
    img = Image.open(path)

    return img.size


def getImageExtension(path):
    path_split = path.split('.')
    return path_split.pop()


def compressImage(fullpath, save_dir, dimensions, size):
    """Fit image into needed stats

    Accepts an image and transforms it in order to fit given stats

    """
    is_processed = False
    image_dimensions = getImageDimensions(fullpath)

    if (image_dimensions[1] > dimensions[1]) or (image_dimensions[0] > dimensions[0]):
        is_processed = True
        fullpath = fitImageIntoDimensions(fullpath, save_dir, image_dimensions, dimensions)

    is_size_small_enough = os.stat(fullpath).st_size / (1024 * 1024) < size

    if not is_size_small_enough:
        is_processed = True
        fullpath = shrinkImageUntilSizeSmallEnough(fullpath, save_dir, size)

    if not is_processed:
        shutil.copy(fullpath, save_dir)


def fitImageIntoDimensions(image_path, save_dir, current_dimensions, dimensions_needed):
    to_fit_height_scale_ratio = (dimensions_needed[1] * 100 / current_dimensions[1]) / 100
    to_fit_width_scale_ratio = (dimensions_needed[0] * 100 / current_dimensions[0]) / 100

    scale_ratio = min(to_fit_height_scale_ratio, to_fit_width_scale_ratio)

    return scaleImage(image_path, save_dir, scale_ratio)


def shrinkImageUntilSizeSmallEnough(image_path, save_dir, size_needed):
    original_filepath = image_path
    is_size_small_enough = os.stat(image_path).st_size / (1024 * 1024) < size_needed
    scale_ratio = .75
    # if the image is more than size_needed Mb, resize it
    while not is_size_small_enough:
        image_path = scaleImage(image_path, save_dir, scale_ratio)

        is_size_small_enough = os.stat(image_path).st_size / (1024 * 1024) < size_needed

        if not is_size_small_enough:
            os.remove(image_path)
            scale_ratio -= .05
            image_path = original_filepath

    return image_path

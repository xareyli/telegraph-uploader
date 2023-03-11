from PIL import Image


def scaleImage(path, scale_ratio):
    img = Image.open(path)
    resized_width  = int(img.size[0] * scale_ratio)
    resized_height = int(img.size[1] * scale_ratio)
    img = img.resize((resized_width, resized_height), Image.ANTIALIAS)

    path_split = path.split('.')
    image_extension = path_split.pop()
    resized_image_path = '.'.join(path_split) + '.thumbnail.' + image_extension

    img.save(resized_image_path)

    return resized_image_path


def getImageExtension(path):
    path_split = path.split('.')
    return path_split.pop()

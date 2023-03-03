from PIL import Image


def scaleImage(path):
    img = Image.open(path)
    resized_width  = int(img.size[0] * 0.75)
    resized_height = int(img.size[1] * 0.75)
    img = img.resize((resized_width, resized_height), Image.ANTIALIAS)

    path_split = path.split('.')
    image_extension = path_split.pop()
    resized_image_path = '.'.join(path_split) + '.thumbnail.' + image_extension

    img.save(resized_image_path)

    return resized_image_path

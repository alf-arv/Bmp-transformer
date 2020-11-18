from PIL import Image
import os

__author__ = 'alf-arv'


def remove_alpha_layer(img: Image) -> Image:
    """
    Function for removing transparency layer if there is one
    :param img: Image to be stripped of its alpha layer
    :return: Image in three channels (R,G,B)
    """
    if len(img.split()) == 4:
        # prevent IOError: cannot write mode RGBA as BMP
        r, g, b, a = img.split()
        img = Image.merge("RGB", (r, g, b))
        return img
    else:
        return img


def transform_picture_to_bmp(image_path_in: str,
                             image_path_out: str = False,
                             width: int = False,
                             height: int = False,
                             scale: float = '',
                             use_original_dimensions: bool = False) -> Image:
    """
    Function for transforming the provided picture to bmp and saving it to
    the output path if provided. If not, the transformed image is saved in
    the same path as the input.

    :param image_path_in: Path to the image to transform to bmp
    :param image_path_out: Output path to save the transformed image to
    :param width: Specified width in pixels
    :param height: Specified height in pixels
    :param scale: Specified scale
    :param use_original_dimensions: False if specified dimensions should be used, True otherwise
    :return: True if successful transform, False otherwise
    """

    # Prevent misusage
    if use_original_dimensions and (width or height):
        return False

    if image_path_in:
        # Create an Image object
        img = Image.open(remove_alpha_layer(image_path_in))

        if use_original_dimensions:
            width = img.width
            height = img.height

        if scale == '':
            scale = 1

        # Resize
        resized_image = img.resize((int(float(scale) * float(width)), int(float(scale) * float(height))))

        # Save image to disk
        if image_path_out:
            resized_image.save(os.path.join(image_path_out,
                                            str('.'.join(image_path_in.split(".")[:-1])).split("/")[-1] + '_tr.bmp'))
        else:
            resized_image.save(str('.'.join(image_path_in.split(".")[:-1])) + '_tr.bmp')
        return True
    return False

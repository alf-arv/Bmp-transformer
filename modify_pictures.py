from PIL import Image
import os

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
        #img.save(file_out)
        return img
    else:
        return img

def transform_picture_to_bmp(image_path_in: str, image_path_out: str=False) -> Image:
    """
    Function for transforming the provided picture to bmp and saving it to
    the output path if provided. If not, the transformed image is saved in
    the same path as the input.

    :param image_path_in: Path to the image to transform to bmp
    :param image_path_out: Output path to save the transformed image to,
    :return: True if successful transform, False otherwise
    """
    if image_path_in:
        # Create an Image object
        img = Image.open(image_path_in)

        # Resize
        resizedImage = img.resize((100, 100)) # change this resolution

        # Save image to disk
        if image_path_out:
            resizedImage.save(os.path.join(image_path_out, 'pelican_modified.bmp'))
        else:
            resizedImage.save(str('.'.join(image_path_in.split(".")[:-1]))+'_tr.bmp')
        return True
    return False

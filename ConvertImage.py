from wand.image import Image
from Log import Log

class ConvertImage:
    def convertImage(self, path_image, name_image, new_name, format):
        log = Log()
        name_method = self.convertImage.__name__

        try:
            with Image(filename=f"{path_image}/{name_image}") as img:
                img.format = format
                img.save(filename=f"{path_image}/new/{new_name}.{format}")

            message = f"Success to run {name_method}"

            return True, message, name_method
        except:
            message = f"Erro to run {name_method}"

            return False, message, name_method
    
    def validateFormat(self, format):
        format_support = ["jpeg", "png", "tiff", "bmp", "esp"]
        name_method = self.validateFormat.__name__

        if format in format_support:
            message = f"Success to run {name_method}"

            return True, message, name_method
        else:
            message = f"Error to run {name_method}"

            return False, message, name_method

import sys
import os

from Files import Files
from Log import Log
from ConvertImage import ConvertImage

v1 = sys.argv[0] #name script
pathFile = sys.argv[1] #path files
format = sys.argv[2] #format

lenght = len(sys.argv)
file = Files(pathFile)
log = Log()
convertImage = ConvertImage()

format_support = ["jpeg", "png", "tiff", "bmp", "esp"]
count = 1

try:
    it_worked, message, name_method, list_files = file.listDir()

    if it_worked:
        log.info(message, name_method)

        it_worked, message, name_method = file.createDir()

        if it_worked:
            log.info(message, name_method)

            it_worked, message, name_method = convertImage.validateFormat(format)

            if it_worked:
                log.info(message, name_method)

                for element in list_files:
                    if element[-4:] == ".png" or element[-5:] == ".jpeg" or element[-4:] == ".bmp" or element[-4:] == ".eps" or element[-5:] == ".webp":
                        path_image = f"{pathFile}"
                        it_worked, message, name_method = convertImage.convertImage(path_image, element, count, format)

                        if it_worked:
                            count += 1

                            log.info(message, name_method)
                        else:
                            log.error(message, name_method)
            else:
                log.error(message, name_method)
        else:
            log.error(message, name_method)
    else:
        log.error(message, name_method)
except:
    log.error("Error to run main", "main")
from os import listdir
from os.path import isfile, join
import os

class Files:
    def __init__(self, path):
        self.path = path

    def listDir(self):
        name_method = listdir.__name__

        try:
            only_files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
            message = "Success to run " + name_method

            return True, message, name_method, only_files
        except:
            message = "Error to run " + name_method
            
            return False, message, name_method, ""
    
    def createDir(self):
        name_method = self.createDir.__name__

        try:
            name_dir = "new"

        
            if os.path.exists(self.path):
                message = "Directory already exists"
                return True, message, name_method
            else:
                path = os.path.join(self.path, name_dir)
                os.mkdir(path)
                message = f"Success to run {name_method}"

                return True, message, name_method
        except:
            message = f"Erro to run {name_method}"
            
            return False, message, name_method
            
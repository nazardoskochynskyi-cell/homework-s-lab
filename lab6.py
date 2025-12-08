import os
import logging
import json

# ==============ЛОГУВАННЯ===================
class MyFileNotFoundError(Exception):
    pass
class FileCorrupted(Exception):
    pass
def logged(exception_type, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_type as e:
                logger = logging.getLogger("AppLogger")
                if logger.hasHandlers():
                    logger.handlers.clear()
                if mode == "file":
                    handler = logging.FileHandler("app_errors.log", encoding='utf-8')
                    
                formatter = logging.Formatter('%(asctime)s - ERROR - %(message)s')
                handler.setFormatter(formatter)
                logger.addHandler(handler)

                logger.error(f"Method '{func.__name__}' failed: {e}")
                return f"[LOGGED] Error handled ({mode})"
        return wrapper
    return decorator
# ==========================================
class FileOperations:
    def __init__(self, name_1, write_mode='w', read_mode='r', append_mode='a'):
        self.name_1 = name_1
        self.write_mode = write_mode
        self.read_mode = read_mode
        self.append_mode = append_mode

    @logged(MyFileNotFoundError, mode="file")
    def read_file(self):
        if not os.path.exists(self.name_1):
            raise MyFileNotFoundError(f"File '{self.name_1}' not found!")    
        with open(self.name_1, self.read_mode, encoding='utf-8') as f:
                content = json.load(f)
                return content
        return(f"--ERROR: File {self.name_1} not found--")
    
    @logged(FileCorrupted, mode="file")    
    def write_file(self, text={"message": "hello from function"}):
        try:
            with open(self.name_1, self.write_mode, encoding='utf-8') as f:
                json.dump(text, f, indent=4)
            return("File written successfully")
        except Exception as e:
            raise FileCorrupted(f"cannot write to file '{self.name_1}': {e}")   

    @logged(FileCorrupted, mode="file")   
    def append_file(self, text):
        try:
            data = []
            if os.path.exists(self.name_1):
                with open(self.name_1, self.read_mode, encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                    except:
                        data = []
            
            if not isinstance(data, list):
                data = [data]
            
            data.append(text)

            with open(self.name_1, self.write_mode, encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            return("File appended successfully")
        except Exception as e:
            raise FileCorrupted(f"cannot append to file '{self.name_1}': {e}")

    @property
    def filename(self):
        return self.name_1
    
    @filename.setter
    def filename(self, name_2):
        self.name_1 = name_2
        print(f"New file: {name_2}")
    
    @property
    def fileappend(self):
        return self.append_mode
    
    @fileappend.setter
    def fileappend(self, text):
        self.append_mode = text
        print(f"New append mode: {text}")

if __name__ == "__main__":
    
    print(f"_File location {os.getcwd()}_")

    file_check = "new_name.json"
    if os.path.exists(file_check):
        os.remove(file_check)
        print(f"{file_check} is removed!")

    file_ops = FileOperations('old_name.json')

    print(file_ops.read_file()) 
    
    file_ops.filename = "new_name.json"
    print(file_ops.write_file({"id": 1, "user": "First"}))
    print(file_ops.append_file({"id": 2, "user": "Second"}))
    print(file_ops.read_file())
    print(f"{file_ops.filename}--current filename")
    
    if not os.path.exists("test_folder"): os.mkdir("test_folder")
    
    file_ops.filename = "test_folder" 
    
    print(f"Write error test: {file_ops.write_file({'test': 'text'})}")
    
    os.rmdir("test_folder")
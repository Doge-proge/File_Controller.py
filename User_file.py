import os
import shutil

class FileRepository:
    def __init__(self, filename) -> None:
        self.__f_name = filename
        self.__rline = 1
        with open(self.__f_name, "w"):
            pass

    def read_lines(self, line):
        self.__rline = line
        with open(self.__f_name, "r") as f:
            for i in range(0,self.__rline):
                data = f.readline()
                print(data)
    
    def write_lines(self, text):
        with open(self.__f_name, "a") as f:
            if type(text) in (tuple, list, set):
                for i in text:
                    f.write(str(i) + "\n")
            else:
                f.write(str(text) + "\n")

    def read(self,bytes = 0):
        with open(self.__f_name, "r") as f:
            if bytes:
                print(f.read())
            else:
                print(f.read(bytes))
    
    def write(self, text):
        with open(self.__f_name, "a") as f:
            f.write(str(text))
        
    def delete(self):
        print("The file has been deleted !")
        print("Quitting the program ...")
        os.remove(self.__f_name)
        quit()

    def rename(self, new_name):
        os.rename(self.__f_name, new_name)
        self.__f_name = new_name

    def copy(self, new_name):
        shutil.copy(self.__f_name, new_name)

    def delete_word(self, element_to_del):
        with open(self.__f_name, "r+") as f:
            data = f.read().split()
            index = 0
            for i in data:
                if i == element_to_del:
                    del data[index]
                    break
                index += 1
        with open(self.__f_name, "w") as f:
            for i in data:
                f.write(i)
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

    def replace(self, st_str, sec_str):
        with open(self.__f_name, "r") as f:
            data = f.read().split()
            st_ind = []
            sec_ind = []
            index = 0
            for i in data:
                if i == st_str:
                    st_ind.append(index)
                elif i == sec_str:
                    sec_ind.append(index)
                index += 1

            if len(st_ind) == len(sec_ind):
                for i in range(0,len(st_ind)):
                    data[st_ind[i]], data[sec_ind[i]] = data[sec_ind[i]], data[st_ind[i]]
            elif len(st_ind) < len(sec_ind):
                for i in range(0,len(st_ind)):
                    data[st_ind[i]], data[sec_ind[i]] = data[sec_ind[i]], data[st_ind[i]]
            elif len(st_ind) > len(sec_ind):
                for i in range(0,len(sec_ind)):
                    data[st_ind[i]], data[sec_ind[i]] = data[sec_ind[i]], data[st_ind[i]]

        with open(self.__f_name, "w") as f:
            for i in data:
                f.write(i)

    def search(self, place) -> bool:
        with open(self.__f_name, "r") as f:
            data = f.read().split()
            for i in data:
                if place == i:
                    return True
            return False
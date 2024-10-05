from User_file import FileRepository

def User_int():
    print("Which function do you want to use ?")
    print("1. Write lines")
    print("2. Read lines")
    print("3. Read")
    print("4. Write")
    print("5. Delete")
    print("6. Copy")
    print("7. Rename")
    print("8. Delete a word")
    print("9. Replace")
    print("10. Search")

def usage(func: int, o1: FileRepository):
    match func:
        case 1:
            text = input("Enter the text you want to append: ")
            o1.write_lines(text)
        case 2:
            line = int(input("Enter a number of lines you want to read: "))
            o1.read_lines(line)
        case 3:
            ch = int(input("Enter a number of characters u wanna read: "))
            o1.read(ch)
        case 4:
            text = input("Enter a text you want to continue yours with: ")
            o1.write(text)
        case 5:
            o1.delete()
        case 6:
            new_name = input("Enter a new file's name: ")
            o1.copy(new_name)
        case 7:
            new_name = input("Enter new name: ")
            o1.rename(new_name)
        case 8:
            element_to_del = input("Enter the element you want to delet from the file: ")
            o1.delete_word(element_to_del)
        case 9:
            place1 = input("Enter 1 word you wanna replace in the file: ")
            place2 = input("Enter 2 word you wanna replace with in the file: ")
            o1.replace(place1, place2)
        case 10:
            place = input("Enter a word you wanna find in the file: ")
            print(o1.search(place))

name = input("enter the name of the file")
o1 = FileRepository(name)
n = 1
func = 0

while n:
    User_int()
    try:
        func = int(input("Type the function you want to use: "))
    except ValueError:
        print("Invalid Value !")
    except Exception:
        print("Invalid !")
    usage(func, o1)
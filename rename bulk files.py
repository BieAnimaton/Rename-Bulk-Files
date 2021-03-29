import os

def main():
    path = raw_input("Enter the diretory to renaming files: ")
    path = path + "/"
    new_name = raw_input("Enter the new Name for files: ")

    i = 0
    for filename in os.listdir(path):
        file_extension = filename.split(".")
        my_dest = new_name + str(i) + "." + file_extension[1]
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1
    print("Files renamed to {}.{}".format(new_name, file_extension[1]))

if __name__ == '__main__':
    main();
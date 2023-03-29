import os
import sys
from util import get_catalogs,get_files

#a)
def print_all_catalogs():
    for catalog in get_catalogs():
        print(catalog)


#b)
def print_all_files():
    for catalog in get_catalogs():
        print("    ",catalog,":")
        for file in get_files(catalog):
            print(file)




if __name__ == "__main__":
    print_all_files()




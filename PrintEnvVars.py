import os #interakcja z systemem operacyjnym
import sys
from utils import print_dict,create_filtered_env_vars_dict

def print_all_env_vars():
    print_dict(os.environ.copy())


#a)
def print_filtered_env_vars(filters_list):
    try:
        print_dict(create_filtered_env_vars_dict(filters_list))
    except ValueError:
        print("did not receive any arguments!")


# b)
def print_filtered_env_vars_sorted(filters_list):
    try:
        dict = create_filtered_env_vars_dict(filters_list)
        for key,value in sorted(dict.items()):
            print(key,":",value)
    except ValueError:
        print("did not receive any arguments!")


if __name__ == "__main__":
    print_filtered_env_vars_sorted(sys.argv)




import os
import sys


#Dictonaires - task 1

def print_dict(dict):
    for key,value in dict.items():
        print(key,":",value,"\n")


def create_filtered_env_vars_dict(filters_list):    #raises value error if no args
    env_vars  = os.environ.copy()  #dict of all environment variables
    if len(sys.argv)>1:
        return {variable: value for variable, value in env_vars.items() if variable in filters_list}
    raise ValueError("did not receive arguments")




#Paths - task 2

def get_path():
    return os.environ.copy()["PATH"]

def get_catalogs():
    return [catalog for catalog in get_path().split(";")]

def get_files(path):
    return [file for file in os.listdir(path)]
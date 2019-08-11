import os

def read_file():
    #file_path = os.path.join(os.path.split(os.getcwd())[0], "configfiles", "data.yml")
    file_path = os.path.join(os.getcwd(), "amazon", "configfiles", "data.yml")
    with open(file_path) as file:
        data = file.readlines()
        return data

import os

class Sorting():
    def __init__(self, path: str, interval: int, type_of_file: str, reverse: bool):
        if reverse==True:
            index = -1
        elif reverse==False:
            index= 1
        first = 1
        second = 1
        for file in os.listdir(path)[::index]:
            name = f'{first}_{second}'
            old_name = f'{path}\{file}'
            new_name = f'{path}\{name}.{type_of_file}'
            os.rename(old_name, new_name)
            second+=1
            if second>interval:
                first+=1
                second=1
            

    
    
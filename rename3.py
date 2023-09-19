import os 


def rename(dir):
    count = 1
    for file in os.listdir(dir):
        
        old_path = os.path.join(dir, file)
        new_names = f'0{count}.png'
        new_path = os.path.join(dir, new_names)
        os.rename(old_path,new_path)
        count+=1

        
directory = r''

# Quando for passar seu diretório 

change = rename(directory)
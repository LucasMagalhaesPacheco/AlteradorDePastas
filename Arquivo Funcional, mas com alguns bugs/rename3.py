import os 


def rename(dir):
    # Contador para começar as imagens do zero.
    count = 0
    # Utilizamos a biblioteca listdir para contar os arquivos dentro da paqsta
    for file in os.listdir(dir):
    # Aqui definimos quais são os antigos parâmetros que a imagem tinha tanto a imagem com seu file, quanto seu repositório com dir e o file.
        old_path = os.path.join(dir, file)
    # Aqui definimos como a imagem será renomeada e colocamos se vai ser Png, jpg, etc
        new_names = f'{count}.png'
    # Aqui criamos o nosso novo caminho, diferente do antigo, colocamos em vez de file, os new names
        new_path = os.path.join(dir, new_names)
    # Aqui por fim colocamos a substituição do antigo pelo novo
        os.rename(old_path,new_path)
    # Fazemos o loop dá volta até o último arquivo ser lido
        count+=1

        
directory = r''


change = rename(directory)
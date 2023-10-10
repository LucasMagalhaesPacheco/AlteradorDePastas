import os

def rename(dir, use_existing_numbers=True):
    # Contador que vai começar do zero
    
    # Inicialmente começamos o nosso código usando o sorted para alinhar em ordem crescente
    # os.listdir(dir) pegamos os arquivos do diretório
    # Aqui então na função Lambda mostramos que a ordem que ele tem que seguir é usando o gettime
    # Ou seja a ordem inicial que foi baixado os arquivos

    files = sorted(os.listdir(dir), key=lambda x: os.path.getmtime(os.path.join(dir, x)))
    existing_numbers = set() # Uma variável que vai guardar o número de um conjunto de arquivos, caso eles existam, usado no if
    count = 0
    
    # Aqui começamos uma função opcional, para o código considerar ou não a existência já de arquivos numerados
    if use_existing_numbers:
         # Agora temos um loop que percorre todos os arquivos
        for file in files:  
        # fazemos o contador inicial
        # Aqui inicialmente vemos se os arquivos são arquivos ou diretórios que são pastas etc
           if os.path.isfile(os.path.join(dir, file)):
            # Aqui para sabermos a divisão dos arquivos a partir de ponto.
            # Ou seja, se o arquivo é 123.man.txt
            # ele vai ficar 123 . man . txt
            parts = file.split('.')
            # Aqui começamos a primeira parte do código para ele ler arquivos que são números
            # Até mesmo começando por 0
            if len(parts) > 1 and (parts[0].isdigit() or parts[0] == '0'):
                # Aqui adicionamos o número em um conjunto de Python
                existing_numbers.add(int(parts[0]))
                
    
    # Após todos esses passos começamos o loop de alteração
    for file in files:
                             
     # Essa linha de código ela verifica se o arquivo em questão é um diretório
     # No caso uma pasta, caso for ele continua para o próximo arquivo e pula ele.
     if os.path.isdir(os.path.join(dir, file)):
            continue
     # Essa linha de código separa por meio de um array a extensão do arquivo, se é JPG, PNG, mp4
     # esse sendo o indice 1, utilizando splittext
     file_extension = os.path.splitext(file)[1]
     # Aqui definimos o novo nome do arquivo
     new_name = f'{count}{file_extension}'

     # Aqui fazemos um while para ver se já existe arquivos numerados, assim dando nomes únicos aos demais e pulando ele.
     # Verificando se essa condição é verdadeira
     if use_existing_numbers:
        while new_name in existing_numbers:
           count += 1
           new_name = f'{count}{file_extension}'
     # Aqui definimos qual era o nome anterior dos arquivos das pastas, sendo o primeiro parâmetro
     # O nome da pasta e o segundo parâmetro o arquivo
     old_path = os.path.join(dir, file)
     #Aqui a mesma coisa só muda que o segundo parâmetro é o novo nome do arquivo
     new_path = os.path.join(dir, new_name)
     # Por fim chamamos a função rename da biblioteca para executar o código
     # Por sua vez ela funciona bem se os nomes não forem semelhantes, agora vamos adicionar um try para ele testar um tipo de código
     # Se não para ele testar uma excessão.
     try:
        os.rename(old_path, new_path)
        #Utilizamos a função fileExistisError se der esse problema
     except FileExistsError:
        # Se um arquivo com o novo nome já existe, adicione um número ao nome
         count += 1
         new_name = f'{count}{file_extension}'
         new_path = os.path.join(dir, new_name)
         os.rename(old_path, new_path)
     
     # E finalmente repetimos isso até o código preencher todas as imagens
     count += 1

    
    print("Renomeado com sucesso")

 

# Aqui tem que se lembrar de colocar a \ para chegar mais direito no diretório
directory = r''

change = rename(directory, use_existing_numbers=False)
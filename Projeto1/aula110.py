import os
from itertools import count

counter = count()

caminho = os.path.join('C:\\Users', 'user', 'directory', 'documents',\
                                                      'file')

for root, dirs, files in os.walk(caminho):
    
    the_counter = next(counter)
    print(the_counter, root)

    
    
    for dir in dirs:
        
        print('   ', dir)
        

        for file in files:
            
            print('      ', file)
            
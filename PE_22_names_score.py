from string import ascii_lowercase as alpha

nameValue = lambda name: sum([alpha.index(l)+1 for l in name.lower()])

totalValue = lambda names: sum([(nameValue(name) * (i+1)) for i, name in enumerate(names)])

def extractNames(file_location, mode='r'):
    try:
        names = ''
        with open(file_location, mode) as file:
            names = [name.strip('"') for name in file.readline().split(',')]
        names.sort()
    except FileNotFoundError:
        print(f'No se pudo abrir el archivo {file_location}')
    except:
        print('Ocurrio un error inesperado')
    return names


def __main__():
    
    archivo = 'names.txt'
    names = extractNames(archivo)
    if names != '':
        names_score = totalValue(names)
        print(f'El valor total de los nombres es {names_score}')
    else:
        print('Verifique la existencia del archivo e intente de nuevo.')

if __name__ == "__main__":
    __main__()

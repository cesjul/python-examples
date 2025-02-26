#exercicio
import json

lista_tarefas = []
lista_desfazer = []
lista_refazer = []
i = 0
caminho = 'aula76.json'


def ler_json(lista, caminho):
    dados = []
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
           dados = json.load(arquivo)

    except FileNotFoundError:
        salvar_json(lista, caminho)
    
    return dados

        
def salvar_json(lista, caminho):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(lista,
                  arquivo,
                  indent=2,
                  ensure_ascii= False
                  )

while True:
   
    print('Comandos: listar, desfazer ou refazer')
    entrada = input('Digite uma tarefa ou comando: ')
    print()

    if entrada == 'listar':
        if lista_tarefas == []:
           lista_tarefas = ler_json(lista_tarefas, caminho)

        print('Tarefas:')
        for n, item in enumerate(lista_tarefas, start=1):
            print(n, item, sep=' - ')
        print()

    elif entrada == 'desfazer':
        lista_tarefas.pop()
        i -= 1
        print('Tarefas:')
        for n, item in enumerate(lista_tarefas, start=1):
            print(n, item)
        print()

    elif entrada == 'refazer':

        if lista_tarefas != lista_refazer:
            lista_tarefas.append(lista_refazer[i])
            i += 1
        else:
            print('Não há o que refazer!\n')
            continue

        print('Tarefas:')
        for n, item in enumerate(lista_tarefas, start=1):
            print(n, item)
        print()

    else:
        lista_tarefas.append(entrada)
        lista_desfazer.append(entrada)
        lista_refazer.append(entrada)
        i = len(lista_refazer)
        
    salvar_json(lista_tarefas, caminho)

    
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
# import os


# def listar(tarefas):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para listar')
#         return

#     print('Tarefas:')
#     for tarefa in tarefas:
#         print(f'\t{tarefa}')
#     print()


# def desfazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para desfazer')
#         return

#     tarefa = tarefas.pop()
#     print(f'{tarefa=} removida da lista de tarefas.')
#     tarefas_refazer.append(tarefa)
#     print()
#     listar(tarefas)


# def refazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas_refazer:
#         print('Nenhuma tarefa para refazer')
#         return

#     tarefa = tarefas_refazer.pop()
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()
#     listar(tarefas)


# def adicionar(tarefa, tarefas):
#     print()
#     tarefa = tarefa.strip()
#     if not tarefa:
#         print('Você não digitou uma tarefa.')
#         return
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()
#     listar(tarefas)


# tarefas = []
# tarefas_refazer = []

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')

#     comandos = {
#         'listar': lambda: listar(tarefas),
#         'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
#         'refazer': lambda: refazer(tarefas, tarefas_refazer),
#         'clear': lambda: os.system('clear'),
#         'adicionar': lambda: adicionar(tarefa, tarefas),
#     }
#     comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
#         comandos['adicionar']
#     comando()

#     # if tarefa == 'listar':
#     #     listar(tarefas)
#     #     continue
#     # elif tarefa == 'desfazer':
#     #     desfazer(tarefas, tarefas_refazer)
#     #     listar(tarefas)
#     #     continue
#     # elif tarefa == 'refazer':
#     #     refazer(tarefas, tarefas_refazer)
#     #     listar(tarefas)
#     #     continue
#     # elif tarefa == 'clear':
#     #     os.system('clear')
#     #     continue
#     # else:
#     #     adicionar(tarefa, tarefas)
#     #     listar(tarefas)
#     #     continue
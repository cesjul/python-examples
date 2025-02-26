from argparse import ArgumentParser

parse = ArgumentParser()
parse.add_argument('-b', '--basic',
                   help='Exibe o que for enviado',
                #    type= str,
                   metavar= 'STRING',
                #    default= 'Nenhum valor',
                   required=False,
                #    nargs= '+'
                   action='append' 
                   )
args = parse.parse_args()

if args.basic is None:
    print(f'Envie um argumento para {args.basic=}')
    print(args.basic)
else:
    print(args.basic)
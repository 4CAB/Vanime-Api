from api import Vanime
from utils import args
from utils.formatters import formatter


def main():
    vanime = Vanime()
    argv = args.args()

    if argv.buscar:
        return vanime.search(value=argv.buscar)
    elif argv.info:
        return vanime.get_anime(slug=argv.info)
    elif argv.capitulo:
        if argv.numero:
            return vanime.get_capitulo(slug=argv.capitulo, numero=str(argv.numero),
                                       check=argv.check)
        else:
            return formatter(data='El parámetro :c requiere del parámetro :n\n    |    \
                             vanime.py :c one-piece-tv :n 1000')
    else:
        return formatter(data='Intenta\n    |    vanime.py :h')


if __name__ == '__main__':
    print(main())
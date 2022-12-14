#!/usr/bin/env python
from Vanime.api import Vanime
from Vanime.utils import args
from Vanime.utils.formatters import formatter
from rich import print


def main():
    vanime = Vanime()
    argv = args.args(standalone_mode=False)

    if argv['buscar']:
        return vanime.search(value=argv['buscar'])
    elif argv['info']:
        return vanime.get_anime(slug=argv['info'])
    elif argv['capitulo']:
        if argv['numero']:
            return vanime.get_capitulo(slug=argv['capitulo'], numero=str(argv['numero']),
                                       check=argv['check'])
        else:
            return formatter(data='El parámetro [bold red]:c[/] \
requiere del parámetro [bold red]:n[/]\n\
    vanime :c one-piece-tv :n 1000')
    else:
        return formatter(data='Intenta\n    vanime :h')


if __name__ == '__main__':
    print(main())

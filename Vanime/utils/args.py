import argparse


def args():
    parser = argparse.ArgumentParser(prefix_chars=':')
    parser.add_argument(':b',
                        help='Busca un anime. | :b "black clover"',
                        dest='buscar')

    parser.add_argument(':i',
                        help='Obtiene información de un anime. | :i "slug"',
                        dest='info')

    parser.add_argument(':c',
                        help='Obtiene el capítulo de un anime. | :c "slug" :n 1',
                        dest='capitulo')

    parser.add_argument(':n',
                        help='Indica número de capítulo. Requerido para :c. | :n 1',
                        dest='numero')

    parser.add_argument(':check',
                        help='Devuelve sólo los enlaces que funcionen. Opcional de :c. \
                        | :check',
                        nargs='?',
                        const=True,
                        dest='check')

    args = parser.parse_args()
    return args

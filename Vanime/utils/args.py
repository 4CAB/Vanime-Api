import click


@click.option(':b', 'buscar', help='Busca un anime. | :b "black clover"')
@click.option(':i', 'info', help='Obtiene información de un anime. | :i "slug"')
@click.option(':c', 'capitulo', help='Obtiene el capítulo de un anime. | :c "slug" :n 1')
@click.option(':n', 'numero', help='Indica número de capítulo. Requerido para :c. | :n 1')
@click.option(':check', 'check', default=True,
              help='Devuelve sólo los enlaces que funcionen. Opcional de :c. | :check')

@click.command()
@click.pass_context
def args(ctx, *args, **kwargs):
    return kwargs
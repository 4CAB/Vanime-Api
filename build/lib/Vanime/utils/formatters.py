from rich.console import group
from rich.panel import Panel


@group()
def formatter_list(data):
    for i in data:
        data = ""

        for key, value in i.items():
            data += f"[bold red]{key}[/]: [italic]{value}[/]\n"

        yield Panel(data, title=i['Titulo'])


def formatter(data):
    return Panel(data, title='Vanime')


def anime_info_formatter(data) -> str:
    generos = ""
    for i in data['Generos']:
        for key in i:
            generos += f"\n    [bold red]{key}[/]: [italic]https://animeflv.net{i[key]}[/]"

    content = '\n'.join(f'[bold red]{i}[/]: [italic]{data[i]}[/]'
                        for i in data if i != 'Generos')
    content += f'\n[bold red]Generos[/]: [italic]{generos}[/]'

    return Panel(content, title='Vanime')


def capitulo_info_formatter(data) -> str:
    return formatter_list(data)

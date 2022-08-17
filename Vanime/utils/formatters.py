def formatter(data) -> str:
    content = f"""
    ------------------------
    |{data}
    ------------------------
    """

    return content


def anime_info_formatter(data) -> str:
    generos = ""
    for i in data['Generos']:
        for key in i:
            generos += f"\n    |\t{key}: https://animeflv.net{i[key]}"

    content = '\n    |'.join(f'{i}: {data[i]}' for i in data if i != 'Generos')
    content = content + f'\n    |Generos: {generos}'

    return formatter(data=content)


def capitulo_info_formatter(data) -> str:
    content = ""
    for i in data:
        content += formatter(data='\n    |'.join(f"{key}: {value}" for key, value in i.items()))

    return content

from json import dump


def to_json(results: dict, output: str = "output.json"):
    """
    Salva os resultados da detecção em um Arquivo JSON
    
    Args:
        - result: dict
        - output: str
    """
    
    with open(output, "w", encoding='utf-8') as json_file:
        dump(results, json_file, ensure_ascii=False, indent=4)

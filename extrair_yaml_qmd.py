import os
import ast
import json

def extrair_metadados_qmd(caminho_arquivo):
    """
    Lê o arquivo .qmd e retorna um dicionário com:
    - title
    - description
    - categories (lista)
    - children_paths (lista de caminhos de arquivos filhos, se existirem)
    """
    dados = {
        'title': None,
        'description': None,
        'categories': [],
        'children_paths': []
    }

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        bloco_yaml = []
        dentro_yaml = False

        for linha in arquivo:
            linha_strip = linha.strip()

            # Verifica início/fim do bloco YAML
            if linha_strip == '---':
                dentro_yaml = not dentro_yaml
                # se chegamos ao fim do bloco YAML, paramos
                if not dentro_yaml:
                    break
                continue

            if dentro_yaml:
                bloco_yaml.append(linha_strip)

    # Percorre o bloco YAML para extrair as informações
    for linha in bloco_yaml:
        # title:
        if linha.startswith('title:'):
            dados['title'] = linha.replace('title:', '').strip().strip('"')
        # description:
        elif linha.startswith('description:'):
            dados['description'] = linha.replace('description:', '').strip().strip('"')
        # categories:
        elif linha.startswith('categories:'):
            # Exemplo: categories: ["estatística", "amostragem"]
            lista_categorias_str = linha.replace('categories:', '').strip()
            try:
                dados['categories'] = ast.literal_eval(lista_categorias_str)
            except Exception:
                dados['categories'] = []
        # linhas que começam com '- conteudo/' => caminho de arquivo filho
        elif linha.startswith('- conteudo/'):
            caminho_filho = linha.lstrip('-').strip()  # remove '- ' do início
            dados['children_paths'].append(caminho_filho)

    return dados


def processar_qmds_base(diretorio='.'):
    """
    1. Lê todos os .qmd no diretório atual (sem subpastas).
    2. Extrai as informações do arquivo pai (filename, title, description, categories).
    3. Para cada caminho de arquivo filho encontrado, extrai as mesmas informações.
    4. Retorna uma lista de dicionários, em que cada dicionário representa o arquivo pai, com:
       {
         "filename": <nome do arquivo pai>,
         "title": ...,
         "description": ...,
         "categories": [...],
         "children_paths": {
             "<caminho_filho>": {
                 "filename": <caminho_filho>,
                 "title": ...,
                 "description": ...,
                 "categories": [...]
             },
             ...
         }
       }
    """

    resultado = []

    for nome_arquivo in os.listdir(diretorio):
        if nome_arquivo.endswith('.qmd'):
            caminho_arquivo_pai = os.path.join(diretorio, nome_arquivo)

            # Garante que é um arquivo, não uma pasta
            if os.path.isfile(caminho_arquivo_pai):
                # Extrai metadados do arquivo pai
                dados_pai = extrair_metadados_qmd(caminho_arquivo_pai)

                # Monta o dicionário final do arquivo pai
                dict_pai = {
                    'filename': nome_arquivo,
                    'title': dados_pai['title'],
                    'description': dados_pai['description'],
                    'categories': dados_pai['categories'],
                    'children_paths': {}
                }

                # Processa cada arquivo filho
                for caminho_filho in dados_pai['children_paths']:
                    caminho_arquivo_filho = os.path.join(diretorio, caminho_filho)
                    if os.path.isfile(caminho_arquivo_filho):
                        dados_filho = extrair_metadados_qmd(caminho_arquivo_filho)

                        dict_filho = {
                            'filename': caminho_filho,
                            'title': dados_filho['title'],
                            'description': dados_filho['description'],
                            'categories': dados_filho['categories']
                        }

                        # Insere esse dicionário de filho dentro de 'children_paths'
                        dict_pai['children_paths'][caminho_filho] = dict_filho

                # Adiciona o dicionário do pai à lista de resultados
                resultado.append(dict_pai)

    return resultado


if __name__ == '__main__':
    dados_qmd = processar_qmds_base()
    
    # Salva o dicionário como arquivo JSON
    with open('saida.json', 'w', encoding='utf-8') as f:
        json.dump(dados_qmd, f, ensure_ascii=False, indent=2)


    # Exemplo: imprimir cada dicionário pai
    for item in dados_qmd:
        print(item)

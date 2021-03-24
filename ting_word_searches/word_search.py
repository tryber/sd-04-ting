def exists_word(word, instance):
    resultado = []
    contador = 0
    apareceu = []
    for elemento in range(len(instance)):
        file = instance.search(elemento)
        contador += 1
        if word in file["linhas_do_arquivo"][0]:
            apareceu.append({"linha": contador})
            resultado.append({
                "palavra": f"{word}",
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": apareceu,
            })
    return resultado


def search_by_word(word, instance):
    resultado = []
    contador = 0
    apareceu = []
    for elemento in range(instance.__len__()):
        file = instance.search(elemento)
        contador += 1
        for line in file["linhas_do_arquivo"]:
            # if word in file["linhas_do_arquivo"][0]:
            if word in line:
                conteudo = {
                    # "conteudo": file["linhas_do_arquivo"][0],
                    "linha": contador,
                    "conteudo": line,
                }
                apareceu.append(conteudo)
                conteudo_resultado = {
                    "palavra": f"{word}",
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": apareceu,
                }
                resultado.append(conteudo_resultado)
    return resultado

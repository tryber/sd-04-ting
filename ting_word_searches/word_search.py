def search_on_lines(word, file_info, add_content):
    result = []
    for index in range(len(file_info["linhas_do_arquivo"])):
        line = file_info["linhas_do_arquivo"][index]
        if word.lower() in line.lower():
            occurrences = {"linha": index + 1}
            if add_content:
                occurrences["conteudo"] = line
            result.append(occurrences)
    return result

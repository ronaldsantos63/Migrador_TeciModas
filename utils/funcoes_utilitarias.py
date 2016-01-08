#!/usr/bin/env python
# encoding: utf-8

def remove_caracteres(texto):
    try:
        texto = str(texto)
        new_txt = texto.strip()
        if len(new_txt) == 0:
            return [False, "Foi passado um texto em branco"]

        new_txt = new_txt.replace("CALÃA", "CALCA").replace("Á", "A").replace("Â", "A").replace("Ã", "A") \
            .replace("À", "A").replace("É", "E").replace("Ê", "E").replace("È", "E").replace("Í", "I") \
            .replace("Ì", "I").replace("Ó", "O").replace("Õ", "O").replace("Ô", "O").replace("Ò", "O") \
            .replace("Ú", "U").replace("Ü", "U").replace("Ù", "U").replace("Ç", "C").replace(":", " ")
        while new_txt.__contains__("Փ") or new_txt.__contains__("�"):
            new_txt = new_txt.replace("Փ", " ")
            new_txt = new_txt.replace("�", " ")
        while new_txt.__contains__("ڰ"):
            new_txt = new_txt.replace("ڰ", " ")
        while new_txt.__contains__("ڱ"):
            new_txt = new_txt.replace("ڱ", " ")
        while new_txt.__contains__("ڲ"):
            new_txt = new_txt.replace("ڲ", " ")
        while new_txt.__contains__('ڳ'):
            new_txt = new_txt.replace("ڳ", " ")
        while new_txt.__contains__("ڴ"):
            new_txt = new_txt.replace("ڴ", " ")
        while new_txt.__contains__("ڵ"):
            new_txt = new_txt.replace("ڵ", " ")
        while new_txt.__contains__("ڷ"):
            new_txt = new_txt.replace("ڷ", " ")
        while new_txt.__contains__("ڹ"):
            new_txt = new_txt.replace("ڹ", " ")
        while new_txt.__contains__("&"):
            new_txt = new_txt.replace("&", " ")
        while new_txt.__contains__("(") or new_txt.__contains__(")"):
            new_txt = new_txt.replace("(", " ")
            new_txt = new_txt.replace(")", " ")
        while new_txt.__contains__("[") or new_txt.__contains__("]"):
            new_txt = new_txt.replace("[", " ")
            new_txt = new_txt.replace("]", " ")
        while new_txt.__contains__("/") or new_txt.__contains__("\\"):
            new_txt = new_txt.replace("/", " ")
            new_txt = new_txt.replace("\\", " ")
        # while new_txt.__contains__("."):
        #     new_txt = new_txt.replace(".", " ")
        while new_txt.__contains__("'") or new_txt.__contains__("`") or new_txt.__contains__("´"):
            new_txt = new_txt.replace("'", " ")
            new_txt = new_txt.replace("`", " ")
            new_txt = new_txt.replace("´", " ")
        while new_txt.__contains__("$") or new_txt.__contains__("§"):
            new_txt = new_txt.replace("$", " ")
            new_txt = new_txt.replace("§", " ")
        while new_txt.__contains__('"') or new_txt.__contains__('""') or new_txt.__contains__("''"):
            new_txt = new_txt.replace('"', " ")
            new_txt = new_txt.replace('""', " ")
            new_txt = new_txt.replace("''", " ")
        while new_txt.__contains__("º") or new_txt.__contains__("ª") or new_txt.__contains__("€"):
            new_txt = new_txt.replace("€", " ")
            new_txt = new_txt.replace("º", " ")
            new_txt = new_txt.replace("ª", " ")
        while new_txt.__contains__("├") or new_txt.__contains__("¬") or new_txt.__contains__("┤"):
            new_txt = new_txt.replace("├", "A")
            new_txt = new_txt.replace("¬", "")
            new_txt = new_txt.replace("┤", " ")
        while new_txt.__contains__("┌") or new_txt.__contains__("╔"):
            new_txt = new_txt.replace("╔", " ")
            new_txt = new_txt.replace("┌", "U")
        while new_txt.__contains__("  "):
            new_txt = new_txt.replace("  ", " ")

        new_txt = new_txt.strip()

        return [True, new_txt]

    except Exception as e:
        print("Erro ao formatar dados\nErro: {}".format(e))
        return [False, "Erro ao formatar texto\nErro: {}".format(e)]
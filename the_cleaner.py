import re

def clean(file):
    message = remove_chat_trash_data(file)
    cleaner = remove_non_message_text(message)
    return cleaner

def remove_chat_trash_data(file):
    
    books = ("""Génesis", "Éxodo", "Levítico",
             "Números", "Deuteronomio", "Josué",
             "Jueces", "Rut", "1 Samuel", "2 Samuel",
             "1 Reyes", "2 Reyes", "1 Crónicas", "2 Crónicas",
             "Esdras", "Nehemías", "Ester", "Job",
             "Salmos", "Proverbios", "Eclesiastés", "Cantares", "Isaías",
             "Jeremías", "Lamentaciones", "Ezequiel", "Daniel", "Oseas",
             "Joel", "Amós", "Abdías", "Jonás", "Miqueas",
             "Nahúm", "Habacuc", "Sofonías", "Hageo", "Zacarías", "Malaquías",
             "Mateo", "Marcos", "Lucas", "Juan", "Hechos", "Romanos", "1 Corintios",
             "2 Corintios", "Gálatas", "Efesios", "Filipenses",
             "Colosenses", "1 Tesalonicenses", "2 Tesalonicenses", "1 Timoteo", "2 Timoteo",
             "Tito", "Filemón", "Hebreos", "Santiago", "1 Pedro", "2 Pedro",
             "1 Juan", "2 Juan", "3 Juan", "Judas", "Apocalipsis""")
    verses = ("""1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
              "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
              "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
              "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
              "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
              "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
              "71", "72", "73", "74", "75", "76""")
    spaces = """
    """
    erase = books + verses + spaces
    
    with open(file, "r", encoding="UTF-8") as corpus_file:
        content = corpus_file.read()
        cleaned = re.sub(erase, "", content)
    return tuple(cleaned.split("\n"))

def remove_non_message_text(export_text_lines):
    
    messages = export_text_lines[1:-1]

    filter_out_msgs = ("<Multimedia omitido>",)
    return tuple((msg for msg in messages if msg not in filter_out_msgs))
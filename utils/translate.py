from googletrans import Translator

def translate_text_google(text, dest="ru"):
    translator = Translator()
    result = translator.translate(text, dest=dest)
    return result.text
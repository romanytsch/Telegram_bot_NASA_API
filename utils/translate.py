from googletrans import Translator

def translate_text_google(text: str, dest: str ="ru") -> str:
    """
        Переводит текст на указанный язык с использованием Google Translate.

        :param text: Исходный текст.
        :param dest: Язык назначения (по умолчанию 'ru').
        :return: Переведённый текст.
    """
    translator = Translator()
    result = translator.translate(text, dest=dest)
    return result.text
import gtts.lang
langs = gtts.lang.tts_langs()
print('lo' in langs, langs.get('lo'))
print(langs)  # see what codes are available

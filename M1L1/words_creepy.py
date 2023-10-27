meme_dict = {
            'LOL':     'una respuesta a algo gracioso',
            'CRINGE':  'algo raro o embarazoso',
            'ROFL':    'una respuesta a una broma',
            'SHEESH':  'ligera desaprobación',
            'CREEPY':  'aterrador, siniestro',
            'AGGRO':   'ponerse agresivo/enojado',
            'CHULO':   'significa que es algo muy bueno'
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print('Pon otra palabra ')

























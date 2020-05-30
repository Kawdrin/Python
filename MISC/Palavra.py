"""Programa Que Corta Palavras."""

def cut_string(p_arg: str, s_arg: str, c: str) -> str:
    """Corta as strings."""
    try:
        cut_p = [p for p in p_arg.lower()]
        cut_s = [p for p in s_arg.lower()]

        cut_p_index = cut_p[:cut_p.index(c)]
        cut_s_index = cut_s[cut_s.index(c):]

        return ''.join(cut_p_index) + ''.join(cut_s_index)
    except Exception:
        print('Strings Invalidas!!!')


while True:
    print('-=-'*10)
    p_palavra = str(input('Primeira: '))
    s_palavra = str(input('Segundo: '))
    cut = str(input('Corta: ')).lower()
    if(cut == 'exit'):
        break
    else:
        print(cut_string(p_palavra, s_palavra, cut))

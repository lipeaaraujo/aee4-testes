def decodeMessageEx(encodedMessage):
  
    char_map = {
        '*': '@',
        '|': '!',
        '$': '?',
        '_': ' '
    }

    consonant_map = {
        'b': 'y', 'c': 'x', 
        'd': 'w', 'f': 'v', 
        'g': 'u', 'h': 't', 
        'j': 's','k': 'r', 
        'l': 'q', 'm': 'p', 
        'n': 'o', 'p': 'n', 
        'q': 'm', 'r': 'l',
        's': 'k', 't': 'j', 
        'v': 'h', 'w': 'g', 
        'x': 'f', 'y': 'e', 
        'z': 'd'
    }

    decoded_message = []
    prev_char = None
    count = 0

    for char in encodedMessage:
        # remove os caracteres indesejados
        if char in {'#', 'ˆ'}:
            continue

        # Vogais duplicadas
        if char in "aeiou":
            if char == prev_char:
                count += 1
                if count > 2:
                    prev_char = ""
                continue
            else:
                count = 1
        else:
            count = 0
        

        #Inverte consoantes
        if char in consonant_map:
            char = consonant_map[char]

        # Decrementa o número
        if char.isdigit():
            char = '9' if char == '0' else str(int(char) - 1)

        # Caracteres especiais convertidos
        if char in char_map:
            char = char_map[char]

        decoded_message.append(char)
        prev_char = char


        return ''.join(decoded_message)
    
def decodeMessage(encodedMessage):
    char_map = {
        '*': '@',
        '|': '!',
        '$': '?',
        '_': ' '
    }
    
    consonant_map = {
        'b': 'z', 'c': 'y', 'd': 'x', 'f': 'w', 'g': 'v',
        'h': 't', 'j': 's', 'k': 'r', 'l': 'q', 'm': 'p',
        'n': 'n', 'p': 'm', 'q': 'l', 'r': 'k', 's': 'j',
        't': 'h', 'v': 'g', 'w': 'f', 'x': 'd', 'y': 'c', 'z': 'b'
    }
    
    if encodedMessage == "":
        return ""
    
    decoded_message = ""
    prev_char = None
    for char in encodedMessage:
        # remove vogal duplicada
        if char in "aeiou" and prev_char == char:
            prev_char = None # limpa depois de achar um par
            continue
        prev_char = char
    
        # Caracteres especiais convertidos
        if char in char_map:
            char = char_map[char]
            
        # remove os caracteres indesejados
        if char in {'#', '^'}:
            continue
        
        # Decrementa o número
        if char.isdigit():
            char = '9' if char == '0' else str(int(char) - 1)
            
        # Inverte consoantes
        if char in consonant_map:
            char = consonant_map[char]
                        
        # adiciona o char a resposta
        decoded_message = decoded_message + char

    return decoded_message

if __name__ == "__main__":
    decodeMessage.main()
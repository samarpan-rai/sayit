number_to_text_map = {
    0 : 'zero',
    1 : 'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine'
}
    


def int2text(number:int):
    if number in number_to_text_map.keys():
        return number_to_text_map[number]
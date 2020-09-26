between_zero_and_9 = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

between_10_and_19 = {10: "ten"}


between_20_and_100 = {20: "twenty"}


number_to_text_map = {**between_zero_and_9, **between_10_and_19, **between_20_and_100}


def int2text(number: int):
    if number in number_to_text_map.keys():
        return number_to_text_map[number]

'''
OwO what's this
(it's a program that makes text into uwu-speak)
based on the ideas of https://github.com/sorayori/Re-ZerOwO/
'''
import random

prefixes = [" OwO What's this? ",
            " OwO ",
            " H-hewwo?? ",
            " Huohhhh. ",
            " Haiiii! ",
            " UwU ",
            " OWO ",
            " HIIII! ",
            " <3 "]
suffixes = [" :3",
            " UwU ",
            " ʕʘ‿ʘʔ",
            " >_>",
            " ^_^",
            "..",
            " Huoh.",
            " ^-^",
            " ;_;",
            " ;-;",
            " xD",
            " x3",
            " :D",
            " :P",
            " ;3",
            " XDDD",
            ", fwendo ",
            " ㅇㅅㅇ",
            " (人◕ω◕)",
            " （＾ｖ＾）"]
replacements = {
            "r": "w",
            "l": "w",
            "R": "W",
            "no": "nu",
            "has": "haz",
            "have": "haz",
            "you": "uu",
        }

def uwu(string):
    '''
    takes an input string and transforms it into uwu-speak
    '''
    output = ""

    for key in replacements:
        string = string.replace(key, replacements[key])

    sentences = string.split(".")

    for sentence in sentences:
        coin_1 = random.randrange(0, 2)
        if coin_1 == 1:
            sentence = random.choice(prefixes) + sentence

        coin_2 = random.randrange(0, 2)
        if coin_2 == 1:
            sentence = sentence + random.choice(suffixes)

        else:
            sentence += "."

        output += sentence

    print(output)

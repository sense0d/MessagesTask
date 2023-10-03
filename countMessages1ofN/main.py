def countTextCharsLenght(text):
    result = isinstance(text, list)
    if result:
        # print('yes')
        lengthText = len(text) - 1

        for word in text:
            # print(len(word))
            lengthText += len(word)
        # print(lengthtext)
        if lengthText > 140:
            print('large text')
            if lengthText < 1161:
                print('there be 9 parts')
            elif lengthText > 1160:
                print('there be 10 parts')
            elif lengthText > 1279:
                print('text too large')
        else:
            print('small text')
    else:
        print('this not array')





text123 = ['sdasd', 'asdasd', 'dsadas']
textTest1 = [
    "Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
    "Curabitur", "consequat", "sapien", "eu", "ante", "blandit", "ac", "tincidunt",
    "libero", "interdum", "Fusce", "vehicula", "ornare", "vestibulum", "Maecenas",
    "vitae", "massa", "eu", "libero", "consequat", "vehicula", "Nullam", "eu", "eleifend",
    "elit", "Sed", "eget", "urna", "eget", "mi", "congue", "consectetur", "Pellentesque",
    "eget", "nibh", "nec", "purus", "dictum", "feugiat", "Cras", "ut", "lectus", "in",
    "nulla", "efficitur", "posuere", "Vivamus", "tristique", "sollicitudin", "libero",
    "eu", "laoreet", "dui", "facilisis", "a", "Sed", "feugiat", "mauris", "nec", "lacinia", "interdum"]


# countTextCharsLenght(text123)
countTextCharsLenght(textTest1)
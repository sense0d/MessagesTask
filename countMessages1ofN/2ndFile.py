def countTextCharsLenght(text):
    result = isinstance(text, list)
    if result:
        lengthText = len(text) - 1
        messagelength1 = 0
        message1 = []
        for word in text:
            # print(len(word))
            lengthText += len(word)
        print(lengthText)
        if lengthText > 140 and lengthText < 1279:
            print('large text')
            if lengthText > 1160:
                parts = 10
            else:
                resultParts = lengthText/129
                if isinstance(resultParts, float):
                    parts = int(resultParts) +1
                    # print(parts)
                else:
                    parts = resultParts
            # message1 = []
            partof = 1
            for i, word in enumerate(text):
                if messagelength1 < 127:
                    messagelength1 += len(word) + 1
                    firstWordNextMessage = f'{word} '
                    if messagelength1 < 127:
                        # print(word)
                        str = f'{word} '
                        message1.append(str)
                        if i == len(text)-1:
                            messagelength1 = 0
                            str = f'Part {partof} of {parts}'
                            message1.append(str)
                            print(message1)
                            partof += 1
                    else:
                        messagelength1 = 0
                        str = f'Part {partof} of {parts}'
                        message1.append(str)
                        print(message1)
                        partof += 1
                        message1.clear()
                        message1.append(firstWordNextMessage)
        elif lengthText > 1279:
            print('toolarge')
        else:
            print('small text')
            for word in text:
                str = f'{word} '
                message1.append(str)
            print(message1)
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
textTest2 = [
    "She", "started", "with", "insinuations", "simple", "artless", "ones", "that",
    "Pierre", "hardly", "even", "recognized", "Then", "she", "tried", "blunt",
    "accusation", "in", "the", "privacy", "of", "their", "bedroom", "When", "he",
    "denied", "that", "she", "resorted", "to", "violent", "humiliating", "denouncements",
    "in", "the", "kitchens", "the", "winery", "the", "plantations", "The", "angel", "that",
    "Pierre", "had", "married", "in", "Madagascar", "had", "become", "a", "termagant",
    "blinded", "by", "jealousy", "Nothing", "he", "did", "or", "said", "could", "help",
    "Often", "she", "would", "refuse", "to", "speak", "for", "a", "week", "or", "more", "and",
    "when", "at", "last", "she", "spoke", "it", "would", "only", "be", "to", "scream", "yet",
    "more", "abuse", "or", "swear", "again", "her", "intention", "to", "leave", "him", "By",
    "the", "third", "vine-harvest", "it", "was", "obvious", "to", "everyone", "that", "they",
    "loathed", "each", "other", "One", "Friday", "evening", "Pierre", "was", "down", "in", "the",
    "winery", "working", "on", "a", "new", "electric", "winepress", "He", "was", "alone", "The",
    "grape-pickers", "had", "left", "Suddenly", "the", "door", "opened", "and", "Faniry", "entered",
    "excessively", "made", "up", "She", "walked", "straight", "up", "to", "Pierre", "flung", "her",
    "arms", "around", "his", "neck", "and", "pressed", "herself", "against", "him", "Even", "above",
    "the", "fumes", "from", "the", "pressed", "grapes", "he", "could", "smell", "that", "she", "had",
    "been", "drinking"
]
textTest3 = [
    "For", "the", "most", "wild", "yet", "most", "homely", "narrative", "which", "I", "am", "about", "to",
    "pen", "I", "neither", "expect", "nor", "solicit", "belief", "Mad", "indeed", "would", "I", "be", "to",
    "expect", "it", "in", "a", "case", "where", "my", "very", "senses", "reject", "their", "own", "evidence",
    "Yet", "mad", "am", "I", "not", "and", "very", "surely", "do", "I", "not", "dream", "But", "to-morrow", "I",
    "die", "and", "to-day", "I", "would", "unburthen", "my", "soul", "My", "immediate", "purpose", "is", "to",
    "place", "before", "the", "world", "plainly", "succinctly", "and", "without", "comment", "a", "series", "of",
    "mere", "household", "events", "In", "their", "consequences", "these", "events", "have", "terrified", "have",
    "tortured", "have", "destroyed", "me", "Yet", "I", "will", "not", "attempt", "to", "expound", "them", "To", "me",
    "they", "have", "presented", "little", "but", "Horror", "to", "many", "they", "will", "seem", "less", "terrible",
    "than", "barroques", "Hereafter", "perhaps", "some", "intellect", "may", "be", "found", "which", "will", "reduce",
    "my", "phantasm", "to", "the", "common-place", "some", "intellect", "more", "calm", "more", "logical", "and",
    "far", "less", "excitable", "than", "my", "own", "which", "will", "perceive", "in", "the", "circumstances", "I",
    "detail", "with", "awe", "nothing", "more", "than", "an", "ordinary", "succession", "of", "very", "natural",
    "causes", "and", "effects", "From", "my", "infancy", "I", "was", "noted", "for", "the", "docility", "and",
    "humanity", "of", "my", "disposition", "My", "tenderness", "of", "heart", "was", "even", "so", "conspicuous",
    "as", "to", "make", "me", "the", "jest", "of", "my", "companions", "I", "was", "especially", "fond", "of",
    "animals", "and", "was", "indulged", "by", "my", "parents","with", "a", "great", "variety", "of", "pets",
    "with", "a", "great", "variety", "of", "pets","with", "a", "great", "variety", "of", "pets","great", "variety", "of", "pets",
]
textTest31 = [
    "For", "the", "most", "wild", "yet", "most", "homely", "narrative", "which", "I", "am", "about", "to",
    "pen", "I", "neither", "expect", "nor", "solicit", "belief", "Mad", "indeed", "would", "I", "be", "to",
    "expect", "it", "in", "a", "case", "where", "my", "very", "senses", "reject", "their", "own", "evidence",
    "Yet", "mad", "am", "I", "not", "and", "very", "surely", "do", "I", "not", "dream", "But", "to-morrow", "I",
    "die", "and", "to-day", "I", "would", "unburthen", "my", "soul", "My", "immediate", "purpose", "is", "to",
    "place", "before", "the", "world", "plainly", "succinctly", "and", "without", "comment", "a", "series", "of",
    "mere", "household", "events", "In", "their", "consequences", "these", "events", "have", "terrified", "have",
    "tortured", "have", "destroyed", "me", "Yet", "I", "will", "not", "attempt", "to", "expound", "them", "To", "me",
    "they", "have", "presented", "little", "but", "Horror", "to", "many", "they", "will", "seem", "less", "terrible",
    "than", "barroques", "Hereafter", "perhaps", "some", "intellect", "may", "be", "found", "which", "will", "reduce",
    "my", "phantasm", "to", "the", "common-place", "some", "intellect", "more", "calm", "more", "logical", "and",
    "far", "less", "excitable", "than", "my", "own", "which", "will", "perceive", "in", "the", "circumstances", "I",
    "detail", "with", "awe", "nothing", "more", "than", "an", "ordinary", "succession", "of", "very", "natural",
    "causes", "and", "effects", "From", "my", "infancy", "I", "was", "noted", "for", "the", "docility", "and",
    "humanity", "of", "my", "disposition", "My", "tenderness", "of", "heart", "was", "even", "so", "conspicuous",
    "as", "to", "make", "me", "the", "jest", "of", "my", "companions", "I", "was", "especially", "fond", "of",
    "animals", "and", "was", "indulged", "by", "my", "parents","with", "a", "great", "variety", "of", "pets",
    "with", "a", "great", "variety", "of", "pets","with", "a", "great", "variety", "of", "pets",
]

# tests
# countTextCharsLenght(text123)
# countTextCharsLenght(textTest1)
# countTextCharsLenght(textTest2)
# countTextCharsLenght(textTest3)
countTextCharsLenght(textTest31)


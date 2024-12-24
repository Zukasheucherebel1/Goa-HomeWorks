def variance(numbers): 
    total = 0
    variance = 0
    for i in numbers:
        total += i
    total /= len(numbers)
    for i in numbers:
        variance += (i - total) ** 2
    return variance / len(numbers)


def find_missing_letter(input):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    start = alphabet.index(input[0])
    for i in range(len(input)):
        if not input[i] == alphabet[start+i]:
            return alphabet[start+i]
        
        return None
    

    # Test the function with the provided example
print(variance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
print(find_missing_letter(['O', 'Q', 'R', 'S']))
print(find_missing_letter(['a', 'b', 'c', 'd', 'e',
                           'f']))





def high(x):
    highest_score = 0
    for word in x.split(' '):
        score = sum(ord(c)-96 for c in word)
        if score > highest_score:
            highest_score = score
            highest_word = word
            
    return highest_word
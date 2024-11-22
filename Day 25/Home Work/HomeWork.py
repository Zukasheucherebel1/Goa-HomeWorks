def sentence_to_list_and_back(sentence):
    words = sentence.split()  
    new_sentence = ", ".join(words)  
    return new_sentence

result = sentence_to_list_and_back("This is a sample sentence")
print(result)  

def print_word_lengths(sentence):
    words = sentence.split()  # 
    for word in words:
        print(f"Word: '{word}', Length: {len(word)}")  


print_word_lengths("Hello world this is a test")




def remove_extra_spaces(sentence):
    clean_sentence = " ".join(sentence.split())  
    return clean_sentence

result = remove_extra_spaces("This    is   a  sentence  with   extra  spaces")
print(result)  



def replace_spaces_with_hyphen(sentence):
    new_sentence = "-".join(sentence.split()) 
    return new_sentence

# მაგალითი:
result = replace_spaces_with_hyphen("Replace spaces with hyphens")
print(result)  



def reverse_word_order(sentence):
    words = sentence.split()  
    reversed_words = words[::-1]  
    new_sentence = " ".join(reversed_words)  
    return new_sentence

# მაგალითი:
result = reverse_word_order("Hello World!")
print(result)  # შედეგი: "World! Hello"


text = "hello world"
print(text.capitalize())  


text = "hello world"
print(text.title())  

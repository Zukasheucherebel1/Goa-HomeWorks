def manual_replace(input_string):
    # შექმნით ცარიელ სტრინგს, სადაც შევინახავთ შედეგს
    result = ""
    
    # ვათვალიერებთ თითოეულ სიმბოლოს სტრინგში
    for char in input_string:
        # თუ სიმბოლო არის space, ვამატებთ ტირე
        if char == " ":
            result += "-"
        else:
            # სხვა შემთხვევაში ვამატებთ სიმბოლოს როგორც არის
            result += char
            
    return result

# მაგალითი
test_string = "გამარჯობა მსოფლიო"
print(manual_replace(test_string))  # შედეგი: "გამარჯობა-მსოფლიო"
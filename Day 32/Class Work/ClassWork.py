def manual_count(string, element):
    count = 0  
    for char in string:  
        if char == element:  
            count += 1  
    return count  



def manual_replace(string):
    result = ""  
    for char in string: 
        if char == " ":  
            result += "-"  
        else:
            result += char  
    return result  


#მეოთხე დავალების ახსნა

 # შევქმნით ცვლად result, რომელიც ინახავს საბოლოო შედეგს
# გადავუაროთ შტრინგის ყველა სიმბოლოს
# თუ მიმდინარე სიმბოლო არის space
# ვამატებთ ტირეს result-ში
# სხვა შემთხვევაში ვამატებთ მიმდინარე სიმბოლოს result-ში
# ვაბრუნებთ საბოლოს
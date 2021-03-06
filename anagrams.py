def is_anagram(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()
    for i in text1:
        if text1.count(i) != text2.count(i):
            return "Not anagrams"
            
    return "Anagrams"
    
    
text1 = input("Enter your first text: ")
text2 = input("Enter your second text: ")

print(is_anagram(text1, text2))
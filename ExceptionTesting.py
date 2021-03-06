def read_int(prompt, min, max):
    try:
        prompt = int(prompt)
    except:
        print("Error: wrong input")
        prompt = input("Enter a number from -10 to 10: ")
        if prompt.isdigit():
            prompt = int(prompt)
        else:exit(1)
        
    try:
        assert min <= prompt <= max
    except:
        print("Error: the value is not within permitted range (-10..10)")
        prompt = input("Enter a number from -10 to 10: ")
        if prompt.isdigit():
            prompt = int(prompt)
        else:exit(1)
        
    return prompt
        
        


# v = read_int("Enter a number from -10 to 10: ", -10, 10)

# print("The number is:", v)

new_arr = [1, "dog", False]

for i in range(3):
    print(f"new_arr length = {len(new_arr)}, new_arr[0] = {new_arr[0]}")
    del new_arr[0]

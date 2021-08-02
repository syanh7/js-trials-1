"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)    


def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums


def get_odd_indices(items):
    result = []
    for i in range(len(items)):
        if i % 2 != 0:
            result.append(items[i])
    
    return result


def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f'{i}. {item}')
        i+=1


def get_range(start, stop):
    nums = []
    for num in range(start, stop):
        nums.append(num)
    return nums    


def censor_vowels(word):
    chars = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        if char in vowels:
            chars.append("*")
        else:
            chars.append(char)
    return "".join(chars)


def snake_to_camel(string):
    camel_case = []
    for element in string.split("_"):
        camel_case.append(element[0].upper() + element[1:])
    return "".join(camel_case)


def longest_word_length(words):
    longest = len(words[0])
    for word in words:
        if longest < len(word):
            longest = len(word)
    return longest        


def truncate(string):
    result = ['']
    
    for ch in string:
        if ch != result[-1]:
            result.append(ch)
    
    return ''.join(result)


def has_balanced_parens(string):
    parens = {}
    #'(Oh no!)('

    for ch in string:
        parens[ch] = parens.get(ch, 0) + 1
        #parens['('] = parens.get('(', 0 ) + 1
        #parens = {'(':2, 'O':1, 'h':1, '(',1}
    
    if parens['('] == parens[')']:
        return True
    else:
        print('whatups')
        return False


def compress(string):
    compressed = []
    curr_char = ''
    char_count = 0

    for ch in string:
        if ch != curr_char:
            compressed.append(curr_char)
            if char_count > 1:
                compressed.append(str(char_count))
            curr_char = ch
            char_count = 0
        char_count += 1
    
    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))
    
    return ''.join(compressed)

    


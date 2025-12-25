def get_num_words(text):
    words = text.split()
    return len(words)

def num_of_char(text):
    word_dict = {}
    for char in text:
        char = char.lower()
        if char  in  word_dict:
            word_dict[char] += 1
        else:
            word_dict[char] = 1
    return word_dict

def char_dic_to_sort_list(char_counts):
    sorted_list = []
    for char,count in char_counts.items():
        sorted_list.append({'char': char, 'num': count})
    sorted_list.sort(key=lambda x: x['num'], reverse=True)
    return sorted_list




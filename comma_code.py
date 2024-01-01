def comma_code(n_str):
    nw_str = ''
    for i in range(len(n_str)):
        print(n_str[i], i)
        if i > 0 and i < len(n_str) - 1:
            nw_str = nw_str + ', ' + n_str[i]
        elif i == (len(n_str) - 1):
            nw_str = nw_str + ', and ' + n_str[i]
        else:
            nw_str = nw_str + n_str[i]
    return(nw_str)

spam = ['apples', 'bananas', 'tofu', 'cats']

new_string = comma_code(spam)


print(new_string)
print(type(new_string))

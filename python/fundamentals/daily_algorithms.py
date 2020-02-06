
# 1. Parens Valid: Create a function that, given an input string str , returns a boolean whether parentheses in str are valid. Valid sets of parentheses always open before they close.


def paren_valid(str):
    openings = 0
    closings = 0

    for char in str:
        if char == '(':
            openings += 1
        elif char == ")":
            closings += 1
            if closings > openings:
                return False

    return openings == closings


print(paren_valid("Y(3(p)p(3)r)s"))
print(paren_valid("N(0(p)3"))
print(paren_valid("N(0)t ) 0( k"))
print(paren_valid("a(b))(c"))


# 2. Braces Valid: Given a sequence of parentheses, braces and brackets, determine whether it is valid.


def braces_valid(string):
    openings = []
    dict = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in dict.values():
            openings.append(char)
        elif char in dict.keys():
            if dict[char] == openings[len(openings) - 1]:
                openings.pop()
            else:
                return False

    return len(openings) < 1


print(braces_valid("W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!"))


def is_palindrome(str):
    reversed_str = ""
    for i in range(len(str) - 1, -1, -1):
        reversed_str += str[i]
    return str == reversed_str


# def longest_palindrome(str):
#     palins = []
#     for i in range(len(str)):
#         if i > 0 and i < len(str) - 1:
#             if str[i - 1] == str[i + 1]:
#                 p_str = str[i - 1: i + 1]
#                 left = i - 1
#                 right = i + 1
#                 done = True

#                 while (done):
#                     if done == is_palindrome(p_str):
#                         done = True
#                         break
#                     else:
#                         left -= 1
#                         right += 1
#                         if left < 0 or right > len(str):
#                             break
#                         else:
#                         p_str = str[left: right]

#                 if done:


def book_index(list):
    final_str = ""
    last_num = 0

    for i in range(len(list)):
        if i == len(list) - 1:
            final_str += f"{list[i]}"
        else:
            if list[i] > last_num:
                for x in range(i, len(list) - 1):
                    if list[x] + 1 == list[x + 1]:
                        last_num = list[x + 1]
                    else:
                        final_str += f"{list[i]}{("" if last_num < 0 else "-" + str(last_num))}, "
                        break

    return final_str

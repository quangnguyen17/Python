
# Parens Valid
# Create a function that, given an input string str , returns a boolean whether parentheses in str are valid. Valid sets of parentheses always open before they close.


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

# Braces Valid
# Given a sequence of parentheses, braces and brackets, determine whether it is valid.


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

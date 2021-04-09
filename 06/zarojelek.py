#!/usr/bin/env python3


def is_valid(string):
    open_brackets = ["(", "[", "{"]
    closed_brackets = [")", "]", "}"]
    stack_of_brackets = []
    
    for c in string:
        if c in open_brackets:
            stack_of_brackets.append(c)
        elif c in closed_brackets:
            pos = closed_brackets.index(c)
            if(len(stack_of_brackets) > 0 and (open_brackets[pos] == stack_of_brackets[len(stack_of_brackets)-1])):
                stack_of_brackets.pop()
            else:
                return False
    return len(stack_of_brackets) == 0


def main():
    test1 = "((5+3)*2+1)"
    test2 = "{[(3+1)+2]+}"
    test3 = "(3+{1-1)}"
    test4 = "[1+1]+(2*2)-{3/3}"
    test5 = "(({[(((1)-2)+3)-3]/3}-3)"
    print(f"{test1} == {is_valid(test1)}")
    print(f"{test2} == {is_valid(test2)}")
    print(f"{test3} == {is_valid(test3)}")
    print(f"{test4} == {is_valid(test4)}")
    print(f"{test5} == {is_valid(test5)}")

#############################################################################

if __name__ == "__main__":
    main()
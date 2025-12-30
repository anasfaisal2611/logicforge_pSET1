def removeInvalidParentheses(expr):
    result = set()

    # Step 1: Count extra parentheses
    left_rem = right_rem = 0
    for ch in expr:
        if ch == '(':
            left_rem += 1
        elif ch == ')':
            if left_rem == 0:
                right_rem += 1
            else:
                left_rem -= 1

    # Step 2: Backtracking
    def backtrack(index, left_count, right_count, left_rem, right_rem, path):
        # End of string
        if index == len(expr):
            if left_rem == 0 and right_rem == 0:
                result.add(path)
            return

        ch = expr[index]

        # Option 1: Remove current parenthesis
        if ch == '(' and left_rem > 0:
            backtrack(index + 1, left_count, right_count,
                      left_rem - 1, right_rem, path)

        if ch == ')' and right_rem > 0:
            backtrack(index + 1, left_count, right_count,
                      left_rem, right_rem - 1, path)

        # Option 2: Keep character
        if ch not in "()":
            backtrack(index + 1, left_count, right_count,
                      left_rem, right_rem, path + ch)

        elif ch == '(':
            backtrack(index + 1, left_count + 1, right_count,
                      left_rem, right_rem, path + ch)

        elif ch == ')' and right_count < left_count:
            backtrack(index + 1, left_count, right_count + 1,
                      left_rem, right_rem, path + ch)

    backtrack(0, 0, 0, left_rem, right_rem, "")
    return list(result)
if __name__ == "__main__":
    expr = input("Enter expression: ")

    result = removeInvalidParentheses(expr)

    print("Valid expressions with minimum removals:")
    for s in result:
        print(s)

from collections import deque


def modify_stack(query: str, stack):
    if query.startswith("1"):
        # append number to the top of the stack
        number_to_push = int(query.split()[1])
        stack.append(number_to_push)
    elif query.startswith("2"):
        # delete first in the stack
        if stack:
            stack.pop()
    elif query.startswith("3"):
        # print max in the stack
        if stack:
            print(max(stack))
    elif query.startswith("4"):
        # print min in the stack
        if stack:
            print(min(stack))


def main():
    stack = deque()
    cnt_queries = int(input())
    for _ in range(cnt_queries):
        query = input()
        modify_stack(query, stack)
    else:
        # print stack when done
        print(", ".join([str(x) for x in stack][::-1]))


if __name__ == "__main__":
    main()



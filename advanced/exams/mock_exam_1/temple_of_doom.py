from collections import deque


def main():
    """
    Main function of a game Lost Temple.

    In this game, Harry must use tools and substances to craft new tools and overcome challenges.
    - The `tools` represent available tools in a queue (deque) and are consumed in reverse order.
    - The `substances` represent available substances in a list and are consumed from the back of the list.
    - The `challenges` represent the challenges Harry must overcome by combining substances and tools.

    The game continues until there are no more `tools`, `substances`, or `challenges`.
    If all challenges are overcome, Harry finds an ancient ostracon.

    Note: Tools and substances are used to craft new tools. Challenges are removed if the product of
    a substance and a tool is equal to the value of a challenge.
    """
    tools = deque([int(x) for x in input().split()])
    substances = [int(x) for x in input().split()]
    challenges = [int(x) for x in input().split()]

    while tools and substances:
        if not challenges:
            break

        tool_element = tools.popleft()
        substance_element = substances.pop()
        craft_tool = tool_element * substance_element
        if craft_tool in challenges:
            challenges.remove(craft_tool)
        else:
            tool_element += 1
            tools.append(tool_element)

            substance_element -= 1
            if substance_element > 0:
                substances.append(substance_element)

    if (not tools or not substances) and challenges:
        print("Harry is lost in the temple. Oblivion awaits him.")
    else:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
    if tools:
        print("Tools: {0}".format(", ".join([str(x) for x in tools])))
    if substances:
        print("Substances: {0}".format(", ".join([str(x) for x in substances])))
    if challenges:
        print("Challenges: {0}".format(", ".join([str(x) for x in challenges])))


if __name__ == "__main__":
    main()

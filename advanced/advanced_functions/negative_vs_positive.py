def evalute_sequence(numbers: list) -> str:
    """Function receives a list of positive and negative numbers and returns the sum of each group
       If the absolute sum of negative numbers group is larger than the positive group. The negatives are considered
       `stronger`.

       returns: string containing the sum of each group and a statement displaying the stronger group
    """
    result = ""
    positive = sum([int(x) for x in numbers if int(x) > 0])
    negative = sum([int(x) for x in numbers if int(x) < 0])

    result += f"{negative}\n"
    result += f"{positive}\n"
    if abs(negative) > positive:
        result += "The negatives are stronger than the positives"
    elif abs(negative) < positive:
        result += "The positives are stronger than the negatives"
    else:
        raise ValueError("The sum of negatives and positives is equal.")

    return result



def main():
    string_of_numbers = input()
    print(evalute_sequence(string_of_numbers.split()))

if __name__ == "__main__":
    main()

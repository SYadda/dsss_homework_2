import random


def get_random_int(min, max): # returns a random integer between min and max
    """
    parameters:
        min: int, the upper bound of the random number
        max: int, the lower bound of the random number
    returns:
        int, a random number between min and max
    """
    return random.randint(min, max)


def get_random_oper(): # returns a random operator from ['+', '-', '*']
    """
    returns:
        str, a random operator from ['+', '-', '*']
    """
    return random.choice(['+', '-', '*'])


def get_problem_and_answer(num1, num2, oper): # returns a tuple of the problem and the answer
    """
    parameters:
        num1: int, the first number
        num2: int, the second number
        oper: str, the math operator
    returns:
        tuple, a tuple of the problem (in str) and the answer (in int)
    """

    try:
        assert type(num1) == int
        assert type(num2) == int
    except AssertionError:
        raise TypeError("Invalid input. num1 and num2 must be integers.")
    
    try:
        assert oper in ['+', '-', '*']
    except AssertionError:
        raise ValueError("Invalid input. oper must be one of ['+', '-', '*'].")


    problem = f"{num1} {oper} {num2}"
    if oper == '+': 
        answer = num1 + num2
    elif oper == '-': 
        answer = num1 - num2
    elif oper == '*': 
        answer = num1 * num2
    return problem, answer

def math_quiz():
    correct_answers = 0 # how many questions the user answered correctly
    total_questions = 4 # how many questions the user will be asked

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = get_random_int(1, 10); num2 = get_random_int(1, 6); oper = get_random_oper()

        PROBLEM, ANSWER = get_problem_and_answer(num1, num2, oper)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            correct_answers += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {correct_answers}/{total_questions}")

if __name__ == "__main__":
    math_quiz()

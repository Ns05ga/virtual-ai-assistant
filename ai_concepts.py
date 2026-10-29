from datetime import datetime


def recommend_activity():
    
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        activity = "It's morning. Have breakfast and plan your day."
    elif 12 <= current_hour < 17:
        activity = "It's afternoon. Take a lunch break and continue your work."
    elif 17 <= current_hour < 21:
        activity = "It's evening. Consider exercising or relaxing."
    else:
        activity = "It's late. Consider resting and getting some sleep."

    return activity


def perceptron_demo():
                                                                                                                                                                                                                               
    print("Assistant: Perceptron demonstration")
    print("Enter two numeric inputs.")

    try:
        input1 = float(input("Enter input 1: "))
        input2 = float(input("Enter input 2: "))

    except ValueError:
        print("Assistant: Please enter valid numbers.")
        return

    
    weight1 = 0.5
    weight2 = -0.3
    bias = 0.1

    
    weighted_sum = (
        input1 * weight1
        + input2 * weight2
        + bias
    )

    
    if weighted_sum > 0:
        output = 1
    else:
        output = 0

    print(f"Assistant: Weighted sum = {weighted_sum}")
    print(f"Assistant: Perceptron output = {output}")

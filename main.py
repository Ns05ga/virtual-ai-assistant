from greetings import get_user_name, build_greeting
from datetime_utils import get_current_time, get_current_date
from calculator import parse_expression, calculate
from content import get_random_quote, get_random_joke, get_random_fact
from game import play_guessing_game
from ai_concepts import recommend_activity, perceptron_demo
from help_menu import print_help

def main():
    

    print("=" * 40)
    print("       MINI ALEXA - VIRTUAL AI")
    print("=" * 40)

   
    user_name = get_user_name()
    print(build_greeting(user_name))

    
    while True:
        command = input(f"\nYou ({user_name}): ").lower().strip()

        
        if command == "time":
            print(f"Assistant: It's currently {get_current_time()}.")

       
        elif command == "date":
            print(f"Assistant: Today's date is {get_current_date()}.")

       
        elif command == "calculate" or command.startswith("calculate "):
            try:
                number1, operator, number2 = parse_expression(command)
                result = calculate(number1, operator, number2)

               
                if result == int(result):
                    result = int(result)

                print(f"Assistant: The result is {result}")

            except ZeroDivisionError as error:
                print(f"Assistant: {error}")

            except ValueError as error:
                print(f"Assistant: {error}")

        
        elif command == "quote":
            print(f"Assistant: {get_random_quote()}")

        
        elif command == "joke":
            print(f"Assistant: {get_random_joke()}")

       
        elif command == "fact":
            print(f"Assistant: {get_random_fact()}")
        elif command == "game":
            play_guessing_game()
            
            
        elif command in ("recommend", "activity"):
            print(f"Assistant: {recommend_activity()}")

        elif command == "perceptron":
            perceptron_demo()
        elif command == "help":
            print_help()


        elif command in ("exit", "quit", "bye"):
            print(
                f"Assistant: Goodbye, {user_name}! "
                "Have a great day."
            )
            break

        else:
            print(
                "Assistant: I'm not sure I understood that. "
                "Type 'help' to see what I can do."
            )


if __name__ == "__main__":
    main()

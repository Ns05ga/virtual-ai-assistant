
# Mini Alexa - Virtual AI Assistant

## Project Description
Mini Alexa is a text-based, rule-based virtual assistant
developed using Python. It runs offline in the terminal
and uses keyword matching to respond to commands.

## Requirements
- Python 3.x
- VS Code or another text editor
- Terminal or command prompt

No external Python packages are required.

## Project Structure
- main.py: Main program and command loop
- greetings.py: Greeting and name capture
- datetime_utils.py: Current date and time
- calculator.py: Basic arithmetic
- content.py: Quotes, jokes, and facts
- game.py: Number-guessing game
- ai_concepts.py: Activity recommendation and perceptron
- help_menu.py: Help menu

## How to Run
1. Open the project folder in VS Code.
2. Open the terminal in the project folder.
3. Run:

   python main.py

## Supported Commands
- time: Show current time
- date: Show current date
- calculate: Perform arithmetic
- quote: Display a motivational quote
- joke: Tell a joke
- fact: Display a random fact
- game: Play the number-guessing game
- recommend: Recommend an activity
- activity: Recommend an activity
- perceptron: Run the perceptron demonstration
- help: Display supported commands
- exit, quit, bye: Exit the assistant

## AI Concepts
- Rule-based decision-making
- Keyword detection and pattern matching
- Simplified perceptron with fixed weights and bias
- Step activation function

The perceptron is a conceptual demonstration.
No model training is performed.

## Limitations
- Text-based interface only
- No voice input or output
- No external APIs or network services
- Session data is not saved between runs

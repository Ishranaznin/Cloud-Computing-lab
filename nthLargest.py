
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    # Take user input for the list of numbers
    number_list = input("Enter a list of numbers, separated by spaces: ").split()
    number_list = [int(num) for num in number_list]

    # Take user input for the nth value
    nth = int(input("Enter the value of n: "))
    numbers.sort(reverse=True)  # Sort the numbers in descending order
    if n > len(numbers):
        return "Invalid value of n"

    return "The {nth} largest number is: ",str(number_list[n - 1])


if __name__ == '__main__':
      app.run(host='127.0.0.1', port=8080, debug=True)

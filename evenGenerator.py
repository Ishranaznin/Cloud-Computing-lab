

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    n = int(input("Enter the value of n: "))
    even_numbers = []
    count = 0
    number = 2  # Start with the first even number
    while count < n:
        even_numbers.append(number)
        count += 1
        number += 2  # Increment by 2 to get the next even number
        even_numbers_string = ", ".join(even_numbers)
    return even_numbers_string


if __name__ == '__main__':
      app.run(host='127.0.0.1', port=8080, debug=True)

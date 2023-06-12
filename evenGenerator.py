from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/even/<int:n>', methods=['GET'])
def generate_even_numbers(n):
    """Generate n even numbers and return as JSON."""
    even_numbers = [num for num in range(2, 2 * n + 1, 2)]
    return jsonify(even_numbers)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

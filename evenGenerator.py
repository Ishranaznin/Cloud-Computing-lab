from google.appengine.ext import ndb

class EvenNumber(ndb.Model):
  number = ndb.IntegerProperty()

def generate_even_numbers(n):
  for i in range(n):
    even_number = EvenNumber(number=i * 2)
    even_number.put()

def main():
  n = int(input("Enter the number of even numbers to generate: "))
  generate_even_numbers(n)

if __name__ == "__main__":
  main()

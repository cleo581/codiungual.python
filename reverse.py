class Stringreverse:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

if __name__ == "__main__":
    user_input =input("enter a string: ").strip()
    if not user_input:
       print("no input provided")
    else:
      obj = Stringreverse(user_input)
      result = obj.reverse_words()
      print("Reversed string is:", result)

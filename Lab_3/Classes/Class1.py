class Strings:
    def _init_(self):
        self.input_string = ""

    def get_String(self):
        self.input_string = input("Enter string: ")

    def print_String(self):
        print(self.input_string.upper())


my_str = Strings()

my_str.get_String()

my_str.print_String()
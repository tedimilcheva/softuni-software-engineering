class vowels:
    def __init__(self, s):
        self.s = s
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= (len(self.s) - 1):
            c = self.s[self.i]
            self.i += 1
            if self.is_vowel(c):
                return c
        raise StopIteration()

    @staticmethod
    def is_vowel(c):
        vowels = 'aeiouy'
        return c.lower() in vowels


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
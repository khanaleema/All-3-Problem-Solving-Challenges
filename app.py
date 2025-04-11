# Assignment 3 - Problem Solving Challenges

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

if __name__ == "__main__":
    print(reverse_string("hello"))        # Output: olleh
    print(count_vowels("Apple"))          # Output: 2
    print(sum_of_digits(1234))            # Output: 10

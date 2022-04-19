# WordleBreaker
A simple Wordle helper.  
Product of a random 30-minute coding challenge I decided to do.

It uses regex to handle pretty much everything.

# Usage

`WordleBreaker().add_guess(word, result)` is basically it. Adding a guess takes a word to guess, and the result it came up with.  
The result string is composed with 3 letters:
1. x - does not exist
2. e - exists, but not in the correct position
3. c - correct

For example, if you had guessed `P O I S E` and ![image](https://user-images.githubusercontent.com/74416098/164014220-d90f2bbc-9ba1-402d-b7ee-80a458e58f6a.png) is the result, you would input `xcxxe`.

Example main:
```python
if __name__ == '__main__':
    breaker = WordleBreaker()
    while True:
        w = input("Try a word: ")
        r = input("What was the result? example if 'champ' and c was correct, h exists, a m p are wrong cexxx: ")
        potential = breaker.add_guess(w, r)
        print(potential)
        if len(potential) == 1:
            break
```

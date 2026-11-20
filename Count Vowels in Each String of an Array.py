fruits = ["apple", "mango", "kiwi", "grape"]
vowels = "aeiouAEIOU"

for fruit in fruits:
    count = 0
    for char in fruit:
        if char in vowels:
            count += 1
    print(f"{fruit} has {count} vowel(s)")

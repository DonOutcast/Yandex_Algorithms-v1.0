secret = input()
guess = input()

bulls = 0
cows = 0

in_secret = {}
in_guess = {}

for i in range(len(secret)):
    if secret[i] == guess[i]:
        bulls += 1
    else:
        in_secret[secret[i]] = in_secret.get(secret[i], 0) + 1
        in_guess[guess[i]] = in_guess.get(guess[i], 0) + 1

for digit in in_secret:
    if digit in in_guess:
        cows += min(in_secret[digit], in_guess[digit])

print(bulls, cows)



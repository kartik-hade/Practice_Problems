# Accept a string of lowercase letters from the user and encrypt it using the following image:
# Each letter in the string that appears in the the upper half should be replaced with the corresponding 
# letter in the lower half and vice versa. Print the encrypted string as output.

X = "abcdefghijklm"
Y = "zyxwvutsrqpon"
s = ""
word = input()
for i in word:
    if i in X:
        I = X.index(i)
        l += (Y[I])
    elif i in Y:
        I = Y.index(i)
        l += X[I]
print(s)
#!/usr/bin/python3
for alpha_letters in range(ord('a'), ord('z')+1):
# Breakout the letters we want to exclude
   if alpha_letters == 'e' or alpha_letters == 'q':
# Continue the alphabet Range
    continue
#Printing the Results
print("{:c}".format(alpha_letters), end="")

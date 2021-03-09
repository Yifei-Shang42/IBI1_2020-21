# pseudocode:
# define integer to record number of students of IBI1
# define r rate
# define an integer to carry number of rounds
# while number of rounds is less than 5:
#     calculate total infected number using r rate & infected number of last round
#     add 1 to number of rounds
# print a sentence containing r rate and number of total infected(converted to integer)

n = 84
r = 1.2
i = 0
while i < 5:
    n = n + n*r
    i += 1
print("When r rate = %.1f, after 5 rounds, the number of infected will be %d" \
      % (r,n))

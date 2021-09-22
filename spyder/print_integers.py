# print all integers from 1 to 10 including 1 & 10 using a for loop. 
#%%
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a) #just checking if I got it right
for integer in a:
    print(integer)

# better way to do it 
#%%
for i in range(1, 11) : # the range includes integers from 1 to 10, does not include 11 but includes 1. 
    print(i)


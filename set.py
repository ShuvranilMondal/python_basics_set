# s = {1,2,3}
# s.add(4)
# s.add(5)
# print(s)         # output = {1, 2, 3, 4, 5}


# lis = [2,13,3,1,2,2,3,13]
# print(list(set(lis)))                  # output = [1, 2, 3, 13]


# s = {1,2,3}
# s.remove(2)
# print(s)                               # output = {1, 3}


# s = {1,2,3}
# s.discard(2)                            # output = {1, 3}
# s.discard(4)                            # output = {1, 2, 3} // don't give error if your element not in prasent in set
# print(s)       


# l = {1,2,34,4}
# char = int(input("Enter charr "))
# if char in l:
#     print("present")
# else:
#     print("not present")               # input=2// output = present
# #------------------------------
# for i in l:
#     print(i,end = " ")                   # output = 1 2 34 4



s1 = {1,23,4,3,2,12,3}
s2 = {1,23,4,2,5,6}
print(s1 | s2)                        # union // output =  {1, 2, 3, 4, 5, 6, 12, 23}

print(s1 & s2)
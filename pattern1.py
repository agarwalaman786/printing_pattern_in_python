#printing pattern in python
#
# #
# # #
# # # #
# # # # #

for i in range(4):
    for j in range(4):
        if j>=0 and j<=i:
            print("# ",end="")
    print()


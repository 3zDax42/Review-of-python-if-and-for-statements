# Ezri
# 1/7/25
# Asks the number of lines cleared in tetris nad prints out tiers acording to score

tier = int(input("Enter the number of lines cleared in Tetris:"))
if tier < 100:
    print("Novice")
elif tier < 200:
    print("Intermediate")
elif tier < 300:
    print("Adcanced")
else:
    print("Expert")

# Prints out numbers 2 - 80 counting by tens
for i in range(2, 80, 10):
    print(i, end = " ")
print ("")

# Prints out numbers 100 - 10 counting down by 5
for i in range(100, 9, -5):
    print(i, end = " ")
print ("")

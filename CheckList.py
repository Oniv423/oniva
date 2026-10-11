total_chores = 3
original_count = total_chores
print(f"You have {original_count}chores to finsh today!\n")
completed_count = 0
chore_num = 1
while chore_num <= total_chores:
    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    else: next_chore = "Wash the dishes"
    answer = (f"Have you finshed: {next_chore}? (yes/no)")
    if answer == "yes":
        completed_count += 1
        chore_num += 1
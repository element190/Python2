print("Welcome to Online Quiz")
print("Ready to start")

score = 0
total_mark = 0	

for i in range(1,21):
	if i == 1:
		userchoice = int(input("Question 1: find the square root of 49? "))
		if userchoice == 7:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 2:
		userchoice = int(input("Question 2: find the square root of 121 ? "))
		if userchoice == 11:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 3:
		userchoice = int(input("Question 3: what is the square of 8? "))
		if userchoice == 64:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 4:
		userchoice = int(input("Question 4: find the square of 6? "))
		if userchoice == 36:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 5:
		userchoice = int(input("Question 5: find the square of 5? "))
		if userchoice == 25:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 6:
		userchoice = int(input("Question 6: find the square of 7? "))
		if userchoice == 49:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 7:
		userchoice = int(input("Question 7: find the square root of 121 ? "))
		if userchoice == 11:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 8:
		userchoice = int(input("Question 8: what is the square of 8? "))
		if userchoice == 64:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 9:
		userchoice = int(input("Question 9: find the square of 6? "))
		if userchoice == 36:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 10:
		userchoice = int(input("Question 10: find the square of 5? "))
		if userchoice == 25:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 11:
		userchoice = int(input("Question 11: find the square of 4? "))
		if userchoice == 16:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 12:
		userchoice = int(input("Question 12: find the square root of 121 ? "))
		if userchoice == 11:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 13:
		userchoice = int(input("Question 13: what is the square of 9? "))
		if userchoice == 81:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 14:
		userchoice = int(input("Question 14: find the square of 12? "))
		if userchoice == 144:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 15:
		userchoice = int(input("Question 15: find the square of 13? "))
		if userchoice == 169:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 16:
		userchoice = int(input("Question 16: find the square root of 49? "))
		if userchoice == 7:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 17:
		userchoice = int(input("Question 17: find the square root of 81 ? "))
		if userchoice == 9:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 18:
		userchoice = int(input("Question 18: what is the square of 4? "))
		if userchoice == 16:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	elif i == 19:
		userchoice = int(input("Question 19: find the square of 25? "))
		if userchoice == 625:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")
	else :
		userchoice = int(input("Question 20: find the square of 20? "))
		if userchoice == 400:
			print("Correct! Good Job")
			score = score + 1
		else:
			print("Wrong! Try Again")


total_mark += score

print("mark obtained is", total_mark)


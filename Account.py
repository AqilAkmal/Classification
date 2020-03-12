users = {
	"John" : {
		"password" : "john123",
		"age" : 24,
		"money" : 3000
	},
	"Alex" : {
		"password" : "alex123",
		"age" : 28,
		"money" : 2000
	}
}

instructions = ['check', 'exit', 'edit']
 
username = None
password = None
age = None
money = None

response = None
checking_account = None

def reset():
	global username
	global password
	global age
	global money
	global response
	global checking_account
	username = None
	password = None
	age = None
	money = None
	checking_account = False

def type_end_change():
	global change_info
	global end_change
	if change_info == 'password': return str(end_change)
	elif change_info == 'age': return int(end_change) # age can't be a string in the first place

system_on = True
log_in = False

while system_on:
	action = str(input("Do you want to log in or create new account? "))
	
	if 'log' in action:
		checking_account = True
		while checking_account:
			username = str(input('Username: '))
			if username not in users:
				print("Your username does not exist. Try again!")
			else:
				password = str(input('Password: '))
				if password != users[username]["password"]:
					print("Wrong password!")
				else:
					log_in = True

					while log_in:
						response = str(input('Hello, how may I help you? ')).lower()
						
						if 'check' in response:
							print(f'''
				Username: {username}
				Age: {users[username]["age"]}
				Money: ${users[username]["money"]}
							''')

						elif 'edit' in response:
							picking_change = True
							
							while picking_change:
								change_info = str(input('Which information do you want to change? [Password/Age] ')).lower()
								if change_info not in ['password', 'age']:
									print('You can only change \'password\' and \'age\'.')
								else:
									picking_change = False
									changing_info = True
									print(f'Your current {change_info} is {users[username][change_info]}. ')
									
									while changing_info:
										end_change = input(f'What do you want to change your {change_info} to? ')
										if type(type_end_change()) != type(users[username][change_info]): # Some changes need to be made
											print(type(type_end_change()))
											print(type(users[username][change_info]))
											print('Age must be a number!')
										else:
											changing_info = False
											users[username][change_info] = end_change
											print(f'{username}, your new {change_info} is {users[username][change_info]}.')

						elif 'transfer' in response:
							picking_receiver = True

							while picking_receiver:
								receiver = str(input('Who do you want to transfer your money to? '))
								if receiver not in users:
									print('The user does not exist. Please try again.')
								else:
									picking_receiver = False
									choosing_amount = True

									while choosing_amount:
										print(f'You have ${users[username]["money"]} in your bank account.')
										amount = int(input(f'How much money do you want to transfer to {receiver}? $'))
										if amount > users[username]["money"]:
											print('''
				You do not have enough money!''')
										else:
											choosing_amount = False
											users[username]["money"] -= amount
											users[receiver]["money"] += amount
											print(f'''
				You have successfully transfered ${amount} to {receiver}.''')
											print(f'You have ${users[username]["money"]} left.')

						elif 'exit' in response:
							print('Thank you for using RHX Bank!')
							log_in = False
							reset()

						elif response not in instructions:
							print('Type: 1. CHECK: See your account details. 2. EDIT: Edit your account details. 3. EXIT: Exit the system.')

	elif 'new' in action:
			new_name = str(input('Create a new username (case sensitive): '))
			setting_password = True

			while setting_password:
				new_password = str(input('Set a strong password: '))
				if len(new_password) < 6:
					print('Password must be more than 6 characters!')
				else:
					setting_password = False
					entering_age = True
					
					while entering_age:
						new_age = int(input('Enter your age: '))
						if new_age < 18:
							print('Must be 18+ to apply an account!')
						else:
							entering_age = False
							new_deposit = int(input('First deposit: '))
							users[new_name] = {"password" : new_password, "age" : new_age, "money" : new_deposit}
							print(f'{new_name}, your age is {new_age} and your first deposit ${new_deposit}.')
							
							end_reply = str(input('Reply \'ok\' to confirm!')).lower()
							if end_reply == 'ok':
								print('Thank you for applying!')
							else:
								print('Sorry your application is invalid!')
								del users[new_name]
	
	elif 'exit' in action:
		system_on = False

print(users)

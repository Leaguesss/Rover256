from loader import *
def quit():
	"""
	Will quit the program
	"""
	pass

def menu_help():
	"""
	Displays the help menu of the game
	"""
	print("\nSTART <level file> - Starts the game with a provided file.\nQUIT - Quits the game\nHELP - Shows this message\n")
def menu_start_game(filepath):
	"""
	Will start the game with the given file path
	"""
	boolean, rover = load_level(filepath)
	if boolean != True:
		print('')
		print(rover)
		print('')
		return None
	while True:
		line = input().strip()
		command, *right = line.split(" ", 1)
		if command == 'SCAN':
			if not right or right[0] not in ('shade', 'elevation'):
				print("\nCannot perform this command\n")
			else:
				rover.scan(right[0].strip())
		elif command == 'MOVE':
			if not right:
				print("\nCannot perform this command\n")
			else:
				line = right[0].strip() # get the direction
				try:
					direction, cycles = line.split(' ')
					cycles = int(cycles)
				except:
					print("\nCannot perform this command\n")
					continue
				if direction not in ('N', 'E', 'S', 'W'):
					print("\nCannot perform this command\n")
					continue
				rover.move(direction, cycles)
		elif command == 'WAIT':
			if not right:
				print("\nCannot perform this command\n")
			else:
				try:
					cycles = int(right[0])
				except:
					print("\nCannot perform this command\n")
					continue
				# add battery
				rover.wait(cycles)
		elif command == 'STATS' and not right:
			rover.stats()
		elif command == 'FINISH' and not right:
			rover.finish()
			break
		else:
			print("\nCannot perform this command\n")

def menu():
	"""
	Start the menu component of the game
	"""
	while True:
		line = input().strip()
		command, *right = line.split(' ', 1)
		
		if command == 'HELP':
			menu_help()
		elif command == 'QUIT':
			break
		elif command == 'START' and right:
			# start the game
			menu_start_game(right[0].strip())
		else:
			print("\nNo menu item\n")

if __name__ == "__main__":
	menu()

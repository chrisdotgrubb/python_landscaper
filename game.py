teeth = {
	'name': 'teeth',
	'cost': 0,
	'earn': 1
}
scissors = {
	'name': 'scissors',
	'cost': 5,
	'earn': 5
}
push = {
	'name': 'push mower',
	'cost': 25,
	'earn': 50
}
battery = {
	'name': 'battery powered lawnmower',
	'cost': 250,
	'earn': 100
}
students = {
	'name': 'students',
	'cost': 500,
	'earn': 250
}

current_tools = [teeth]
available_tools = [scissors, push, battery, students]

day = 0
money = 0
lifetime_earnings = 0
tool = current_tools[0]


def print_current_tool(t):
	print(f'''"use {t['name']}" to earn ${t['earn']} / day.''')


def print_available_tools(t):
	print(f'''"buy {t['name']}" for ${t['cost']} to earn ${t['earn']} / day.''')


while not (money >= 1000 and students in current_tools):
	print()
	selection = input('please make a selection:\n').lower()
	if selection == 'menu' or selection == 'help':
		print('''---------------
"menu" for these options
"tool" to see the tool you are using
"current tools" to see tools you own
"available tools" to see tools you can buy
"money" to see current money in your pocket
"mow" to mow the lawn for the day using your tool
"goal" to see your objective for winning
"buy TOOL" to buy chosen tool
"use TOOL" to equip chosen tool
"restart" to restart game
---------------''')
	
	elif selection == 'tool':
		print('---------------')
		print(f'Using {tool["name"]}. "mow" to earn ${tool["earn"]}')
		print('---------------')
	elif selection == 'current tools':
		print('---------------')
		[print_current_tool(cur_tool) for cur_tool in current_tools]
		print('---------------')
	elif selection == 'available tools':
		print('---------------')
		[print_available_tools(avail_tool) for avail_tool in available_tools]
		print('---------------')
	
	elif selection == 'money':
		print('---------------')
		print(f'Current: ${money}')
		print(f'Total earned: ${lifetime_earnings}')
		print('---------------')
	elif selection == 'mow':
		print('---------------')
		money += tool['earn']
		lifetime_earnings += tool['earn']
		day += 1
		print(f'''You earned ${tool['earn']}\nPocket: {money}''')
		print('---------------')
	elif selection == 'goal':
		print('---------------')
		print('Hire students and save $1000')
		print('---------------')
	elif selection.startswith('buy'):
		if 'tool' in selection:
			print('---------------')
			print('not literally "TOOL"!\n"available tools" will help')
			print('---------------')
		else:
			tool_to_buy = None
			if 'teeth' in selection:
				tool_to_buy = teeth
			elif 'scis' in selection:
				tool_to_buy = scissors
			elif 'push' in selection:
				tool_to_buy = push
			elif 'batt' in selection:
				tool_to_buy = battery
			elif 'stud' in selection:
				tool_to_buy = students
				
			if not tool_to_buy:
				print('---------------')
				print('invalid selection, "available tools" will help')
				print('---------------')
			else:
				if tool_to_buy in available_tools:
					if money >= tool_to_buy['cost']:
						money -= tool_to_buy['cost']
						available_tools.remove(tool_to_buy)
						current_tools.append(tool_to_buy)
						print('---------------')
						print(f'''Bought {tool_to_buy['name']}! "use {tool_to_buy['name']}" to equip''')
						print(f'''-${tool_to_buy['cost']}\nCurrent money: ${money}''')
						print('---------------')
					else:
						print('---------------')
						print('insufficient funds, get back to mowing')
						print('---------------')
				else:
					print('---------------')
					print(f'''you already own {tool_to_buy['name']}. "use {tool_to_buy['name']}" to equip''')
					print('---------------')
					
	elif selection.startswith('use'):
		if 'tool' in selection:
			print('---------------')
			print('not literally "TOOL"!\n"current tools" will help')
			print('---------------')
		else:
			tool_to_use = None
			if 'teeth' in selection:
				tool_to_use = teeth
			elif 'scis' in selection:
				tool_to_use = scissors
			elif 'push' in selection:
				tool_to_use = push
			elif 'batt' in selection:
				tool_to_use = battery
			elif 'stud' in selection:
				tool_to_use = students
				
			if not tool_to_use:
				print('---------------')
				print('invalid selection, "current tools" will help')
				print('---------------')
			else:
				if tool_to_use == tool:
					print('---------------')
					print('already selected')
					print('---------------')
				elif tool_to_use in current_tools:
					tool = tool_to_use
					print('---------------')
					print(f'''now using {tool['name']}, "mow" to earn {tool['earn']}''')
					print('---------------')
				else:
					print('---------------')
					print(f'''you do not own {tool_to_use['name']}. "buy {tool_to_use['name']}" to purchase''')
					print('---------------')
	elif selection == 'restart':
		current_tools = [teeth]
		available_tools = [scissors, push, battery, students]
		
		day = 0
		money = 0
		lifetime_earnings = 0
		tool = current_tools[0]
		print('---------------')
		print('restarting...')
		print('---------------')
		
	else:
		print('---------------')
		print('invalid selection\n"menu" for options')
		print('---------------')

print('---------------')
print(f'''you won in {day} days''')
print('---------------')

def property_tax():
	actual_value = float(input("Enter the actual value: "))
	assessed_value = actual_value * .60
	property_tax = (assessed_value / 100) * .72
	print ("Assessed value: $", format(assessed_value, '.2f'))
	print ("Property tax: $", format(property_tax, '.2f'))
property_tax()

def future_value():
    P = float(input("Enter the present value of the account in dollars: "))
    i = float(input("Enter the monthly interest rate as a percentage: "))
    t = float(input("Enter the number of months: "))
    I = i * .01
    F = P * (1 + I) ** t
    print ("The information for you account is: ")
    print ("Present value: $", P)
    print ("Interest Rate: %", i)
    print ("After ", t, " months the value of your account will be $", format(F, '.2f'))
future_value()

def genz_search():

    with open("GirlNames.txt", "r") as girl_names:
    	content_girls = girl_names.readlines()

    content_girls = [x.strip('\n') for x in content_girls]

    with open("BoyNames.txt", "r") as boy_names:
    	content_boys = boy_names.readlines()

    content_boys = [x.strip('\n') for x in content_boys]

    user_boy = input("Enter a boy's name, or N if you do not wish to enter a boy's name: ")
    user_girl = input("Enter a girl's name, or N if you do not wish to enter a girl's name: ")

    if user_boy == "N" or user_boy == "n":
    	print("You chose not to enter a boy's name.")
    else:
    	if user_boy in content_boys:
    		print(user_boy + " is one of the most popular boy's names.")
    	elif user_boy not in content_boys:
    		print(user_boy + " is not one of the most popular boy's names.")

    	if user_girl == 'N' or user_girl == 'n':
    		print("You chose not to enter a girl's name.")
    	else:
    		if user_girl in content_girls:
    			print(user_girl + " is one of the most popular girl's names.")
    		elif user_girl not in content_girls:
    			print(user_girl + " is not one of the most popular girl's names.")
genz_search()

def prime_gen():
	num_input = int(input ("Enter an integer greater than 1: "))
	
	for i in range(2,num_input + 1):
		num = 0
		for j in range(2, i):
			if (i % j) == 0:
				num = 1
		if (num==0):
			print (i, "is prime. ")
				
		elif (num==1):
			print (i, "is composite")
prime_gen()

def tirole_noble():

	def get_word_dict(): 
		line=line.strip('\r\n').lower()
		return line.split()
def add (word_locations, word, lineno):
	if word_locations.get(word, None) is None:
		word_locations[word] = [lineno]
	elif lineno in word_locations[word]:
		pass
	else:
		word_locations[word].append(lineno)
		return word_locations

	file = 'index.txt'
	word_locations = {}
	with open("tirole_noble.txt", "r", encoding='utf-8') as f:
		for lineno, line in enumerate (f,1):
			wordslist = get_words(line)
			for word in wordslist:
				word_locations.update(add(word_locations, word, lineno))
	with open('index.txt', "w",) as f:
		for key in sorted(word_locations):
			f.write(key + ':' ''.join(map(str, word_locations[key])) + '\n')
	if__name__=='__tirole_noble__'
tirole_noble()

def pow_recursive(x, y):
	if y == 0:
		return 1
	elif y%2 == 0:
		c= pow(x,y/2)
		return c*c
	else:
		return x*pow(x,y-1)
pow_recursive()



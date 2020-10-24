import sys

def printHello():
	print("hello to you too!")

def getInput():
	# input('Say hi to me!  ')  #python3
	raw_input('Say hi to me!  ') #python2


def main():
	getInput()
	printHello()

if __name__ == "__main__":
	main()
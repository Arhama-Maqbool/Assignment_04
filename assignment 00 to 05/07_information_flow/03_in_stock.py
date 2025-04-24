def main():
	fruit : str = input("\n\033[1;3mEnter a fruit: \033[0m")
	stock = num_in_stock(fruit)
	if stock == 0:
		print("\nThis fruit is not in stock.")
	else:
		print("\nThis fruit is in stock! Here is how many:")
		print(stock)


def num_in_stock(fruit):
	"""
	This function returns the number of fruit Sophia has in stock.
	"""
	if fruit == 'apple':
		return 2
	if fruit == 'mango':
		return 4
	if fruit == 'pear':
		return 1000
	else:
		return 0


if __name__ == '__main__':
    main()
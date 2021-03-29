def fibonacci(numToGenerate):

	array = [1, 1]

	for i in range(0, numToGenerate-2):

		arrayLength = len(array)

		number = array[arrayLength - 2] + array[-1]

		array.append(number)

	print(array)
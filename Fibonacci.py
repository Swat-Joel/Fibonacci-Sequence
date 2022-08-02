Array = [0, 1]
print(Array[0])
print(Array[1])

def Fibonacci():
	result = Array[-1] + Array[-2]
	Array.append(result)
	print(result)

counter_Fibonacci = 0
while counter_Fibonacci <= 10: # Number of times it executes
	Fibonacci()
	counter_Fibonacci = counter_Fibonacci + 1

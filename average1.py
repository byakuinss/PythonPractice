
number = input("enter a number or Enter to finish: ")
numbers = []

while number != "":
  numbers.append(number)
  number = input("enter a number or Enter to finish: ")

def getCount(numbers):
  return len(numbers)

def getSum(numbers):
  result = 0
  for number in numbers:
    result += int(number)
  return result

def getLowest(numbers):
  return min(numbers)
def getHighest(numbers):
  return max(numbers)
def getMean(numbers):
  result = 0
  for number in numbers:
    result += int(number)
  return int(result / len(numbers))


print(numbers)
print("count = " + str(getCount(numbers)) + ", sum = " + str(getSum(numbers)) + ", lowest = " + str(getLowest(numbers)) + ", highest = " + str(getHighest(numbers)) + ", mean = " + str(getMean(numbers)))
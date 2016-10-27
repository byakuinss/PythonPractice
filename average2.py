
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

def getMid(numbers):
  result = 0
  temp = 0

  #sort 
  for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] > numbers[j]: 
        temp = numbers[i]
        numbers[i] = numbers[j]
        numbers[j] = temp
  mid = int(len(numbers)/2)

  if len(numbers) % 2 == 1:
    result = numbers[mid]
  else:
    result = (int(numbers[mid]) + int(numbers[mid + 1])) / 2

  return result


print(numbers)
print("count = " + str(getCount(numbers)) + ", sum = " + str(getSum(numbers)) + ", lowest = " + str(getLowest(numbers)) + ", highest = " + str(getHighest(numbers)) + ", mean = " + str(getMean(numbers)))
print("midian = " + str(getMid(numbers)))
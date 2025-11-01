#Task 2: Lists and Arrays

#2.1: Create a list of 10 random integers
lis = [random.randint(1,25) for _ in range(10)]
print("Original List:", lis)

#2.2:Perform the following operations:

#2.2.1:Add and remove elements.
`
lis.append(26) #add
print("List after adding:",lis)

lis.remove(lis[5])
print("List after Removing:",lis) #remove

#2.2.2 Find the maximum and minimum values.

print("Max Value:", max(lis))
print("Min Value:", min(lis))

#2.2.3 Sort the list
lis.sort()
print("Sorted List:",lis)

# 2.3: Convert the list into a NumPy array
import numpy as np
arr=np.array(lis)

#2.3.1 Mean, Median, and Standard Deviation. 

mean = np.mean(arr)
median = np.median(arr)
stddev = np.std(arr)

print("\n NumPy Calculations")
print("Mean:", round(mean, 2))
print("Median:", median)
print("Standard Deviation:", round(stddev, 2))


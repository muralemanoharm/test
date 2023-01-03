n = list(map(int, input("Enter the elements in array: ").split()))
c = int(input("Enter the no to cycle the array: "))
cyc = n[-c:]
cyc.reverse()
non_cyc = n[:-c]
print(cyc + non_cyc)


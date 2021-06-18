with open('devops.txt', 'a') as file:
    j = [11,22,13,14,35,66,7,18,19]
    for i in range(1,6):
       file.write(f"\n Adding {i} more ATA friend ")
       file.writelines([f" Friend {i} has written {j[i]} posts so far"])
       i = i+1


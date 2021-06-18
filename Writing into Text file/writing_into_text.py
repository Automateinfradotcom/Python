# Open the file for appending (a) and begin reading each line
with open('devops.txt', 'a') as file:
     file.write("\nAdding 5 more ATA friend")
     file.writelines(['\nAdding 5 more ATA friend', '\nAdding 15 more ATA friend'])
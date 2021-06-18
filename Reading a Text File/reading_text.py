with open('devops.txt', 'r') as a:
      read_content = a.read()
with open('devops.txt', 'r') as b:
      read_char = b.read(5)
with open('devops.txt', 'r') as c:
      read_line_by_line = c.readline()
      print(read_content)
      print(read_char)
      print(read_line_by_line)
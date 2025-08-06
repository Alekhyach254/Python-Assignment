def append_and_read_last_lines(file_path, new_line):

    with open(file_path, 'a') as file:
        file.write(new_line + '\n')

    with open(file_path, 'r') as file:
        lines = file.readlines()
        last_3_lines = lines[-3:]  

    return last_3_lines

file_path = 'word.txt'
new_line = 'I hope to join team soon.'

last_lines = append_and_read_last_lines(file_path, new_line)
print('Last 3 lines of the file:')
for line in last_lines:
    print(line.strip())
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as text:
        file_content = text.readlines()
    return ''.join(file_content)


file_list = ['text1.txt', 'text2.txt', 'text3.txt']
sorted_file_list = sorted(file_list, key=len)
with open('final.txt', 'w') as output:
        output.write(f'{sorted_file_list[0]}\n{len(read_file(sorted_file_list[0]))}\n')
        output.write(read_file(sorted_file_list[0]))
for file in sorted_file_list:
    file_content = read_file(file)
    output.write(f'{file}\n{len(file_content)}\n')
    output.write(file_content)
output.close()

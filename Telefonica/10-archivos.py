from io import open

def read_n_lines(file, n):
    file.seek(0)
    return file.readlines()[:n]

def encrypt_file(src, dest):
    src.seek(0)
    original_text = src.readlines()
    for line in original_text:
        encrypted_line = ""
        for i in line:
            if i >= 'a' and i <= 'z':
                encrypted_line += chr((ord(i) + 13) % 26)
            else:
                encrypted_line += i
        dest.write(encrypted_line)

file = open("test_file1.txt", "w+")
file.write("1\n2\n3\n4\n5\nmiau")
print(read_n_lines(file, 4))

encrypted_file = open("test_file2.txt", "w+")
encrypt_file(file, encrypted_file)
encrypted_file.seek(0)
print(encrypted_file.readlines())
file.close()
encrypted_file.close()

# Program 1: Print alternate elements of a list
lst = input("Enter a list of elements separated by space: ").split()
print("Alternate elements of the list are:", lst[::2])

# Program 2: Reverse the content of a list without using reverse()
lst = input("Enter a list of elements separated by space: ").split()
reversed_list = lst[::-1]
print("Reversed list:", reversed_list)

# Program 3: Find the largest number in a list without using max()
lst = list(map(int, input("Enter numbers separated by space: ").split()))
largest = lst[0]
for num in lst:
    if num > largest:
        largest = num
print("The largest number in the list is:", largest)

# Program 4: Rotate elements of a list
lst = input("Enter a list of elements separated by space: ").split()
rotated_list = lst[1:] + lst[:1]
print("Rotated list:", rotated_list)

# Program 5: Delete a given word from a string
string = input("Enter a string: ")
word_to_delete = input("Enter the word to delete: ")
modified_string = string.replace(word_to_delete, "")
print("String after deleting the word:", modified_string)

# Program 6: Convert date format from mm/dd/yyyy to Month day, year
date = input("Enter a date in mm/dd/yyyy format: ")
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
mm, dd, yyyy = map(int, date.split("/"))
print(f"{months[mm - 1]} {dd}, {yyyy}")

# Program 7: Capitalize the first letter of each word in a string
def capitalize_words(sentence):
    return " ".join(word.capitalize() for word in sentence.split())
sentence = input("Enter a sentence: ")
print("Capitalized sentence:", capitalize_words(sentence))

# Program 8: Find the sum of each row in a matrix
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
print("Enter the matrix row by row:")
for _ in range(rows):
    matrix.append(list(map(int, input().split())))
for i, row in enumerate(matrix, start=1):
    print(f"Sum of row {i} =", sum(row))

# Program 9: Add two matrices
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print("Enter the first matrix:")
matrix1 = [list(map(int, input().split())) for _ in range(rows)]
print("Enter the second matrix:")
matrix2 = [list(map(int, input().split())) for _ in range(rows)]
result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
print("Resultant matrix:")
for row in result:
    print(*row)

# Program 10: Multiply two matrices
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))
if cols1 != rows2:
    print("Matrix multiplication is not possible.")
else:
    print("Enter the first matrix:")
    matrix1 = [list(map(int, input().split())) for _ in range(rows1)]
    print("Enter the second matrix:")
    matrix2 = [list(map(int, input().split())) for _ in range(rows2)]
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    print("Resultant matrix:")
    for row in result:
        print(*row)
import fitz
import csv

pdf_path = '1980_UrbanaChampaign.pdf'
doc = fitz.open(pdf_path)
rows = []
for page in doc:
    words = page.get_text_words()
    rows += words

rows.sort(key=lambda w: (w[3], w[0]))

columns = []
current_column = []
previous_word_x = None
for word in rows:
    if previous_word_x is not None and abs(word[0] - previous_word_x) > 5:
        columns.append(current_column)
        current_column = []
    current_column.append(word)
    previous_word_x = word[0]
columns.append(current_column)

# Concatenating the words in each column into a single string
columns_text = []
for column in columns:
    column_text = ""
    for word in column:
        column_text += word[4] + " "
    columns_text.append(column_text)

column1 = []
column2 = []
column3 = []
for word in rows:
    if word[0] < 200:
        column1.append(word[4])
    elif word[0] < 400:
        column2.append(word[4])
    else:
        column3.append(word[4])

# Printing the contents of each column
print("Column 1:", " ".join(column1))
print("Column 2:", " ".join(column2))
print("Column 3:", " ".join(column3))

# Storing the contents of each column in a list
data = []
max_len = max(len(column1), len(column2), len(column3))
for i in range(max_len):
    row = []
    if i < len(column1):
        row.append(column1[i])
    else:
        row.append("")
    if i < len(column2):
        row.append(column2[i])
    else:
        row.append("")
    if i < len(column3):
        row.append(column3[i])
    else:
        row.append("")
    data.append(row)

# Write the data to a CSV file
columns = ["Column 1", "Column 2", "Column 3"]
with open("output3.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(columns)
    for row in data:
        writer.writerow(row)


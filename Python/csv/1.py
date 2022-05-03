import csv

# with open('./1.csv', newline='', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

with open('./1.csv', 'a', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['4', '猫砂', '25', '1022', '886'])
    writer.writerow(['5', '猫罐头', '18', '2234', '3121'])

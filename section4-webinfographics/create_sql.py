import csv
lines = []
with open('csv/csv_entuty.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        
        line = ', '.join(row)
        print(line)
        lines.append(line)


# def add_brakets(line):
#     return '(' + line + "),"


# sql = list(map(add_brakets, lines))

# table_name = 'entities'
# sql_file = f"insert into {table_name}  {sql[0][:-1]} values "
# for line in sql[1:]:
#     print(line)
#     sql_file += line+'\n'

# sql_file = sql_file[:-2] + ';'
# # print(sql_file)
# print("sql generated")

# file_name = f'data_{table_name}.sql'
# # print(file_name)

# with open(file_name, 'w') as file:
#     file.write(sql_file)

# print("sql file generated")

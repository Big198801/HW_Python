def print_operation_table(operation, num_rows = 6, num_columns = 6): 
    for x in range(1, num_rows + 1): 
        row = [] 
        for y in range(1, num_columns + 1): 
            row.append(str(operation(x, y))) 
        print(*row, sep="\t") 
 

print_operation_table(lambda x, y: x * y)
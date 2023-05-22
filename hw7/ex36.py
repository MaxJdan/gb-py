def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range(1, num_rows + 1):
        lists = []
        for y in range(1, num_columns + 1):
            num = operation(x, y)
            lists.append(num)
        print(*[str(x) for x in lists])
print_operation_table(lambda x, y: x * y )
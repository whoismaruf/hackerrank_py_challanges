def print_fun(n):
    if n in range(1, 150):
        final_string = []
        for i in range(1, n+1):
            final_string.append(str(i))
        return "".join(final_string)
    else:
        print("Out of memory!")

print(print_fun(5))
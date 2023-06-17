def input_array(arr, n):
    if n == 0:
        return
    input_array(arr, n - 1)
    arr[n - 1] = int(input(f"Enter element {n}: "))

def output_array(arr, n):
    if n == 0:
        return
    output_array(arr, n - 1)
    print(arr[n - 1])
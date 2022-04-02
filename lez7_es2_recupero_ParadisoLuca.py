def main():
    fin = open("ex2_data_python_4.txt", "r")
    x_g = 0
    y_g = 0
    n = 0

    for line in fin:
        x,y = line.split()
        x = float(x)
        y = float(y)
        x_g += x
        y_g += y
        n += 1
    x_g = x_g / n
    y_g = y_g / n
    print(f"Baricentro: ({x_g}, {y_g})")

main()

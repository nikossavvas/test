while True:
    number = int(input("Enter n (1-20): "))

    if number == 0:
        print("End")
        break
    elif 0 < number <= 20:
        # rows
        number_of_cols = (2*number)+2
        for row in range(1, number+1):
            # columns
            for column in range(1, number_of_cols):
                if column <= row or column+row >= number_of_cols:
                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print("\r")
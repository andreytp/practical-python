last_height = 100
for i in range(1,11):
    last_height = last_height * 3 / 5
    print(f'bounce {i}, height {round(last_height, 4)}')
def read_numbers():
    try:
        with open("numbers.txt", "r") as file:
            data = file.read()
        data = data.replace("\n", "").split(",")
        for num in data:
            print(num)
    except FileNotFoundError:
        print("Error: 'numbers.txt' file not found.")

if __name__ == "__main__":
    read_numbers()
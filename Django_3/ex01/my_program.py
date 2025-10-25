from path import Path



if __name__ == "__main__":
    mypath = Path('created_directory')
    mypath.mkdir()

    file = mypath / 'my_file.txt'
    file.write_text('Hello, World! This is test for path module.\n')
    print(file.read_text())

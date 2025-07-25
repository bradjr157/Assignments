def read_and_write_file(filename):
    try:
        #Read The File
        with open(filename, 'r') as file:
            contents = file.read()

            #Modify The Contents
            modified_contents = contents.upper()

            #Write The Modified Contents To A New File
            new_filename = f"modified_{filename}"
            with open(new_filename, 'w') as new_file:
                new_file.write(modified_contents)   

                print(f"Modified contents written to {new_filename}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read or write the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main ():
    filename = input("Enter the filename: ")
    read_and_write_file(filename)

if __name__ == "__main__":
    main()
    
                      

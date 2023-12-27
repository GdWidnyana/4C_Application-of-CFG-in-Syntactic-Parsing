# Define the baca_file function
def baca_file(filepath):
    # Prepare an empty list
    data = []
    
    # Open the text file in read mode
    with open(filepath, 'r') as file: 
        # Read each line of the rules
        raw = file.readlines()

        # Add each rule to the data list and remove the newline character
        for rule in raw:
            data.append(rule.strip('\n'))

    # Return the raw CNF rules
    return data

# Specify the file path
filepath = 'data/4c_CNF.txt'

try:
    # Call the baca_file function with the specified file path
    data_cnf = baca_file(filepath)

    # Now data_cnf contains the content of the file '4c_CNF.txt'
    # You can perform further operations with the data_cnf variable as needed
    print("Content of '4c_CNF.txt':")
    for rule in data_cnf:
        print(rule)
except FileNotFoundError as e:
    print(e)

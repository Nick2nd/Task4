import os

# Base directory
base_directory = "/home/lexie/CodeCamp_Task4"

# Define users and their groups
users = {
    "Andrew": "System_Administrator",
    "Julius": "Legal",
    "Chizi": "Human_Resource_Manager",
    "Jeniffer": "Sales_Manager",
    "Adeola": "Business_Strategist",
    "Bach": "CEO",
    "Gozie": "IT_intern",
    "Ogochukwu": "Finance_Manager"
}

# Define directories
directories = [
    "Finance Budgets",
    "Contract Documents",
    "Business Projections",
    "Business Models",
    "Employee Data",
    "Company Vision and Mission Statement",
    "Server Configuration Script"
]

# Function to create a group
def create_group(group):
    try:
        os.system(f'sudo groupadd {group}')
        print(f'Group {group} created.')
    except Exception as e:
        print(f'Error creating group {group}: {e}')

# Function to create a user and assign them to a group
def create_user(username, group):
    try:
        os.system(f'sudo useradd {username}')
        os.system(f'sudo usermod -aG {group} {username}')
        print(f'User {username} created and added to group {group}.')
    except Exception as e:
        print(f'Error creating user {username}: {e}')

# Function to create a directory
def create_directory(directory):
    try:
        dir_path = os.path.join(base_directory, directory)
        os.makedirs(dir_path, exist_ok=True)
        print(f'Directory {dir_path} created.')
    except Exception as e:
        print(f'Error creating directory {directory}: {e}')

# Function to create a file in a specified directory
def create_file():
    file_name = input("Enter the name of the file: ")
    directory_name = input("Enter the directory to create the file in: ")

    if directory_name in directories:
        file_path = os.path.join(base_directory, directory_name, file_name)
        with open(file_path, 'w') as file:
            file.write("")  # Creates an empty file
        print(f'File {file_name} created in directory {directory_name}.')
    else:
        print(f'Directory {directory_name} does not exist. File not created.')

# Main function to run the script
def main():
    # Ensure the base directory exists
    os.makedirs(base_directory, exist_ok=True)
   
    # Create groups
    for group in set(users.values()):
        create_group(group)
   
    # Create users and assign them to their groups
    for user, group in users.items():
        create_user(user, group)
   
    # Create directories
    for directory in directories:
        create_directory(directory)
   
    # Create a file based on user input
    create_file()

if __name__ == "__main__":
    main()
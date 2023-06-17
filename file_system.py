
#BELOW CODE IS ONLY TO GET THE PROGRAM STARTED
program_run = True
initialize = False
whitespace = ' '

while not initialize:
    username = input('enter a name for your home folder below \n').lower()
    if whitespace in username:
        valid_username = ''
        print(f'Run Error: "{username}" is invalid. Username must be one position. Use "_" to concatenate')
        user_list = username.split(' ')
        for i in range(0, len(user_list)):
            valid_username += user_list[i]
            if i + 1 < len(user_list):
                valid_username += '_'
        print(f'>>>>>>>>>>> example username: {valid_username}')
    else:
        initialize = True

#CODE BELOW MUST REMAIN CONSISTENT THROUGHOUT FUNCTIONS
current_folder = (rf'C:\users\{username}')
current_folder_title = current_folder.split('\\')[-1]
file_system = {f'{current_folder}': ['downloads', 'pictures', 'documents', 'music'],
                rf'C:\users\{username}\downloads': ['example_file.txt'],
                rf'C:\users\{username}\pictures': ['example_file.txt'],
                rf'C:\users\{username}\documents': ['example_file.txt'],
                rf'C:\users\{username}\music': ['example_file.txt']
               }

#DIRECTORIES IS ONLY FOR REFERENCE
# directories = {'home': ['downloads',
#                        'pictures',
#                        'documents',
#                        'music',]
#                        }

# starting_dir = (rf'C:\users\{username} > ')


#BELOW CODE WILL BE FUNCTIONS LS, MKDIR, CD, AND TOUCH,
def ls():
    global current_folder
    for folder in file_system[current_folder]:
        print(folder)


def mkdir():
    global current_folder
    example = ''
    
    new_folder_title = argument.split(' ')[1].lower()
    new_folder = f'{current_folder}\{new_folder_title}'
    if len(argument.split(' ')) > 2:
        print(f'mkdir Usage: Input "{argument}" invalid. folder name must be one position. Use "_" to concatenate')
        example_list = argument.split(' ')
        for i in range(1, len(example_list)):
            example += example_list[i]
            if i + 1 < len(example_list):
                example += '_'
        print(f'>>>>>>>>>>> example folder name: {example}')
    elif new_folder in file_system:
        print('mkdir Usage: Folder already exists')
            
    else:
        file_system[f'{new_folder}'] = []
        file_system[f'{current_folder}'].append(new_folder_title)
    
def cd():
    global current_folder
    if argument == 'cd':
        current_folder = ' '
        current_folder = (rf'C:\users\{username}')
    elif argument.split(' ')[1].lower() in file_system[current_folder]:
        change_dir_to = argument.split(' ')[1].lower()
        current_folder += f'\{change_dir_to}'
    else:
        change_dir_to = argument.split(' ')[1].lower()
        print(rf'cd: Cannot find path C:users\{username}\{change_dir_to} because it does not exist')

def touch():
    global current_folder
    example = ''
    new_file = argument.split(' ')[1].lower() + '.txt'
    if len(argument.split(' ')) > 2:
        print(f'touch Usage: Input "{argument}" invalid. File name must be one position. Use "_" to concatenate')
        example_list = argument.split(' ')
        for i in range(1, len(example_list)):
            example += example_list[i]
            if i + 1 < len(example_list):
                example += '_'
        print(f'>>>>>>>>>>> example file name: {example}')
    elif new_file in file_system[current_folder]:
        print(f'{new_file} Overwritten')
    else:
        file_system[current_folder].append(new_file)

#BELOW CODE WILL KEEP PROGRAM IN LOOP TO MANIPULATE DIRECTORIES UNTIL EXIT 
while program_run:
    
    argument = input(f'\n{current_folder} > ').lower()
    argument_split = argument.split()
    if argument_split[0] == 'ls':
        if len(argument_split) == 1:
            ls()
        else:
            print(f'Command not found: {argument}')
    elif argument_split[0] == 'mkdir':
        if len(argument_split) > 1:
            mkdir()
        else:
            print('mkdir Usage: mkdir requires a folder name after the command is called')
    elif argument_split[0] == 'cd':
        cd()
    elif argument_split[0] == 'touch':
        if len(argument_split) > 1:
            touch()
        else:
            print('touch Usage: touch requires a file name after the command is called')
    elif argument_split[0] == 'exit':
        program_run = False
    else:
        print(f'Command not found: {argument}')

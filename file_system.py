
#BELOW CODE IS ONLY TO GET THE PROGRAM STARTED
program_run = True
initialize = False
whitespace = ' '

while not initialize:
    username = input('enter a name for your home folder below \n').title()
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
home_dir = (rf'C:\users\{username}')
current_dir_title = home_dir.split('\\')[-1]
current_dir = {f'{home_dir}': ['downloads', 'pictures', 'documents', 'music'],
                rf'C:\users\{username}\downloads': ['example_file.txt'],
                rf'C:\users\{username}\pictures': ['example_file.txt'],
                rf'C:\users\{username}\documents': ['example_file.txt'],
                rf'C:\users\{username}\music': ['example_file.txt']
               }

#DIRECTORIES IS ONLY FOR REFERENCE
directories = {'home': ['downloads',
                       'pictures',
                       'documents',
                       'music',]
                       }

starting_dir = (rf'C:\users\{username} > ')

program_count = 0

#BELOW CODE WILL BE FUNCTIONS LS, MKDIR, CD, AND TOUCH,
def ls():
    global home_dir
    for folder in current_dir[home_dir]:
        print(folder)
    
def mkdir():
    global home_dir
    example = ''
    
    new_folder_title = argument.split(' ')[1].lower()
    new_folder = f'{home_dir}\{new_folder_title}'
    if argument == 'mkdir':
        print('mkdir Usage: mkdir requires a folder name after the command is called')
    elif len(argument.split(' ')) > 2:
        print(f'mkdir Usage: Input "{argument}" invalid. folder name must be one position. Use "_" to concatenate')
        example_list = argument.split(' ')
        for i in range(1, len(example_list)):
            example += example_list[i]
            if i + 1 < len(example_list):
                example += '_'
        print(f'>>>>>>>>>>> example folder name: {example}')
    elif new_folder in current_dir:
        print('mkdir Usage: Folder already exists')
            
    else:
        current_dir[f'{new_folder}'] = []
        current_dir[f'{home_dir}'].append(new_folder_title)
    
def cd():
    global home_dir
    if argument == 'cd':
        home_dir = ' '
        home_dir = (rf'C:\users\{username}')
    elif argument.split(' ')[1].lower() in current_dir[home_dir]:
        change_dir_to = argument.split(' ')[1].lower()
        home_dir += f'\{change_dir_to}'
    else:
        change_dir_to = argument.split(' ')[1].lower()
        print(rf'cd: Cannot find path C:users\{username}\{change_dir_to} because it does not exist')

def touch():
    global home_dir
    example = ''
    new_file = argument.split(' ')[1].lower() + '.txt'
    if argument == 'touch':
        print('touch Usage: touch requires a file name after the command is called')
    elif len(argument.split(' ')) > 2:
        print(f'touch Usage: Input "{argument}" invalid. File name must be one position. Use "_" to concatenate')
        example_list = argument.split(' ')
        for i in range(1, len(example_list)):
            example += example_list[i]
            if i + 1 < len(example_list):
                example += '_'
        print(f'>>>>>>>>>>> example file name: {example}')
    elif new_file in current_dir[home_dir]:
        print(f'{new_file} Overwritten')
    else:
        current_dir[home_dir].append(new_file)

#BELOW CODE WILL KEEP PROGRAM IN LOOP TO MANIPULATE DIRECTORIES UNTIL EXIT 
while program_run:
    program_count += 1
    argument = input(f'\n{home_dir} > ').lower()
    if 'ls' in argument:
        ls()
    elif 'mkdir' in argument:
        mkdir()
    elif 'cd' in argument:
        cd()
    elif 'touch' in argument:
        touch()
    elif argument == 'exit':
        program_run = False
    else:
        print(f'Command not found: {argument}')

# Python-Assessment
To run the program all you have to do is input a name to create a home folder (i.e. my_home will create a folder in location C:\users\my_home). You will remain in a loop if you use whitespace in your username (the program will remind you). To update the 'file system' use the following commands:

**ls
cd
mkdir
touch
exit**

The program will give you a simulated error to help you understand how to properly execute a command but here are some tips to run it:

**** ls - ls is a straightforward command and will print what contents are in the folder you are 'located' in.

**** cd - cd will change the 'folder' you are in. To execute properly you will need to provide the name of the folder you would like to change to (i.e. 'cd documents' to change to the documents folder). If the folder does not exist the program will tell you at which point you will need to input mkdir to create one.
IF 'cd' IS ENTERED WITHOUT A FOLDER NAME THE PROGRAM IS DESIGNED TO TAKE YOU BACK TO YOUR HOME FOLDER

**** mkdir - mkdir will create a folder for you. As with cd you will need to also need to provide the name of the folder after mkdir (i.e. 'mkdir files' to create a folder named files). If the folder exists the program will notify you and you will need to provide a different name. Any folders that are more than one position in name must be without spaces to properly execute otherwise the program will inform you at which point you will need to input the name in a manner similiar. (i.e 'mkdir new folder' will result in programmed error whereas 'mkdir new_folder' will not.

**** touch - touch will create a new .txt file in whichever folder you currently are in. If the file already exists, unlike mkdir, the file will simply be overwritten without error

**** exit - exit will quit the program and all memory of the file system will be lost

There are created folders and files as a reference in each folder but you can manipulate the file system however you choose within the aforementioned parameters

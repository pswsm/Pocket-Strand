import os
from pathlib import Path

# Menu details--------------------------------------------------------

padding = 3


# Display the option menu------------------------------------------------
def count_canvas_size(options) -> int:
    '''
    Input: 	Takes the option list, checks the length of the longest option. 
    Output:	An integer, which represents the whole length of the menu canvas.
    '''
    longest_len = 0
    
    for key in options.keys():
        if len(str(key) + ': ' + options[key]) > longest_len:
           longest_len = len(str(key) + ': ' + options[key])
			
    return (2 * padding) + longest_len    


def print_filled_row(options, canvas_len) -> None:
    '''Takes the menu canvas length and the option list 
    		-> Counts the paddings.
    		-> Loops through the options list.
    		-> Prints out each padded option row.'''
    
    for key in options.keys():
        left_padding  = padding * " "
        right_padding = (canvas_len - len(str(key) + ': ' + options[key]) - padding) * " "

        row = "|" + left_padding + str(key) + ': ' + options[key] + right_padding + "|"
    
        print(row)


def menu(options) -> None:
   
    canvas_len = count_canvas_size(options)

    print("\n")
    print("+" + ("-" * canvas_len) + "+")
    print("|" + (" " * canvas_len) + "|")
    
    print_filled_row(options, canvas_len)
    
    print("|" + (" " * canvas_len) + "|")
    print("+" + ("-" * canvas_len) + "+")
	


#-Get and validate user input for integers and number ranges--------------------------------------------------------------------


def validate_format(usr_input) -> int:
    correct = usr_input.isnumeric()
    
    while not correct:
        print("\nERROR: invalid format. Must be a integer.")
        usr_input  = input("Choose an option: ")
        correct    = usr_input.isnumeric()
        
    return int(usr_input)
   
def validate_range(options, usr_input) -> int:
    "Validates the input to the corresponding number of menu options."
    correct = usr_input > 0 and usr_input <= len(options)
    
    while not correct:
        print("\nERROR: Input is out of range.")
        usr_input    = input("Choose an option: ")
        valid_format = validate_format(usr_input)
        correct      = valid_format > 0 and valid_format <= len(options)
    
    return usr_input


def get_menu_input(options) -> int:
    
    usr_input     = input("Choose an option: ")
    valid_format  = validate_format(usr_input)
    correct_range = validate_range(options,valid_format)

    return correct_range
            

#Validate boolean input-----------------------------------------------------------------------
def validate_bool_input(user_input) -> str:

    correct = user_input.lower() == 'y' or user_input.lower() == 'n'
    while not correct:
        print('ERROR: Invalid usr_input.\nType "y" as yes or "n" as no. ')
        usr_input = input("\nWould You like to save the result in a new file? - y/n\n")
        correct   = usr_input.lower() == 'y' or usr_input.lower() == 'n'

    return user_input

     

#-Function for saving the results------------------------------------------------------------
def save_result(result):
    usr_input   = input("\nWould You like to save the result in a new file? - y/n\n")
    valid_input = validate_bool_input(usr_input)

    
    if valid_input.lower() == 'y':
        if not os.path.exists('saved'):
            os.makedirs('saved')


        file_name   = input("File name: ")
        save_path   = os.path.join('./saved/',file_name)
        output_file = open(save_path + '.txt','w')
        output_file.write(result)
        output_file.close()
        
    elif valid_input.lower() == 'n':
        pass
    
    
#-Functions for importing data for analysis------------------------------------------
def import_data():
    
    import_options = {
        1:"Import from a file",
        2:"Input manually",
        3:"Main",
        4:"Exit"
    }

    while True:
            menu(import_options)
            usr_input = get_menu_input(import_options)
            data      = "nothing"
            
            if usr_input == 1:
                path = input("Give the path of your file: ")
                data = Path(path).read_text()
                    
            elif usr_input == 2:
                data = input("Enter / paste your sequence here:\n")
            
            elif usr_input == 3:
                import main
                main.display_main_menu()
                
            elif usr_input == 4:
                quit()
            
            return data

#-Functions to arrange the outputs--------------------------------
def arrange_nuc_output(data1, data2, length) -> None:
    "Arranges the input and output sequences into a more readable format."
    
    line1 = [data1[index:index + length] for index in range(0,len(data1),length)]
    line2 = [data2[index:index + length] for index in range(0,len(data2),length)]

    for index in range(len(line1)):
        print(line1[index])
        print("·" * len(line1[index]))
        print(line2[index] + "\n")



def arrange_amino_output(data,result) -> None:
    "Arranges the input and output sequences into a more readable format."
    
    data_rows = [data[i:i+60] for i in range(0,len(data),60)]
    "Breaks down the whole data string into a list[str] where each index represent a row of 60 chars."

    result_spaces = "   ".join([prot for prot in result])
    '''Insert spaces between amino acids in the result and breaks down to individual rows
       with the corresponding length to the 'data_rows'''

    for i in range(0,len(data_rows)):
        data_spaces = " ".join([data_rows[i][n:n+3] for n in range(0,len(data_rows[i]),3)])
        result_rows = [result_spaces[i:i + len(data_spaces)] for i in range(0,len(result_spaces),len(data_spaces))]
        print(data_spaces)        
        print(f"{result_rows[i]}\n")
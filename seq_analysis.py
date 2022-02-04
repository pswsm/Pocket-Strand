import utility
import seq_random

analysis_options = {
    1:"Count nucleotides, GC content, molecular weight",
    2:"Transcription",
    3:"Translation",
    4:"Complement",
    5:"Reverse complement",
    6:"Main",
    7:"Exit"
}

def display_seq_analysis_menu():
    "Displays the sequence analysis menu with the options."
    
    while True:
        utility.menu(analysis_options)
        value: str = utility.get_menu_input(analysis_options)
        
    
        if value == 1:
            "Count nucleotides, GC content, approximate mass"   
             
            try:
                data = utility.import_data()
                nuc_count  = count_nucleotides(data.upper())
                gc_count   = count_gc(data.upper())
                mol_weight = count_mol_weight(gc_count,nuc_count)
                
                result = f'''\n
Number of Nucleotides -> {nuc_count}
GC_Content -> {gc_count} %
Approximate mass:
    Single stranded linear -> {mol_weight} g/mol
    Double stranded linear -> {mol_weight*2} g/mol'''
                
                
                print(result)
                utility.save_result(result) 

            except FileNotFoundError:
                print("Wrong path or not a valid file.")
                
        elif value == 2:
            "Transcription"
            
            try:
                data   = utility.import_data()
                result = transcription(data.upper())

                usr_input   = input("Would You like to display both sequences? (y/n)\n")
                valid_input = utility.validate_bool_input(usr_input)

                if valid_input.lower()   == 'y':
                    utility.arrange_nuc_output(data,result,60)

                elif valid_input.lower() == 'n':
                    print(result)

                utility.save_result(result)
                
            except FileNotFoundError:
                print("Wrong path or not a valid file.")
            
        elif value == 3:
            "Translation"
            
            try:
                data   = utility.import_data()
                result = translation(data.upper(),0)

                usr_input   = input("Would You like to display both sequences? (y/n)\n")
                valid_input = utility.validate_bool_input(usr_input)

                if valid_input.lower()   == 'y':
                    utility.arrange_amino_output(data,result)

                elif valid_input.lower() == 'n':
                    print(result)

                utility.save_result(result)
            except FileNotFoundError:
                print("Wrong path or not a valid file.")
         
        elif value == 4:
            "Complement"

            try:
                data   = utility.import_data()
                result = complement(data)
                
                usr_input   = input("Would You like to display both sequences? (y/n)\n")
                valid_input = utility.validate_bool_input(usr_input)

                if valid_input.lower()   == 'y':
                    utility.arrange_nuc_output(data,result,60)

                elif valid_input.lower() == 'n':
                    print(result)

                utility.save_result(result)
                
            except FileNotFoundError:
                print("Wrong path or not a valid file.")

        elif value == 5:
            "Reverse complement"

            try:
                data   = utility.import_data()
                result = complement(data)
                
                usr_input   = input("Would You like to display both sequences? (y/n)\n")
                valid_input = utility.validate_bool_input(usr_input)

                if valid_input.lower()   == 'y':
                    utility.arrange_nuc_output(data,result[::-1],60)

                elif valid_input.lower() == 'n':
                    print(result[::-1])

                utility.save_result(result[::-1])
                
            except FileNotFoundError:
                print("Wrong path or not a valid file.")

        elif value == 6:
            "Main"

            import main
            main.display_main_menu()
        
        elif value == 7:
            "Exit"

            quit()

# Functions of this menu-----------------------------------------------
def count_nucleotides(dna_seq) -> dict:
    "Will count the number of nucleotides found in the input sequence."

    result = {"A": 0, "T" : 0, "G" : 0, "C" : 0 }

    for nuc in dna_seq:
        if nuc not in result:
            continue 
        result[nuc] += 1
        
    return result

def count_gc(dna_seq) -> int:
    '''Takes the nucleotides sequence as an input,
        then returns the gc content as a string in percentage.'''
    
    gc_content = round((dna_seq.count('C') + dna_seq.count('G')) / len(dna_seq) * 100)

    return gc_content


def count_mol_weight(gc_cont, nuc_count) -> float:
    ''' Takes the dictionary of "count_nucleotides" and the gc_content,
        then calculates the approximate mass of the given dna sequence.'''
    
    bp_avgW  = {'AT':326.7151, 'GC':327.2092 }
    
    gc_avg   = (gc_cont/100) * bp_avgW['GC']
    at_avg   = (1-(gc_cont/100)) * bp_avgW['AT']
    curr_avg = gc_avg + at_avg 
    
    length   = 0
    for num in nuc_count.values():
        length += num
    
    g_mol    = curr_avg * length
    
    return round(g_mol,2)
    

def transcription(sequence) -> str:
    "DNA -> RNA transcription"
    return sequence.replace("T","U")


def complement(sequence) -> str:
    '''Creates the complementary strand of the input sequence.
        Runs through the input data and switches the nucleotides for their complementary.'''
    
    complements = {"A":"T","T":"A","G":"C","C":"G"}
    result      = []
    
    for nuc in sequence:
        if nuc.upper() not in complements:
            result.append("?")
            continue
        
        result.append(complements[nuc.upper()])
    
    return "".join(result)
        
def translation(sequence, start_position) -> str:
    '''Runs through the input data in steps of 3, 
        and when finds the matching amino acid of the codon, appends it to the result list.'''
    result = []
    
    for position in range(start_position, len(sequence) - 1,3):
        if sequence[position:position + 3] not in seq_random.codons:
            result.append("?")
            continue
        
        result.append(seq_random.codons[sequence[position:position + 3]])      
        
    return "".join(result)







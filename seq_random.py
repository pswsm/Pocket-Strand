import random
import utility


sequence_options = {
    1:"DNA sequence",
    2:"Amino acid sequence",
    3:"Main",
    4:"Exit"
}

# Structures ---------------------------------------------------------
dna    = ("A", "C","G", "T")

codons = {
    "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "TGT":"C", "TGC":"C",
    "GAT":"D", "GAC":"D",
    "GAA":"E", "GAG":"E",
    "TTT":"F", "TTC":"F", 
    "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",
    "CAT":"H", "CAC":"H",
    "ATT":"I", "ATC":"I", "ATA":"I",
    "AAA":"K", "AAG":"K",
    "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L", "TTA":"L", "TTG":"L",
    "ATG":"M",
    "AAT":"N", "AAC":"N",
    "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAA":"Q", "CAG":"Q",
    "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R", 
    "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S", 
    "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V", 
    "TGG":"W",
    "TAT":"Y", "TAC":"Y",
    "TGA":"_", "TAA":"_", "TAG":"_"
}

amino_acids = sorted(list(set([codons[i] for i in codons])))
"Re-uses the 'codons' dictionary and gets the amino acid list."


def display_randomization_menu():
    "Displays the options for random nucleotide or amino acid sequences. "    
    
    while True:
        utility.menu(sequence_options)
        value = utility.get_menu_input(sequence_options)
        
        if value == 1:
            dna_seq = randomize_sequence(dna)
            print(f"\n{dna_seq}")
            utility.save_result(dna_seq)
            
        elif value == 2:
            amino_acid_seq: str = randomize_sequence(amino_acids)
            print(f"\n{amino_acid_seq}")
            utility.save_result(amino_acid_seq)
        
        elif value == 3:
            import main
            main.display_main_menu()
            
        elif value == 4:
            quit()


# Randomization function-------------------------------------------------------------
def randomize_sequence(sequence_type):
    
    
    length       = input("Choose a length: ")
    valid_length = utility.validate_format(length)

    correct = valid_length > 0
    while not correct:
        print("\nERROR: Incorrect range.")
        
        length       = input("Choose a length: ")
        valid_length = utility.validate_format(length)
        correct      = valid_length > 0
            
    sequence = [random.choice(sequence_type) for i in range(valid_length)]

    return "".join(sequence)


    





















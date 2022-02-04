import utility
import seq_random
import seq_analysis

main = {
    1:"Randomize sequence",
    2:"Sequence Analysis",
    3:"Exit"
}


def display_main_menu() -> None:
    while True:
        utility.menu(main)
        value = utility.get_menu_input(main)
    
        if value   == 1:
            seq_random.display_randomization_menu()
            
        elif value == 2:
            seq_analysis.display_seq_analysis_menu()
            
        elif value == 3:
            quit()
            
display_main_menu()
What I think I need to do are the ff:
. Compartmentalize each "mode", ie, create a dedicated function/method per mode to deal with each
. Use a list of dictionaries, with each dictionary representing each mode
. Each mode has the properties "name", "keyword", "description", "config_instructions", a method "check_config", and then another method "go_focus"
. The function choose_activity() will then give the user the option by looping through the mode list and getting the names
. Once the choice is selected, the main function will then run the appropriate mode by finding the corresponding dictionary in the mode list, and running the "go_focus" method of the matched dictionary
. BUT, before doing the "go_focus" method, the script should first run the "check_config" method, which serves as a checker to confirm if all external dependencies are met, which simply mean checking if folder paths, path variables, and installed software are all correct
. If correct, run the "go_focus" method, if not, display the corresponding error for the mismatch AND THEN display the "config_instructions"


Bare-minimum flow working

from InquirerPy import inquirer


class Questions:

    def ask_all(self):
        
        answers = {}

    answers["title"] = inquirer.text(
            message="Project title:"
        ).execute()   
    
    answers["description"] = inquirer.text(
            message="Short description of the project:"
        ).execute()
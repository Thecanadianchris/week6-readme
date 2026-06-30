from InquirerPy import inquirer


class Questions:

    LICENSE_OPTIONS = ["Python", "Javasript", "BootStrap", "Other", "None"]



    def ask_all(self):
        
        answers = {}

        answers["title"] = inquirer.text(
            message="Project title:"
        ).execute()   

    
        answers["description"] = inquirer.text(
            message="Short description of the project:"
        ).execute()


        answers["installation"] = inquirer.text(
            message="Installation instructions:"
        ).execute()


        answers["usage"] = inquirer.text(
            message="Usage information:"
        ).execute()


        answers["license"] = inquirer.select(
            message="Choose a license:",
            choices=self.LICENSE_OPTIONS,
        ).execute()


        answers["author"] = inquirer.text(
            message="Author name:"
        ).execute()


        answers["contact"] = inquirer.text(
            message="Contact information (email/GitHub):"
        ).execute()


        return answers
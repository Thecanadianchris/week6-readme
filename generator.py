class ReadmeGenerator:

    def __init__(self, answers):
        self.answers = answers

    def build_markdown(self):
        a = self.answers   

        markdown = f"""# {a['projectTitle']}

# Description

{a['description']}



# Installation

{a['installation']}


# Usage

{a['usage']}


# License

This project is licensed under the {a['license']} license.


# Author

{a['author']}


# Contact

{a['contact']}
"""
        

        return markdown
    
    def write_file(self, filename="README.md"):
        content = self.build_markdown()
        with open(filename, "w") as f:
            f.write(content)
        print(f"\n {filename} has been generated!")

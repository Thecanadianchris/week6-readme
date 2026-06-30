class ReadmeGenerator:

    def __init__(self, answers):
        self.answers = answers

    def build_markdown(self):
        a = self.answers   

        markdown = f"""# {a['projectTitle']}

# Description

{a['description']}
S

{a['contact']}
"""
        

        return markdown
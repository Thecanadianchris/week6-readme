from questions import Questions
from generator import ReadmeGenerator

def main():
    print("Python README Generator\n")

    questions = Questions()
    answers = questions.ask_all()

    generator = ReadmeGenerator(answers)
    generator.write_file("README_Python.md")


if __name__ == "__main__":
    
    main()
from word_generator import WordTemplateGenerator
from word_template_data import WordTemplateData

if __name__ == '__main__':
    generator = WordTemplateGenerator(WordTemplateData)
    generator.generate()
    generator.save('Generate_Access_Token_API.docx')
    print("Word document generated: Generate_Access_Token_API.docx")
from word_generator import WordTemplateGenerator
import json
import os
from convert_postman_to_template import convert_postman_item

def main():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    postman_path = os.path.join(dir_path, 'ABC.postman_collection.json')
    with open(postman_path, encoding='utf-8') as f:
        postman_json = json.load(f)
    template_data = [convert_postman_item(item) for item in postman_json['item']]
    # Write to WordTemplateData.py as a class
    word_template_data_path = os.path.join(dir_path, 'WordTemplateData.py')
    with open(word_template_data_path, 'w', encoding='utf-8') as f:
        f.write('class WordTemplateData:\n')
        f.write('    items = ')
        json.dump(template_data, f, indent=4, ensure_ascii=False)
        f.write('\n')
    print(f"WordTemplateData.py generated at {word_template_data_path}")


if __name__ == '__main__':
    main()
    # Import the generated class dynamically
    import importlib.util
    dir_path = os.path.dirname(os.path.abspath(__file__))
    word_template_data_path = os.path.join(dir_path, 'WordTemplateData.py')
    spec = importlib.util.spec_from_file_location('WordTemplateData', word_template_data_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    generator = WordTemplateGenerator(module.WordTemplateData)
    generator.generate()
    generator.save('Generate_API_DOC.docx')
    print("Word document generated: Generate_API_DOC.docx")
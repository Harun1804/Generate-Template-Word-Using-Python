from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

class WordStyles:
    @staticmethod
    def set_table_header_style(row):
        for cell in row.cells:
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            shd = OxmlElement('w:shd')
            shd.set(qn('w:fill'), 'cfe1f3')
            tcPr.append(shd)
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.bold = True
                    run.font.name = 'Tahoma'
                    run.font.size = Pt(11)
                    r = run._element
                    r.rPr.rFonts.set(qn('w:eastAsia'), 'Tahoma')

    @staticmethod
    def set_heading_style(paragraph):
        for run in paragraph.runs:
            run.bold = True
            run.font.name = 'Tahoma'
            run.font.size = Pt(14)
            run.font.color.rgb = RGBColor(0, 0, 0)
            r = run._element
            r.rPr.rFonts.set(qn('w:eastAsia'), 'Tahoma')

    @staticmethod
    def set_content_style(paragraph):
        for run in paragraph.runs:
            run.font.name = 'Tahoma'
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(0, 0, 0)
            r = run._element
            r.rPr.rFonts.set(qn('w:eastAsia'), 'Tahoma')

    @staticmethod
    def set_table_content_style(table, header_rows=None, special_rows=None):
        if header_rows is None:
            header_rows = [0]
        if special_rows is None:
            special_rows = []
        for i, row in enumerate(table.rows):
            if i in header_rows or i in special_rows:
                continue
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    WordStyles.set_content_style(paragraph)
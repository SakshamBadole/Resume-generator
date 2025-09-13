from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import io

def generate_resume_pdf(data_dict):
    """Generates a PDF resume from a dictionary of data and returns it as a bytes object."""
    # Using io.BytesIO to create the PDF in memory instead of saving to a file
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []

    # Get the sample styles
    styles = getSampleStyleSheet()
    
    # Extract data from the dictionary
    name = data_dict.get('name', '')
    phone = data_dict.get('phone', '')
    email = data_dict.get('email', '')
    linkedin = data_dict.get('linkedin', '')
    objective = data_dict.get('objective', '')
    
    # Handle multi-line inputs, splitting by newline characters
    education_lines = data_dict.get('education', '').split('\n')
    skills_programming = data_dict.get('skills_programming', '')
    skills_web = data_dict.get('skills_web', '')
    skills_tools = data_dict.get('skills_tools', '')
    experience_lines = data_dict.get('experience', '').split('\n')
    project_lines = data_dict.get('projects', '').split('\n')
    certifications_lines = data_dict.get('certifications', '').split('\n')
    languages = data_dict.get('languages', '')
    hobbies = data_dict.get('hobbies', '')

    data = [
        ['Name', name],
        ['Contact Info', [
            Paragraph(f'📞 {phone}', styles['Normal']),
            Paragraph(f'📧 {email}', styles['Normal']),
            Paragraph(f'🔗 <font color="blue"><u>{linkedin}</u></font>', styles['Normal'])
        ]],
        ['Career Objective', objective],
        ['Education', [Paragraph(line, styles['Normal']) for line in education_lines if line]],
        ['Skills', [
            Paragraph(f'<b>- Programming:</b> {skills_programming}', styles['Normal']),
            Paragraph(f'<b>- Web:</b> {skills_web}', styles['Normal']),
            Paragraph(f'<b>- Tools:</b> {skills_tools}', styles['Normal'])
        ]],
        ['Experience', [Paragraph(line, styles['Normal']) for line in experience_lines if line]],
        ['Projects', [Paragraph(f'- {line}', styles['Normal']) for line in project_lines if line]],
        ['Certifications', [Paragraph(f'- {line}', styles['Normal']) for line in certifications_lines if line]],
        ['Languages', languages],
        ['Hobbies', hobbies]
    ]

    light_gray = colors.Color(0.95, 0.95, 0.95)
    resume_table = Table(data, [1.5 * inch, 5 * inch])
    style = TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BACKGROUND', (0, 0), (-1, -1), light_gray)
    ])
    resume_table.setStyle(style)
    story.append(resume_table)
    
    doc.build(story)
    
    # Move buffer position to the beginning so it can be read
    buffer.seek(0)
    return buffer
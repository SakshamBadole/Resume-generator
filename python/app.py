from flask import Flask, render_template, request, send_file
from resume_generator import generate_resume_pdf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Get all form data from the user
    user_data = {
        'name': request.form.get('name'),
        'phone': request.form.get('phone'),
        'email': request.form.get('email'),
        'linkedin': request.form.get('linkedin'),
        'objective': request.form.get('objective'),
        'education': request.form.get('education'),
        'skills_programming': request.form.get('skills_programming'),
        'skills_web': request.form.get('skills_web'),
        'skills_tools': request.form.get('skills_tools'),
        'experience': request.form.get('experience'),
        'projects': request.form.get('projects'),
        'certifications': request.form.get('certifications'),
        'languages': request.form.get('languages'),
        'hobbies': request.form.get('hobbies')
    }
    
    # Call the modified resume generator function
    pdf_buffer = generate_resume_pdf(user_data)
    
    # Send the generated PDF file to the user
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name=f"{user_data['name'].replace(' ', '_')}_Resume.pdf",
        mimetype='application/pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)
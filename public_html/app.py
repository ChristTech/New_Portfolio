from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download-pdf')
def download_pdf():
    file_path = 'results.pdf'
    return send_file(file_path, as_attachment=True, download_name='results.pdf')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Context processor to inject the current endpoint name into templates
@app.context_processor
def inject_current_endpoint():
    return dict(current_endpoint=request.endpoint)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the testimonials page
@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

# Route for the services page
@app.route('/services')
def services():
    return render_template('services.html')

# Route for the portfolio page
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

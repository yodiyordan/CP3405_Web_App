from flask import Flask, render_template, request, url_for
import os

IMAGES = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGES


# For render_template pass in name of template and any variables needed
@app.route('/')
@app.route('/index')
# To display images on the web page
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'burndown_and_velocity_chart.jpg')
    return render_template("index.html", user_image=full_filename)


# To specify how to run the app
if __name__ == "__main__":
    app.run()
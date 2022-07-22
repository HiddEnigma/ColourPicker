from flask import Flask, render_template, url_for, request, redirect
from werkzeug.utils import secure_filename
from colorthief import ColorThief
from datetime import datetime

import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/files"


@app.route('/', )
def home():
    return render_template("index.html")


@app.route("/colours", methods=["POST", "GET"])
def result():
    file = request.files['file']

    name = secure_filename(file.filename)

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], name))

    full_image_path = f"static/files/{file.filename}"
    colour_thief = ColorThief(full_image_path)

    top_colours = colour_thief.get_palette(color_count=11)

    return render_template("colours.html", image=full_image_path, top_colours=top_colours)


if __name__ == "__main__":
    app.run(debug=True)

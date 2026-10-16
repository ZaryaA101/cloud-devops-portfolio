from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder="static", static_url_path="")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/Zarya_Amin_Resume.pdf")
def resume():
    return send_from_directory(
        app.static_folder,
        "Zarya_Amin_Resume.pdf",
        mimetype="application/pdf",
        as_attachment=True,
        download_name="Zarya_Amin_Resume.pdf",
    )


@app.route("/images/Zarya_Amin_Graduation.webp")
def graduation_photo():
    return send_from_directory(
        app.static_folder,
        "images/Zarya_Amin_Graduation.webp",
        mimetype="image/webp",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dedupe")
def dedupe():
    return render_template("dedupe.html")


@app.route("/list-compare")
def list_compare():
    return render_template("list_compare.html")


@app.route("/epoch")
def epoch():
    return render_template("epoch.html")


@app.route("/json-formatter")
def json_formatter():
    return render_template("json_formatter.html")


@app.route("/base64")
def base64_tool():
    return render_template("base64.html")


@app.route("/url-encode")
def url_encode():
    return render_template("url_encode.html")


@app.route("/jwt-decoder")
def jwt_decoder():
    return render_template("jwt_decoder.html")


@app.route("/case-converter")
def case_converter():
    return render_template("case_converter.html")


@app.route("/regex-tester")
def regex_tester():
    return render_template("regex_tester.html")


@app.route("/uuid-generator")
def uuid_generator():
    return render_template("uuid_generator.html")


@app.route("/base-converter")
def base_converter():
    return render_template("base_converter.html")


@app.route("/cron-explainer")
def cron_explainer():
    return render_template("cron_explainer.html")


@app.route("/csv-json")
def csv_json():
    return render_template("csv_json.html")


@app.route("/image-ocr")
def image_ocr():
    return render_template("image_ocr.html")


if __name__ == "__main__":
    app.run(debug=True)

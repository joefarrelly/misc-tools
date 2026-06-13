from flask import Flask, render_template, request, jsonify
import pytesseract
from PIL import Image

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


@app.route("/image-ocr/extract", methods=["POST"])
def image_ocr_extract():
    file = request.files.get("image")
    if not file:
        return jsonify({"error": "No image provided"}), 400

    threshold = int(request.form.get("threshold", 85))
    filter_noise = request.form.get("filter", "true") == "true"

    img = Image.open(file.stream)
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

    lines = {}
    for i, text in enumerate(data["text"]):
        if not text.strip():
            continue
        conf = int(data["conf"][i])
        key = (data["block_num"][i], data["par_num"][i], data["line_num"][i])
        if key not in lines:
            lines[key] = {"words": [], "conf": [], "top": data["top"][i]}
        lines[key]["words"].append(text)
        lines[key]["conf"].append(conf)

    sorted_lines = sorted(
        [
            {
                "text": " ".join(v["words"]),
                "conf": sum(v["conf"]) // len(v["conf"]),
                "top": v["top"],
                "key": k,
            }
            for k, v in lines.items()
        ],
        key=lambda x: x["key"],
    )

    if filter_noise:
        sorted_lines = [ln for ln in sorted_lines if ln["conf"] >= threshold]

    if not sorted_lines:
        return jsonify({"chunks": []})

    avg_h = 20
    chunks = []
    current = [sorted_lines[0]["text"]]

    for i in range(1, len(sorted_lines)):
        gap = sorted_lines[i]["top"] - sorted_lines[i - 1]["top"]
        if gap > avg_h * 2.5:
            chunks.append("\n".join(current))
            current = []
        current.append(sorted_lines[i]["text"])
    chunks.append("\n".join(current))

    return jsonify({"chunks": [c for c in chunks if c.strip()]})


if __name__ == "__main__":
    app.run(debug=True)

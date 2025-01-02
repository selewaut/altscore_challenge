from flask import Flask, jsonify, render_template_string, make_response
import random

app = Flask(__name__)

systems = ["engine", "navigation", "communication", "life_support"]
system_codes = {
    "engine": "ENG123",
    "navigation": "NAV456",
    "communication": "COM789",
    "life_support": "LIF101",
}


@app.route("/status")
def status():
    damaged_system = random.choice(systems)
    return jsonify({"damaged_system": damaged_system})


@app.route("/repair-bay")
def repair_bay():
    damaged_system = status().get_json().get("damaged_system")
    unique_code = system_codes[damaged_system]
    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head><title>Repair Bay</title></head>
        <body>
            <div class="anchor-point">{unique_code}</div>
        </body>
    </html>
    """
    return render_template_string(html_content)


@app.route("/repair")
def repair_bay_simple():
    print("repairing")
    damaged_system = status().get_json().get("damaged_system")
    unique_code = system_codes[damaged_system]
    return make_response(unique_code, 200)


@app.route("/teapot", methods=["POST"])
def teapot():
    return make_response("I'm a teapot", 418)


if __name__ == "__main__":
    app.run(debug=True)

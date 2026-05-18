from flask import Flask, request, render_template_string
import json
import os
from motor import load_data, run_engine

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

HTML = """
<!doctype html>
<html lang="sv">
<head>
<meta charset="utf-8">
<title>Poängmotor</title>
<style>
  body { font-family: Arial, sans-serif; max-width: 700px; margin: 40px auto; }
  .error { background: #ffe6e6; border: 1px solid #ff4d4d; padding: 12px; border-radius: 6px; color: #b30000; }
  .result { background: #e6ffe6; border: 1px solid #33cc33; padding: 12px; border-radius: 6px; }
  pre { background: #f5f5f5; padding: 10px; overflow-x: auto; }
  input, select, button { margin: 6px 0; padding: 6px; }
</style>
</head>
<body>
<h2>Poängmotor</h2>

<form method=post enctype=multipart/form-data>
  <label>Ladda upp CSV eller JSON:</label><br>
  <input type=file name=file accept=".csv,.json" required><br>
  <button type=submit>Kör motor</button>
</form>

{% if error %}
  <h3>Fel:</h3>
  <div class="error">{{ error }}</div>
{% endif %}

{% if result %}
  <h3>Resultat:</h3>
  <div class="result">
    <pre>{{ result | tojson(indent=2, ensure_ascii=False) }}</pre>
  </div>
{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    result = None
    
    if request.method == "POST":
        f = request.files["file"]
        if f.filename == "":
            error = "Ingen fil vald"
        else:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
            f.save(filepath)
            
            try:
                data = load_data(filepath)
                result = run_engine(data["rules"], data)
            except Exception as e:
                error = str(e)  # Visar felmeddelandet från motor.py direkt
    
    return render_template_string(HTML, error=error, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

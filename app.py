from flask import Flask, request, jsonify, render_template
import os
import re

app = Flask(__name__)

def process_wildcards(folder_path):
    wildcards = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as file:
                wildcards[file_name] = file.read()

    nodes = [{"id": file.replace(".txt", "")} for file in wildcards]
    links = []
    for file, content in wildcards.items():
        source = file.replace(".txt", "")
        references = re.findall(r'__([\w\d_]+)__', content)
        for ref in references:
            links.append({"source": source, "target": ref})

    return {"nodes": nodes, "links": links}

@app.route("/")
def index():
    # Flask のテンプレートエンジンを使って HTML を表示
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    folder_path = data['folderPath']
    result = process_wildcards(folder_path)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

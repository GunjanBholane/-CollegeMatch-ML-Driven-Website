from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the dataset
file_path = r"D:\F . P\Clg\data.csv"
df = pd.read_csv(file_path)

# Function to find eligible colleges
def find_colleges(marks, caste, stream):
    if marks == 90:
        eligible_colleges = df[
            (df["Min Cutoff " + caste] <= marks) & 
            (df["Course"].str.lower() == stream.lower())
        ]
    else:
        eligible_colleges = df[
            (df["Min Cutoff " + caste] <= marks) & 
            (df["Max Cutoff " + caste] >= marks) & 
            (df["Course"].str.lower() == stream.lower())
        ]
    return eligible_colleges

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_colleges', methods=['POST'])
def get_colleges():
    data = request.get_json()
    marks = int(data['marks'])
    caste = data['caste']
    stream = data['stream']
    
    # Find eligible colleges
    results = find_colleges(marks, caste, stream)
    
    if not results.empty:
        colleges = results[["College Name", "Course", "Location"]].to_dict(orient="records")
    else:
        colleges = []

    return jsonify({"colleges": colleges})

if __name__ == "__main__":
    app.run(debug=True)

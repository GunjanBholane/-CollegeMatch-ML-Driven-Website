from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load dataset
data = pd.read_csv(r'D:\F . P\Clg\dec\raw1\data - Copy.csv')

# Strip spaces and ensure lowercase matching
data.columns = data.columns.str.strip()
data['Branch'] = data['Branch'].str.strip().str.lower()
data['Category'] = data['Category'].str.strip().str.lower()

def filter_colleges(branch, category, marks):
    # Normalize user input
    branch = branch.strip().lower()
    category = category.strip().lower()

    # Filter dataset where Branch, Category match and Marks <= input marks
    filtered = data[(data['Branch'] == branch) & 
                    (data['Category'] == category) & 
                    (data['Marks'] <= marks)]
    
    # Return unique college names
    return list(filtered['Name of College'].unique())

@app.route('/', methods=['GET', 'POST'])
def index():
    colleges = None  # Default to None to avoid errors
    if request.method == 'POST':
        branch = request.form['branch']
        category = request.form['category']
        try:
            marks = float(request.form['marks'])
            colleges = filter_colleges(branch, category, marks)
        except ValueError:
            colleges = ["Invalid marks input. Please enter a valid number."]
    
    return render_template('iwork.html', colleges=colleges)

if __name__ == '__main__':
    app.run(debug=True)

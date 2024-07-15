from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle CSV file upload and accommodation grouping
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Get uploaded files
        file1 = request.files['file1']
        file2 = request.files['file2']

        # Check if files are uploaded
        if file1 and file2:
            # Read CSV files into pandas DataFrames
            df1 = pd.read_csv(file1)
            df2 = pd.read_csv(file2)

            # Merge dataframes on 'ID' column
            merged_df = pd.merge(df1, df2, on='ID')

            # Group students by gender
            accommodation = {}
            for _, row in merged_df.iterrows():
                student_id = row['ID']
                gender = row['Gender']  # Assuming Gender_y from second file for accommodation

                if gender not in accommodation:
                    accommodation[gender] = []

                accommodation[gender].append({
                    'ID': student_id,
                    'Name': row['Name'],  # Assuming Name_x from first file
                    'Age': row['Age']     # Assuming Age_x from first file
                })

            # Render accommodation results
            return render_template('result.html', accommodation=accommodation)
        else:
            return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

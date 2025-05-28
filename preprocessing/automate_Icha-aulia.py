
import pandas as pd
import sys

def preprocess_student_data(filepath):
    df = pd.read_csv(filepath)

    df['gender'] = df['gender'].map({'female': 0, 'male': 1})
    df['race/ethnicity'] = df['race/ethnicity'].astype('category').cat.codes
    df['parental level of education'] = df['parental level of education'].astype('category').cat.codes
    df['lunch'] = df['lunch'].map({'standard': 1, 'free/reduced': 0})
    df['test preparation course'] = df['test preparation course'].map({'completed': 1, 'none': 0})
    df['passed'] = ((df['math score'] >= 50) &
                (df['reading score'] >= 50) &
                (df['writing score'] >= 50)).astype(int)
    return df
if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    df = preprocess_student_data(input_path)
    df.to_csv(output_path, index=False)
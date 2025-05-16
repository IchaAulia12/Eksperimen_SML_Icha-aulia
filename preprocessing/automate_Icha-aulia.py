# automate_Nama-siswa.py
import pandas as pd

def preprocess_student_data(filepath):
    df = pd.read_csv(filepath)

    df['gender'] = df['gender'].map({'female': 0, 'male': 1})
    df['race/ethnicity'] = df['race/ethnicity'].astype('category').cat.codes
    df['parental level of education'] = df['parental level of education'].astype('category').cat.codes
    df['lunch'] = df['lunch'].map({'standard': 1, 'free/reduced': 0})
    df['test preparation course'] = df['test preparation course'].map({'completed': 1, 'none': 0})

    return df

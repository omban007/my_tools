import pandas as pd
import torch
import torchtext
import re
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="darkgrid")

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


def clean_text(x_value):
    cleaned_text = re.sub(r"[^a-zA-Z0-9 ]", "", x_value)
    return cleaned_text


def visualize_text(spam_ham):
    ax = sns.countplot(x="label", data=spam_ham)
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv("../data/spam.csv", encoding='windows-1252')

    df.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    df.rename(columns={'v1': 'label', 'v2': 'value'}, inplace=True)
    df.drop_duplicates(inplace=True)
    df["cleaned_value"] = df['value'].apply(lambda x: clean_text(x))
    df['cleaned_value'] = df['cleaned_value'].str.lower()
    print(df)
    print(df.describe())
    visualize_text(df)

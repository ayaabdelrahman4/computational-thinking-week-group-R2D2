import pandas as pd

def solution_station5(n):
    name = input("Enter a name: ")

    df = pd.read_csv("/Users/aya/computational-thinking-week-group-R2D2/challenge_day2/names_list.csv")

    for index, row in df.iterrows():
        if row["name"] == name:
            print(f"{row["number"]}")

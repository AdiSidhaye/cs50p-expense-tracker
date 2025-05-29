import pandas as pd

def main():
    temp=input("enter new cat")
    df = pd.read_csv('data/categories.csv')
    #for getting the categories as a list instead of a numpy array we use to list
    for catg in df['Category'].tolist():
        print(catg)
        print(type(catg))


if __name__=="__main__":
    main()
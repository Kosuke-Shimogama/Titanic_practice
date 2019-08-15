import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
# import sklearn
import os


def main():
    print(os.path.exists('./src/train.csv'))
    df = pd.read_csv('./src/train.csv')
    print(df.head(3))


if __name__ == '__main__':
    main()

import pandas as pd


runtime_fp = '/Users/Odhran/PycharmProjects/CrashCourse/imdb/runningtimes.csv'
runtime = pd.read_csv(runtime_fp, delimiter=';')
short_runtime = 0

for i in range(runtime.shape[0]):
    if runtime.iloc[i][3] < 10:
        short_runtime += 1

print('Num films <10 mins long: ' + str(short_runtime))
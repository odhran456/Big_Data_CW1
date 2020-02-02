import numpy as np
import pandas as pd


actors_fp = '/Users/Odhran/PycharmProjects/CrashCourse/imdb/actors.csv'
actors = pd.read_csv(actors_fp, delimiter=';')
# print(actors.shape, actors.head, actors.dtypes)

# actors = np.genfromtxt(actors_fp, delimiter=';', encoding='utf-8', skip_header=1, dtype=(int,'U25','U25'))
# gender_problem = np.empty([1,3], dtype=(int,'U25','U25'))

male_actors=0
female_actors=0
gender_problem =[]

for i in range(actors.shape[0]):
    if actors.iloc[i][2] != 'M':
        if actors.iloc[i][2] != 'F':
            gender_problem.append(actors.iloc[i])
    if actors.iloc[i][2] == 'M':
        male_actors += 1
    if actors.iloc[i][2] == 'F':
        female_actors += 1


print('Actors with error in gender field: ' + str(gender_problem) + '   Actors (Male): ' + str(male_actors)
      + '   Actresses: ' + str(female_actors))

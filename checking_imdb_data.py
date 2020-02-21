import pandas as pd


actors_fp = '/Users/Odhran/PycharmProjects/CrashCourse/imdb/actors.csv'
actors = pd.read_csv(actors_fp, delimiter=';')


male_actors=0
female_actors=0

for i in range(actors.shape[0]):
    if actors.iloc[i][2] == 'M':
        male_actors += 1
    if actors.iloc[i][2] == 'F':
        female_actors += 1


print('Actors (Male): ' + str(male_actors)
      + '   Actresses: ' + str(female_actors))


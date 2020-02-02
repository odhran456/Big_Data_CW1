import pandas as pd


movie_fp = '/Users/Odhran/PycharmProjects/CrashCourse/imdb/movies.csv'
movie = pd.read_csv(movie_fp, delimiter=';')

_60s = [i for i in range(1960,1970)]
_70s = [i for i in range(1970,1980)]
_80s = [i for i in range(1980,1990)]
_90s = [i for i in range(1990,2000)]
_00s = [i for i in range(2000,2010)]
_10s = [i for i in range(2010,2020)]

counters = lambda n: [0 for x in range(n)]
_60s_counter, _70s_counter, _80s_counter, _90s_counter, _00s_counter, _10s_counter = counters(6)

for i in range(movie.shape[0]):
    if movie.iloc[i][2] in _60s:
        _60s_counter += 1
    elif movie.iloc[i][2] in _70s:
        _70s_counter += 1
    elif movie.iloc[i][2] in _80s:
        _80s_counter += 1
    elif movie.iloc[i][2] in _90s:
        _90s_counter += 1
    elif movie.iloc[i][2] in _00s:
        _00s_counter += 1
    elif movie.iloc[i][2] in _10s:
        _10s_counter += 1

print('60s: ' + str(_60s_counter) + '\n' + '70s: ' + str(_70s_counter) + '\n' + '80s: ' + str(_80s_counter) + '\n' +
      '90s: ' + str(_90s_counter) + '\n' + '00s: ' + str(_00s_counter) + '\n' + '10s: ' + str(_10s_counter) + '\n')
import numpy as np
import math
import pandas as pd


def getDistance(searchedMovie):
    movies = pd.read_csv('movies.csv')
    rows, columns = movies.shape
    moviesName = list(movies['title'])
    if searchedMovie in moviesName:
        movieId = movies.loc[moviesName.index(searchedMovie), 'movieId']
    else:
        return False

    genres = list(movies['genres'])
    moviesCount = len(genres)
    movieGenres = {}
    genreSet = set()
    for i in range(rows):
        data = movies.loc[i, 'genres']
        genres = data.split('|')
        movieGenres[i+1] = genres
        for genre in genres:
            genreSet.add(genre)
    genresList = list(genreSet)
    genresList.append('Movie ID')
    dfMovies = pd.DataFrame(index=range(rows), columns=genresList)
    dfMovies = dfMovies.fillna(0)
    for i in range(rows):
        dfMovies.loc[i, 'Movie ID'] = i+1
        for gener in genresList:
            if gener in movieGenres[i+1]:
                dfMovies.loc[i, gener] = 1

    searched = list(
        dfMovies.iloc[dfMovies.loc[dfMovies['Movie ID'] == movieId].index[0]])

    searched.pop()
    #  pop id..
    # knn...
    distanceList = list()
    for i in range(rows):
        movie = list(
            dfMovies.iloc[dfMovies.loc[dfMovies['Movie ID'] == dfMovies.loc[i, "Movie ID"]].index[0]])
        movie.pop()
        d = eucaldainDistance(searched, movie)
        distanceList.append((d, dfMovies.loc[i, "Movie ID"]))
    distanceList = sorted(distanceList)[:10]
    return distanceList


def eucaldainDistance(x, y):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance


def main():
    result = getDistance('Dangerous Minds (1995)')
    print(result)


if __name__ == '__main__':
    main()

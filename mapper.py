import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin)
    next(reader, None)  # skip the headers

    for row in reader:
        # Following the given structure: movieId, title, genres, userId, rating, timestamp
        genres = row[2]
        rating = row[4]

        # Each movie can belong to multiple genres, separated by "|"
        for genre in genres.split('|'):
            print(f"{genre}\t{rating}")

if __name__ == '__main__':
    mapper()

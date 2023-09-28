import sys
from collections import defaultdict

def reducer():
    current_genre = None
    total_rating = 0
    count = 0
    genre_ratings = {}

    for line in sys.stdin:
        genre, rating = line.strip().split('\t')
        
        if current_genre == genre:
            total_rating += float(rating)
            count += 1
        else:
            if current_genre:
                avg_rating = total_rating / count
                genre_ratings[current_genre] = avg_rating

            current_genre = genre
            total_rating = float(rating)
            count = 1

    # Handle the last genre
    if current_genre == genre:
        avg_rating = total_rating / count
        genre_ratings[current_genre] = avg_rating

    # Print top 10 genres
    for genre, rating in sorted(genre_ratings.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{genre}\t{rating:.2f}")

if __name__ == '__main__':
    reducer()

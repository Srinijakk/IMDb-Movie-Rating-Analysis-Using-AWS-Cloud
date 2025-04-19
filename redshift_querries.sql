-- Top 10 highest-rated movies
SELECT Title, IMDB_Rating
FROM imdb_cleaned
ORDER BY IMDB_Rating DESC
LIMIT 10;

-- Average rating by genre
SELECT Genre, AVG(IMDB_Rating) AS AvgRating
FROM imdb_cleaned
GROUP BY Genre
ORDER BY AvgRating DESC;

-- Top 5 directors by average rating
SELECT Director, AVG(IMDB_Rating) AS AvgRating
FROM imdb_cleaned
GROUP BY Director
ORDER BY AvgRating DESC
LIMIT 5;

# Kdrama
As a true drama fan, I was interested in ***two things***:
1. Is there any relationship between drama rating and airing year
2. And if there is a correlation between the rating of a drama and the average age of the actors who play in this series.

***Data*** taken from [Kaggle](https://www.kaggle.com/datasets/robertonacu/tmdb-kdramas-2022). And originally from [The Movie Database (TMDB)](https://www.themoviedb.org/).

***Files:***
- logical_schema.png: logical schema of the k_drama database.
- create.sql: create k_drama database tables
- populate.py: Populate tables with data from .csv files.
- function.sql: a function that calculates the average age of the actors
- visualization.py: visualization code for the two questions of interest
- graps.png: visualization

I used ***python*** (pandas, matplotlib.pyplot, seaborn) and ***postgresql*** to complete this project.

***Conclusion***: Unfortunately, the graphs show that there is ***no relationship*** between the rating and the average age of the actors / year of airing.

***New thoughts***: In the future, I want to try to get information about the main actors of each series and only compare their average rating with the drama's rating, since I think that their variation will not be so wide (now the variation may be 60 years, as there may be secondary actors five and sixty-five years old). And I think from that we can see the grouping of the series by age and maybe also see some correlation.

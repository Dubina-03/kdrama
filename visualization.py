import psycopg2
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

username = '-------'
password = 'yourpasword'
database = 'k_drama'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:

    cur = conn.cursor()

    #getting the year of airing date and adding it with raiting
    cur.execute('''SELECT average_rating, extract(year from airing_date) as airing_year
                    FROM rating_date INNER JOIN  all_series ON rating_date.series_id = all_series.id
                    ORDER BY average_rating;''')
    series_popularity_1 = []
    year = []
    for row in cur:
        if row[1]:
            series_popularity_1.append(row[0])
            year.append(row[1])

    #with age_actor function getting the avg_age of actors of the serie and combine with rating
    cur.execute('''SELECT TRIM(name_series), average_rating, age_actor(cast_series.series_id) as age_avg
                    FROM rating_date INNER JOIN  all_series ON rating_date.series_id = all_series.id
                                     INNER JOIN  cast_series ON  all_series.id = cast_series.series_id
                    ORDER BY average_rating;''')
    series_popularity = []
    avg_age = []
    name = []
    for row in cur:
        if row[1]:
            name.append(row[0])
            series_popularity.append(row[1])
            avg_age.append(row[2])


fig, (bar_ax, dot_ax) = plt.subplots(1, 2)

#visualize first query
data_query_1 = pd.DataFrame({'series_rating':series_popularity_1, 'year':year})
bar_ax.set_title('Series rating & year of the airing date')
sns.scatterplot(data = data_query_1, x = 'year', y = 'series_rating', ax = bar_ax)
fig.autofmt_xdate(rotation=45)

#visualize second query
data_query_2 = pd.DataFrame({'name':name, 'series_rating':series_popularity, 'average_age':avg_age})
dot_ax.set_title('Series rating & average age of the actors')
sns.scatterplot(data = data_query_2, x = 'average_age', y = 'series_rating', ax = dot_ax)
fig.autofmt_xdate(rotation=45)


plt.get_current_fig_manager().resize(1900, 900)
plt.subplots_adjust(left=0.1,
                    bottom=0.321,
                    right=0.9,
                    top=0.967,
                    wspace=0.76,
                    hspace=0.195)
plt.savefig('graphs.png', dpi=350)
plt.show()

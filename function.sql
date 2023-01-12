--calculate average age of actors of the series
DROP FUNCTION IF EXISTS age_actor(id_serie integer);
CREATE OR REPLACE FUNCTION age_actor(id_serie integer)
    RETURNS FLOAT
    LANGUAGE 'plpgsql'
AS $$
Declare  
 avg_age FLOAT;  
BEGIN 
    SELECT AVG(extract(year from AGE(airing_date::DATE, birthday::DATE))) INTO avg_age
    FROM all_series INNER JOIN cast_series ON all_series.id=cast_series.series_id
    INNER JOIN people ON cast_series.actor_id=people.id
	WHERE cast_series.series_id = id_serie;
    RETURN avg_age;
END;
$$; 

SELECT * FROM age_actor(112888);
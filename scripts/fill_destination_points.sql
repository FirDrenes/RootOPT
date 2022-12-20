CREATE TABLE IF NOT EXISTS destination_points (
	point_id SERIAL PRIMARY KEY,
	point_name TEXT NOT NULL,
	latitude DOUBLE PRECISION NOT NULL,
	longitude DOUBLE PRECISION NOT NULL
);

-- clear before insertion
DELETE FROM destination_points;

INSERT INTO destination_points (point_name, latitude, longitude)
	SELECT
	name as point_name,
	st_y(st_transform(way, 4326)) as latitude,
	st_x(st_transform(way, 4326)) as longitude
	FROM planet_osm_point WHERE place='city' ORDER BY name;
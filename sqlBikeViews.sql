CREATE VIEW vw_bike_analysis AS
SELECT
    b.dteday,
    b.season,
    b.yr,
    b.mnth,
    b.hr,
    b.holiday,
    b.weekday,
    b.workingday,
    b.weathersit,
    b.temp,
    b.atemp,
    b.hum,
    b.windspeed,
    b.rider_type,
    b.riders,
    c.price,
    c.COGS,
    CAST(b.riders * c.price AS FLOAT) AS revenue,
    CAST(b.riders * c.COGS AS FLOAT) AS cost,
    CAST((b.riders * c.price) - (b.riders * c.COGS) AS FLOAT) AS profit,
    CAST(
        CASE 
            WHEN (b.riders * c.price) = 0 THEN NULL
            ELSE ((b.riders * c.price) - (b.riders * c.COGS)) / (b.riders * c.price)
        END
    AS FLOAT) AS profit_margin
FROM
(
    SELECT * FROM bike_share_yr_0
    UNION ALL
    SELECT * FROM bike_share_yr_1
) b
LEFT JOIN cost_table c
    ON b.yr = c.yr;

SELECT TOP 10 *
FROM vw_bike_analysis;
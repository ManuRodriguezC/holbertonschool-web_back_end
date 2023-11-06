-- Select some dates of the metal_bands
SELECT origin, SUM(fans) as nb_fans FROM metal_bands GROUP BY origin;
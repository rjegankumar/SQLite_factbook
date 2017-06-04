# Querying CIA World factbook database

The [World Factbook](https://www.cia.gov/library/publications/the-world-factbook/) is data published by the CIA which provides high level information about the geography, economy etc. of all the countries in the world. This dataset converted into a database was used to query some interesting information with the help of sqlite3.

## Files

| File name | Description |
| :--- | :--- |
| [area.py](area.py) | Python script to calculate land to water area ratio |
| [environment.yml](environment.yml) | Conda environment YAML |
| [factbook.db](factbook.db) | CIA World factbook database |
| [growth.py](growth.py) | Python script to compute the population growth |
| [next_steps.txt](next_steps.txt) | Ideas to further explore the database |
| [query.py](query.py) | Python script to query first 10 rows by population |

## Setup

- You must have [Anaconda](https://www.continuum.io/downloads) installed to run this code.
- Create a conda environment using [environment.yml](environment.yml) YAML file. More help on this can be found [here](https://conda.io/docs/using/envs.html#use-environment-from-file).

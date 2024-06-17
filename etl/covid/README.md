# API to MySQL pipeline

Given the task of ETL from an API. A covid-19 API was used, just the countries were extracted. A new table was created in the database and loaded with the extracted data.

- Poss improvements
  - Add more tables
    - Getting the statistics
- Decisions
  - It was decided to replace the table and not append because new data is not coming in.
  - This is also why the table if replaced if it exist.

## API from rapid API

### Extract

- headers blocked out to prevent unnecessary calls
- response converted to json

### Transform

- normalized into a pandas dataframe

## Local MySQL Connection

- password was replaced with \* to prevent spillage
- created table and set to replace because to limit double entries unless from the API

## Convert df to format for MySQL Insertion

### Load

- engine password was replaced with \* to prevent spillage

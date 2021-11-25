## Description:
Implement a simple Django application which has the following functionality:
- HTTP API 
  - **POST** /api/calculate (takes a csv input file)
    - The CSV file should have 3 columns - "S", "V" and "T"
    - For each row of the csv one of these must be empty, which means that it needs to be calculated
      - Example input CSV: <br/>
        S,V,T <br/>
        "3","5", "" <br/>
        "2","","3" <br/>
        "", "4", "5" <br/>
    - The API must synchronously calculate the unknown variable for each row and return an excel xlsx spreadsheet with all columns populated correctly (both "S", "V" and "T")
      - The correlation (formula) between the variables is: S = V * T
    - Each calculate request must be assigned an unique id and be recorded in the database 
    - Each response should be assigned unique id and be recorded in the database
      - The response should have a relation to the request in the database.
      - The response should contain the time it took to execute the request calculation function 
  - **GET** /api/responses - should return all responses as a json object that has the following fields for each response: request_id, response_id, calculation_time
- Admin part - create a simple admin site that could be used to browse through all entities created in the system and to edit them.
- Tests
  - Unit tests
  - Integration tests 
- Bonus (All of this is optional and we don't expect you to do all of it because it takes a lot of time.)
  - Deployment
  - CI / CD
  - Error collection
  - Monitoring
  - API docs / examples how to call the API
- Hints
  - Follow the widely adopted software development best practices
  - Deliver the code in a public GitHub repository
  - Use the appropriate design patterns at places where you expect that the functionality might change in future
  
--------------------------------------------------------------------------

## Implementation:
- make external package containing business-logic
- dockerized project
- add celery+rabbitmq for processing requests
# Promptly-API

Creative Writing Prompt API is a RESTful web service that provides users with ideas or suggestions for writing something creative, such as a story, a poem, a script, or an essay. The API allows users to:

## Pre-requisites and Local Development

- python
- pip


### Configuration
To install the necessary packages for the backend, execute the command ```pip install requirements.txt```. This will ensure that you have all the dependencies listed in the requirements file.

Run the application
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
The application is run on `http://127.0.0.1:5000/` by default.



### Tests
Navigate to the backend folder and run the following commands:
```bash
dropdb promptly                      // Drop the database
createdb promptly                    // Create the database    
psql -d promptly -f data.sql         // Create the tables and insert data
python tests.py                // Run tests
```


## API Reference

### Getting Started

- **Note:** Before accessing the following endpoints, ensure that you have a valid authentication token. You can include the token in the request headers as shown below:

```plaintext
Authorization: Bearer YOUR_AUTH_TOKEN
```

- Base URL: This application is run locally. By default on `http://127.0.0.1:5000/`.
  


- There are three types of users with different levels of access:
  - ADMIN: Can make any request.
  - USER:  Can access any `GET` request, and has full access to all endpoints in the prompts section.
  - GUEST: Can only access any `GET` request.

  - Admin token sample
```bash
  token
```

  - User token sample
```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkNRVVoxWmh5MlE1bmNYemdXOTBnNCJ9.eyJpc3MiOiJodHRwczovL3Byb21wdGx5MC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTY0MDc3ODAwMDE3NTA0MTQzNzQiLCJhdWQiOiJwcm9tcHRzIiwiaWF0IjoxNjkxNTcxMDc0LCJleHAiOjE2OTE2NTc0NzQsImF6cCI6IlhzQU5QV3VRVUNRRTZJbFR5UHR4cFZOZGNjblBFRXk5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJhZGQ6cHJvbXB0IiwiZGVsZXRlOnByb21wdCIsInVwZGF0ZTpwcm9tcHQiXX0.1E4PRzTwWGGYEusEP5sLMaTXHgq0_EPGHdPn5D5HeVtZp0Decr3FqtT5RKzkdLqiyHGYFCchWgS2d9AG5yKfZ7cAJtE-Xlyie4cuS1aueIFTPgha2BIt3LcMKTplBj8qA8bVFhzFJ9_CpQKhT9jO3iLTnx1q1ZpjK1rKQaCV-uRVg9xnyCaaJsmdVDI8dQPt16vTfMwkpCzhKv5ZCmj_c0_CtLoANOBpZOL6YFZe1LFuXOlk2f0UEEtVa8CE3E6NlDU-cJwZCKSdiA0yV-HXjf2se7wF1KzrMvoiAtIx70vWd9J-gVJz9_ZVzwp1T3DUiHxpY6yI3DnlGPMSab2ZNA
```
**Note**: No token needed to make `GET` request.

### Errors
Four error types will returned as JSON object if a request fail:
```json
{"success": False, "error": 405, "message": "method not allowed"}
```
- 400: Bad Request
- 401: Unauthorized
- 404: Resource Not Found
- 422: Not Processable
- 405: method not allowed
  

### Endpoints
### Listing or Creating Prompts
#### GET `/prompts`

- This endpoint retrieves a paginated list of prompts.
- Query parameters:
  - page: Page number (default: 1)
```json
{
  "success": true,
  "prompts": [...],  // List of prompts
  "total_prompts": 25
}
```
Example request:   `/prompts?page=2`

#### POST `/prompts`

- This endpoint allows the addition of new prompts.
- Requires authentication with permission 'add:prompt'.
- Request JSON payload:
```json
{
  "title": "New Prompt Title",
  "content": "This is the prompt content.",
  "genre_id": 1
}
```
Response:
```json
{
  "success": true,
  "Prompts": 26
}
```
Getting, Updating, and Deleting Prompts
#### GET `/prompts/{id}`

- This endpoint retrieves a specific prompt by its ID.
- Response:
```json
{
  "success": true,
  "prompt": {...}  // Details of the requested prompt
}
```
Example request: `/prompts/1`
#### PATCH `/prompts/{id}`

- This endpoint allows updating a specific prompt by its ID.
- Requires authentication with permission 'update:prompt'.
- Request JSON payload (at least one field is required):
```json
{
  "content": "Updated prompt content"
}
```
Response:
```json
{
  "success": true,
  "prompt_id": 1
}
```

#### DELETE `/prompts/{id}`

- This endpoint allows deleting a specific prompt by its ID.
- Requires authentication with permission 'delete:prompt'.
- Response:
```json
{
  "success": true,
  "prompt_id": 1
}
```
Example request: `/prompts/1`


### Listing or Creating Genres
#### GET `/genres`

- This endpoint retrieves a paginated list of genres.
- Query parameters:
- page: Page number (default: 1)
- Response:
```json
{
  "success": true,
  "genres": [...],  // List of genres
  "total_genres": 10
}
```
- Example request: `/genres?page=2`

#### POST `/genres`

- This endpoint allows the addition of new genres.
- Requires authentication with permission 'add:genre'.
- Request JSON payload:
```json
  {
    "name": "New Genre",
    "description": "Description of the new genre."
  }
```
- Response:
```json
  {
    "success": true,
    "total_genres": 11
  }
```
### Getting, Updating, and Deleting Genres
#### GET `/genres/{id}`

- This endpoint retrieves a specific genre by its ID.
- Response:
```json
{
  "success": true,
  "genre": {...}  // Details of the requested genre
}
```
- Example request: `/genres/1`


#### PATCH `/genres/{id}`

- This endpoint allows updating a specific genre by its ID.
- Requires authentication with permission 'update:genre'.
- Request JSON payload (at least one field is required):
```json
{
  "description": "Updated genre description"
}
```
- Response:

```json
{
  "success": true,
  "genre_id": 1
}
```

#### DELETE `/genres/{id}`

- This endpoint allows deleting a specific genre by its ID.
- Requires authentication with permission 'delete:genre'.
- Response:
```json
{
  "success": true,
  "genre_id": 1
}
```
- Example request: `/genres/1`

#### Note: Replace placeholders like {id} with actual values when making requests.





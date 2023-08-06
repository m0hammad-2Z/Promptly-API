# Promptly-API

Creative Writing Prompt API is a RESTful web service that provides users with ideas or suggestions for writing something creative, such as a story, a poem, a script, or an essay. The API allows users to:

## Pre-requisites and Local Development

- python
- pip


### Configuration
To install the necessary packages for the backend, navigate to the backend folder and execute the command ```pip install requirements.txt```. This will ensure that you have all the dependencies listed in the requirements file.

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
dropdb trivia                      //Drop the database
createdb trivia                    //Create the database    
psql bookshelf_test < books.psql   //Create the tables and insert data
python test_flaskr.py              //Run tests
```


## API Reference

### Getting Started
- Base URL: This application is run locally. By default on `http://127.0.0.1:5000/`.

- Authentication: No Authentication or API key needed.

### Errors
Four error types will returned as JSON object if a request fail:
```bash
{"success": False, "error": 405, "message": "method not allowed"}
```
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable
- 405: method not allowed

### Endpoints
#### GET /categories
- General
  - Get all available categories, success value and categories number.
- Sample `curl http://127.0.0.1:5000/categories`
```bash
{
    "categories": [
        "Science",
        "Art",
        "Geography",
        "History",
        "Entertainment",
        "Sports"
    ],
    "categories number": 6,
    "success": true
}
```


#### GET /categories/<category_id>
- General
  - Returns the category details for the specified ID.
  - Get category, success value.
- Sample `curl http://127.0.0.1:5000//categories/1`
```bash
{
    "categories": {
        "id": 1,
        "type": "Science"
    },
    "success": true
}
```

#### GET /questions
- General
  - Returns a list of paginated questions, success value, total number of questions and categories.
  - Results are paginated in groups of 10.
  - Include a request argument to choose page number, starting from 1.
- Sample `curl http://127.0.0.1:5000/questions`
```bash
{
    "categories": [
        "Science",
        "Art",
        "Geography",
        "History",
        "Entertainment",
        "Sports"
    ],
    "current_category": null,
    "questions": [
        {
            "answer": "My name is Mohammad Al-Zaro",
            "category": "1",
            "difficulty": 5,
            "id": 24,
            "question": "What is your name"
        },
        {
            "answer": "Blood",
            "category": "1",
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        },
        {
            "answer": "Alexander Fleming",
            "category": "1",
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        },
        {
            "answer": "The Liver",
            "category": "1",
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Mona Lisa",
            "category": "2",
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        {
            "answer": "One",
            "category": "2",
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": "3",
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": "3",
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Maya Angelou",
            "category": "4",
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "George Washington Carver",
            "category": "4",
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        }
    ],
    "success": true,
    "total_questions": 15
```

#### GET /categories/<category_id>/questions
- General
  - Retrieves questions based on the specified category ID.
  - Paginated in groups of 10.categories
  - Get success, questions, total_questions and current_category.
- Sample `curl http://127.0.0.1:5000/categories/1/questions`
```bash
{
    "success": true,
    "questions": [
        {
            "id": 1,
            "question": "What is the capital of France?",
            "answer": "Paris",
            "difficulty": 3,
            "category": "Geography"
        },
        ...
    ],
    "total_questions": 5,
    "categories": ["Science", "Art", "Geography", "Sports"],
    "current_category": "Geography"
}
```

#### DELETE /questions/<question_id>
- General
  - Deletes the question with the specified ID.
  - Return success value, question id and total questions after the deletaion proccess.
- Sample `curl http://127.0.0.1:5000/questions/5 -X DELETE`
```bash
{
    "success": true,
    "question id": 5,
    "total_questions": 19
}
```


#### POST /questions
- General
  - Creates a new question with the provided details.
  - Return success value and total questions after the added proccess.
- Sample `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{
    "question": "What is the capital of Germany?",
    "answer": "Berlin",
    "category": "Geography",
    "difficulty": 2
}'`
```bash
{
    "success": true,
    "total_questions": 20
}
```


#### POST /questions/search
- General
  - Searches for questions that include the specified search term.
  - Return success value, questions, total questions founded.
- Sample `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{
    "searchTerm": "capital"}'`
  
```bash
{
    "success": true,
    "questions": [
        {
            "id": 1,
            "question": "What is the capital of France?",
            "answer": "Paris",
            "difficulty": 3,
            "category": "Geography"
        },
        ...
    ],
    "total found": 2
}
```


#### POST /questions/play
- General
  - Generates a random question for the quiz based on the specified category and previous questions.
  - Return success value and random question from the same category.
- Sample `curl http://127.0.0.1:5000/questions/play -X POST -H "Content-Type: application/json" -d '{
    "quiz_category": {
        "type": "Geography",
        "id": "2"
    },
    "previous_questions": [1, 2, 3]
}'`
  
```bash
{
    "success": true,
    "question": {
        "id": 4,
        "question": "What is the capital of Germany?",
        "answer": "Berlin",
        "difficulty": 2,
        "category": "Geography"
    }
}
```









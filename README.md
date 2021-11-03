# Saarthi.ai_book_lib_api

This Project is REST API service to get information about books

#This Project In currently Hosted on https://saarthi.deltatrek.in
Live Access URLs are  given below

GET    http://saarthi.deltatrek.in/api/v1/external-books?name=:nameOfBook
POST   http://saarthi.deltatrek.in/api/v1/books
GET    http://saarthi.deltatrek.in/api/v1/books
GET    http://saarthi.deltatrek.in/api/v1/books/:id
PATCH  http://saarthi.deltatrek.in/api/v1/books/:id
DELETE http://saarthi.deltatrek.in/api/v1/books/:id


Access URLs of project as mentiond in assignment

GET http://localhost:8000/api/v1/external-books?name=:nameOfABook
response-type : application/json
descripton : This URL get book details from  Ice And Fire API 

    
POST http://localhost:8000/api/v1/books
response-type : application/json
Description : This URL save a book details in local SQlite3 DB
Params structure: {
            "name": "A Clash of Kings",
            "isbn": "978-0553108033",
            "authors": [
                "George R. R. Martin"
            ],
            "number_of_pages": 768,
            "publisher": "Bantam Books",
            "country": "United States", 
            "release_date": "1999-02-02"
        }
        
GET http://localhost:8000/api/v1/books 
response-type : application/json
description : This URL returns a List of all Books Details From local DB

GET http://localhost:8080/api/v1/books/:id 
response-type : application/json
description : This URL returns Book Details of given ID From local DB

PATCH http://localhost:8080/api/v1/books/:id
response-type : application/json
description : This URL Update Details of book of given ID in local DB

DELETE  http://localhost:8080/api/v1/books/:id
response-type : application/json
description : This URL Delete Details of book of given ID From local DB

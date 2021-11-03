# Saarthi.ai_book_lib_api

This Project is REST API service to get information about books

#This Project In currently Hosted on https://saarthi.deltatrek.in
Live Access URLs are  given below

<h4>GET    http://saarthi.deltatrek.in/api/v1/external-books?name=:nameOfBook</h4>
<h4>POST   http://saarthi.deltatrek.in/api/v1/books
<h4>GET    http://saarthi.deltatrek.in/api/v1/books
<h4>GET    http://saarthi.deltatrek.in/api/v1/books/:id
<h4>PATCH  http://saarthi.deltatrek.in/api/v1/books/:id
<h4>DELETE http://saarthi.deltatrek.in/api/v1/books/:id
<br>
<h3>Access URLs of project as mentiond in assignment

<h4>GET http://localhost:8000/api/v1/external-books?name=:nameOfABook
<h4>response-type : application/json
<h4>descripton : This URL get book details from  Ice And Fire API 
 <br>
<h4>POST http://localhost:8000/api/v1/books
<h4>response-type : application/json
<h4>Description : This URL save a book details in local SQlite3 DB
<p>Params structure: {
            "name": "A Clash of Kings",
            "isbn": "978-0553108033",
            "authors": [
                "George R. R. Martin"
            ],
            "number_of_pages": 768,
            "publisher": "Bantam Books",
            "country": "United States", 
            "release_date": "1999-02-02"
    }</p>
<br>        
<h4>GET http://localhost:8000/api/v1/books 
<h4>response-type : application/json
<h4>description : This URL returns a List of all Books Details From local DB
<br>
<h4>GET http://localhost:8080/api/v1/books/:id 
<h4>response-type : application/json
<h4>description : This URL returns Book Details of given ID From local DB
<br>
<h4>PATCH http://localhost:8080/api/v1/books/:id
<h4>response-type : application/json
<h4>description : This URL Update Details of book of given ID in local DB
<br>
<h4>DELETE  http://localhost:8080/api/v1/books/:id
<h4>response-type : application/json
<h4>description : This URL Delete Details of book of given ID From local DB

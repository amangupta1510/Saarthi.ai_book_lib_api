# Saarthi.ai_book_lib_api

This Project is REST API service to get information about books

# you need to install rest Framework to browser access

#GET https://aman1510.pythonanywhere.com/admin
#username : admin   password : admin123

<h3>Access URLs of project as mentiond in assignment

<h4>GET https://aman1510.pythonanywhere.com/api/v1/external-books?name=:nameOfABook
<h4>response-type : application/json
<h4>descripton : This URL get book details from  Ice And Fire API 

<h4>POST https://aman1510.pythonanywhere.com/api/v1/books
<p>response-type : application/json
<p>Description : This URL save a book details in local SQlite3 DB
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
<h4>GET https://aman1510.pythonanywhere.com/api/v1/books 
<p>response-type : application/json
<p>description : This URL returns a List of all Books Details From local DB

<h4>GET https://aman1510.pythonanywhere.com/api/v1/books/:id 
<p>response-type : application/json
<p>description : This URL returns Book Details of given ID From local DB

<h4>PATCH https://aman1510.pythonanywhere.com/api/v1/books/:id
<p>response-type : application/json
<p>description : This URL Update Details of book of given ID in local DB

<h4>DELETE  https://aman1510.pythonanywhere.com/api/v1/books/:id
<p>response-type : application/json
<p>description : This URL Delete Details of book of given ID From local DB
            
 <img src="https://github.com/amangupta1510/Task_Board-Mangement/blob/master/screenshot1.jpg">
 
 <img src="https://github.com/amangupta1510/Task_Board-Mangement/blob/master/screenshot2.jpg">

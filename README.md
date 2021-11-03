# Saarthi.ai_book_lib_api
<h2>note Live hosting not fetch data from external api because of hosting restriction but it's work perfectally fine in local server as you can see in last screenshot
This Project is REST API service to get information about books<h2>

# you need to install rest Framework by using below command to browser access
<p>pip install djangorestframework
<p>pip install markdown      
<p>pip install django-filter

#GET https://aman1510.pythonanywhere.com/admin
#username : admin   password : admin123

<h3>Access URLs of project as mentiond in assignment

<h4>GET https://aman1510.pythonanywhere.com/api/external-books?name=:nameOfABook
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
            
 <img src="https://github.com/amangupta1510/Saarthi.ai_book_lib_api/blob/master/screenshot 1.png">
 <img src="https://github.com/amangupta1510/Saarthi.ai_book_lib_api/blob/master/screenshot 2.png">
 <img src="https://github.com/amangupta1510/Saarthi.ai_book_lib_api/blob/master/screenshot 3.png">

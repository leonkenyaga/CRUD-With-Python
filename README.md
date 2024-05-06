A RESTful API in Python that can perform Create, Read, Update and Delete operations in a database 🚀🚀

Post user's data on http://localhost:5000/postUser in the following format



{
    "name": "string",
    "password":"string",
    "email":"string",
    "friends": [ "string", 
               "string"
    ]
}


Fetch user's data (latest posting) on http://localhost:5000/getUser 

Note: You have to post before fetching otherwise will return error

Run with 'flask run' command
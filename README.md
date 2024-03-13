<img src="/img/9aFInu9ym.png">

# AirBnB clone - The console

Creation and implementation of a AirBnB clone. This is the first step towards building a full web application: *the AirBnB clone*


## Features

- Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances
- A simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- All classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- manage (create, update, destroy, etc) objects via a console / command interpreter
- The first abstracted storage engine of the project in JSON
- Unittests to validate all our classes and storage engine


## The Command Line Interpreter

For this project, we are using a custom shell interpreter, similar to a regular shell to help us manage our object.

#Features:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Show all created objects
- Modify/Update attributes of an existing Object
- Check if an Object exists
- Destroy an Object


## Objective of this project

By the end of this project, I'm expected to have understood:

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function


### Content of Directory ###
* Models Folder: Classes of the project.
    BaseModel is the parent Class. The other classes include (amenity, city, place, review, state, user)  which inherit from BaseModel and specify others attributes for itselfs.
* Tests Folder : Unittests for the project
* AUTHORS: Information about the authors
* console.py: custom shell to execute our program
* file.json: JSON file with all data concerning our instances


## Examples of Usage

### Execution ###
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) quit
$
```
### create ###
Creat an instance and show us the id number
```
leumars@Leumas-PC:~/AirBnB_clone$ ./console.py 
(hbnb) create BaseModel
b6df75dc-6706-4485-bf76-482067f1bb0d
(hbnb)  
```

### Show ###
Show the Class, object if the id is especified and its attributes
```
(hbnb) show BaseModel b6df75dc-6706-4485-bf76-482067f1bb0d
[BaseModel] (b6df75dc-6706-4485-bf76-482067f1bb0d) {'id': 'b6df75dc-6706-4485-bf76-482067f1bb0d', 'created_at': datetime.datetime(2024, 3, 11, 3, 52, 58, 92659), 'updated_at': datetime.datetime(2024, 3, 11, 3, 52, 58, 92695)}
(hbnb) 
```
### all ###
shows all the instances
```
(hbnb) all BaseModel
["[BaseModel] (4a675be2-4998-487d-9445-cafcab7ca2dc) {'id': '4a675be2-4998-487d-9445-cafcab7ca2dc', 'created_at': datetime.datetime(2024, 3, 11, 1, 40, 48, 497405), 'updated_at': datetime.datetime(2024, 3, 11, 1, 40, 48, 497516)}", "[BaseModel] (f37db1e6-f983-4329-bc12-592073f15547) {'id': 'f37db1e6-f983-4329-bc12-592073f15547', 'created_at': datetime.datetime(2024, 3, 11, 1, 58, 32, 4840), 'updated_at': datetime.datetime(2024, 3, 11, 1, 58, 32, 4874), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[BaseModel] (dcc2b9dc-f5b0-4fbe-965f-2632cf948e4b) {'id': 'dcc2b9dc-f5b0-4fbe-965f-2632cf948e4b', 'created_at': datetime.datetime(2024, 3, 11, 1, 58, 32, 5285), 'updated_at': datetime.datetime(2024, 3, 11, 1, 58, 32, 5317), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}", "[BaseModel] (b6df75dc-6706-4485-bf76-482067f1bb0d) {'id': 'b6df75dc-6706-4485-bf76-482067f1bb0d', 'created_at': datetime.datetime(2024, 3, 11, 3, 52, 58, 92659), 'updated_at': datetime.datetime(2024, 3, 11, 3, 52, 58, 92695)}"]
(hbnb) 
```
### update ###
update an instance
```
(hbnb) show BaseModel 4a675be2-4998-487d-9445-cafcab7ca2dc
[BaseModel] (4a675be2-4998-487d-9445-cafcab7ca2dc) {'id': '4a675be2-4998-487d-9445-cafcab7ca2dc', 'created_at': datetime.datetime(2024, 3, 11, 1, 40, 48, 497405), 'updated_at': datetime.datetime(2024, 3, 11, 1, 40, 48, 497516)}
(hbnb) update BaseModel 4a675be2-4998-487d-9445-cafcab7ca2dc name "Betty"
(hbnb) show BaseModel 4a675be2-4998-487d-9445-cafcab7ca2dc
[BaseModel] (4a675be2-4998-487d-9445-cafcab7ca2dc) {'id': '4a675be2-4998-487d-9445-cafcab7ca2dc', 'created_at': datetime.datetime(2024, 3, 11, 1, 40, 48, 497405), 'updated_at': datetime.datetime(2024, 3, 11, 1, 40, 48, 497516), 'name': 'Betty'}
(hbnb) 
```
### Destroy ###
Deletes an instance
```
(hbnb) destroy BaseModel 4a675be2-4998-487d-9445-cafcab7ca2dc
(hbnb) destroy BaseModel 4a675be2-4998-487d-9445-cafcab7ca2dc
** no instance found **
(hbnb) 
```
---

## Installation

* Clone the repository. git clone https://github.com/leumars-o/AirBnB_clone.git
* Open the /AirBnB_clone directory and execute console.py

### Setup

* You need Python interpreter.
All files were interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5) and code checked using the pycodestyle (version 2.8.*)


## Team

- GitHub at <a href="https://github.com/leumars-o">`Leumars`</a>
- GitHub at <a href="https://github.com/PrincewillDev">`Princewill`</a>


## Support by leaving a Star 🌟 

Feel free to contact us!

- GitHub at <a href="https://github.com/leumars-o">`Leumars`</a>


---

## License

Free Source Code

AirBnB clone - The console
================================

Welcome to the AirBnB clone project!
------------------

![image](https://user-images.githubusercontent.com/61886501/163566912-4fc76817-3e9d-4a8f-9aae-a8ec9f9f26f7.png)


` First step: Write a command interpreter to manage AirBnB objects.`

### What's a command interpreter?


-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc...
-   Do operations on objects (count, compute stats, etc...)
-   Update attributes of an object
-   Destroy an object


Learning Objectives
-------------------

### General

-   How to create a Python package
-   How to create a command interpreter in Python using the `cmd` module
-   What is Unit testing and how to implement it in a large project
-   How to serialize and deserialize a Class
-   How to write and read a JSON file
-   How to manage `datetime`
-   What is an `UUID`
-   What is `*args` and how to use it
-   What is `**kwargs` and how to use it
-   How to handle named arguments in a function


### Execution

Your shell work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

```

`\
`

## AUTHORS

***Tarek KHEIR* | Aurélie CEDIA**

<a href="https://github.com/tarekkheir/AirBNB_clone_v2" align="right">Next step (AirBNB clone V2)</a>

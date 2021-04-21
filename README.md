# CS-340
Project for CS-340

Module 8 Journal

Q:
How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

A:
Maintainable code contains well-written comments that can explain the purpose of the code quickly and concisely so that reviewers can understand what it does before (or without the need to) reading it. Maintainable code should also use as few lines of code as possible without being unnecessarily abstract. Maintainable code should also be easy to test and easy to modify.
Readable code should be properly (and consistently) indented with a reasonable number of spaces (4 to 8 tends to be the norm). Readable code should also not span too much of a line and should be cut to a new line in a place that makes sense and does not impede the execution of the code (such as in the case of using Python). Readable code should be grouped properly (ie. constants, helper methods, etc.). Readable code should also be DRY (don't repeat yourself) and should not be littered with excessive comments.
Adaptable code should be written in a way that allows the code to be changed fairly easily in the event of a change. An example of adaptable code is code that is written in a way that would allow changing from a SQL to a NoSQL database relatively easy. Another example of adaptable code is code that is written by a developer who is reasonably sure the requirements will change and keeps their code modular and well-documented.
For the CRUD module of this project, the create, read, update, and delete methods were written with the above ideas in mind. The CRUD methods could easily allow more arguments (if they were needed), could be modified to connect with another database type (would require a lot of code change, but same structure), and were all created with as few lines of code as possible. This module was well-made and tested and did not result in any known errors between the database and the client-side application. In the future, this CRDU python module could easily be used for any other database/collection with any application interface that supports create, read, update, and delete operations (*The queries will need to be client-side as they are passed to the CRUD module as arguments).

Q:
How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

A:
I approached this problem knowing that a persistent database and dynamic interface coupled with logical queries was the most efficient way to solve the clients problem. The client had specific requirements for each animal type they would be searching for and queries to the database could be constructed to show the exact matches for the animals in question. The data was given to us in a csv file (as you would find in Excel or Google Sheets) and I imported it into a database collection using the correct commands. With the database set, it made sense to allow adding to, updating, reading, and deleting information form the existing database. A python module was a quick and efficient solution to allow CRUD and could easily be tested in unit tests. From there, the front end could be made to predefine queries and allow further refining of the animals in question. This project was different than previous projects in other courses because it was a full-stack solution to a fairly legitimate problem. I approached this course with a little more creativity and experimentation than in other courses. In the future, I would certainly use MongoDB and indexing to create databases for projects. I would Utilize the language based on other requirements, but I feel Python is more than satisfactory. I would not use Dash in the future because it is not well-documented and isn't used enough for an efficient community. If I were to write this project again with no technical requirements, it would be written in Java, MongoDB, HTML, CSS, JavaScript, with a front end framework like React.

Q:
What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

A:
Computer scientists are engineers and logical artists. A computer scientist uses technology (computer technology) to solve problems in the most efficient and pragmatic way possible. Computer science is broad in it's disciples, but at it's core it's purpose is to solve problems faster and more efficiently than a human or mechanical system could (technically, there is overlap between mechanical computers and electrical computers, but for this case I refer only to electrical). 

0x00. AirBnB clone - The console

AirBnb the console is  the first step of creating our AirBnB web page , in the Console part is A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

The console
create your data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

Files and Directories
models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
tests directory will contain all unit tests.
console.py file is the entry point of our command interpreter.
models/base_model.py file is the base class of all our models. It contains common elements:
attributes: id, created_at and updated_at
methods: save() and to_json()
models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.
Description of the command interpreter
Commands	Description
quit	Quits the console
Ctrl+D	Quits the console
help or help <command>	Displays all commands or Displays instructions for a specific command
create <class>	Creates an object of type , saves it to a JSON file, and prints the objects ID
show <class> <ID>	Shows string representation of an object
destroy <class> <ID>	Deletes an objects
all or all <class>	Prints all string representations of all objects or Prints all string representations of all objects of a specific class
update <class> <id> <attribute name> "<attribute value>"	Updates an object with a certain attribute (new or existing)
<class>.all()	Same as all <class>
<class>.count()	Retrieves the number of objects of a certain class
<class>.show(<ID>)	Same as show <class> <ID>
<class>.destroy(<ID>)	Same as destroy <class> <ID>
<class>.update(<ID>, <attribute name>, <attribute value>	Same as update <class> <ID> <attribute name> <attribute value>
<class>.update(<ID>, <dictionary representation>)	Updates an objects based on a dictionary representation of attribute names and values

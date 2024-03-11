#!/usr/bin/python3
"""
This from models.engine import filemodule create a custom console for manipulating data
without a visual interface.

Class:
    HBNBCommand:- This class creates a custom Command line
    interface by inheritting from cmd module.
"""
import cmd
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This class inherits the cmd class as its base class.
    It creates a custom command line.

    Attributes:
        prompt:- Class attribute for displaying the prompt
        in the command line interface.

    Methods:
        do_quit:- This method quits the command line
        interface by invoking the <quit command>.

        do_EOF:- This method handles EOF by sending an
        end of file signal when Ctrl-D is pressed.

        do_create:- This method creates an instance of BaseModel
        save the file to json and prints it id.

        do_show:- This Method prints the string representation
        of an instance based on the class name and id.

        do_all:- This method prints the string representation of all instances
        based on the class name and id.

        do _update:- Updates the attribute of an Object based on the class name
        and ID

    """
    prompt = "(hbnb) "
    class_list = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

    def do_quit(self, args):
        """ Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Handle the EOF (End of File) command which is
        triggered by pressing Ctrl-D.
        """
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel and print its id"""
        tokens = args.split()
        if not self.class_check(tokens):
            return
        new_instance = eval(tokens[0] + '()')
        if isinstance(new_instance, BaseModel):
            new_instance.save()
            print(new_instance.id)
        return
    
    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        tokens = args.split()
        objects = models.storage.all()
        if not self.class_check(tokens):
            return
        if not self.id_check(tokens):
            return
        key = f"{tokens[0]}.{tokens[1]}"
        print(objects[key])
    
    def do_destroy(self, args):
        """ Deletes an object/instance using classname and id """
        tokens = args.split()
        objects = models.storage.all()
        if not self.class_check(tokens):
            return
        if not self.id_check(tokens):
            return
        key = f"{tokens[0]}.{tokens[1]}"
        del objects[key]
        models.storage.save()
                
    def do_all(self, args):
        """all command prints a string repr of all instances
        based on class name and id

        Args:
            args (string): Class name and Instance ID

        """
        tokens = args.split()
        objects = models.storage.all()
        new_list = []
        if len(tokens) == 0:
            for value in objects.values():
                new_list.append(str(value))
        elif tokens[0] in HBNBCommand.class_list:
            for key, value in objects.items():
                if tokens[0] == value.__class__.__name__:
                    new_list.append(str(value))
        else:
            print("** class doesn't exist **")
            return False
        print(new_list)
    
    def do_update(self, args):
        """updates the attributes of an Object

        Args:
            args (str): ClassName ID Attribute "Value"

        """
        tokens = args.split()
        if tokens[3].find('"') != -1:
            temp = tokens[3]
            start = temp.find('"')
            end = temp.find('"', start + 1)
            tokens[3] = temp[start + 1 : end]

        objects = models.storage.all()

        if not self.class_check(tokens):
            return
        if not self.id_check(tokens):
            return
        key = f"{tokens[0]}.{tokens[1]}"
        setattr(objects[key], tokens[2], tokens[3])
        models.storage.save()
    
    @classmethod
    def class_check(cls, tokens):
        """Class method checks if a given token matches
        a class name in the `class_list`

        """
        if len(tokens) == 0:
            print('** class name missing **')
            return False
        elif tokens[0] not in cls.class_list:
            print("** class doesn't exist **")
            return False
        return True
    
    @staticmethod
    def id_check(tokens):
        """Static method to verify the id.
        """
        if len(tokens) < 2:
            print('** instance id missing **')
            return False
        objects = models.storage.all()
        key = f"{tokens[0]}.{tokens[1]}"
        if key not in objects.keys():
            print('** no instance found **')
            return False
        return True
    
    @staticmethod
    def attr_check(tokens):
        """static method to verify a command passed to
        update an attribute is valid
        
        """
        if len(tokens) < 3:
            print("** attribute name missing **")
            return False
        if len(tokens) < 4:
            print("** value missing **")
        return True
    
    def emptyline(self):
        "Do nothing when an emptyline is entered"
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()

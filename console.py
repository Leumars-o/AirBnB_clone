#!/usr/bin/python3
"""
This module create a custom console for manipulating data without a visual interface.

Class:
    HBNBCommand:- This class creates a custom Command line interface by inheritting from cmd module.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class inherits the cmd class as its base class.
    It creates a custom command line.

    Attributes:
        prompt:- Class attribute for displaying the prompt in the command line interface.

    Methods:
        do_quit:- This method quits the command line interface by invoking the <quit command>.
        do_EOF:- This method handles EOF by sending an end of file signal when Ctrl-D is pressed.
    """
    prompt = "(hbnb)"

    def do_quit(self, args):
        """ Quit command to exit the program
        """
        return True
    
    def do_EOF(self, line):
        """
        Handle the EOF (End of File) command which is triggered by pressing Ctrl-D.
        """
        return True
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()


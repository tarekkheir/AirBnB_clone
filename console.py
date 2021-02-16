#!/usr/bin/python3
"""
HBNBCommand class that contains the entry point of the command interpreter
"""
import cmd
import sys
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    The command interpreter implement:
     - quit and EOF to exit the program
     - help
     - a custom prompt: (hbnb)
     - an empty line + ENTER shouldn’t execute anything
    """

    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel,
               'User': User,
               'City': City,
               'State': State,
               'Place': Place,
               'Amenity': Amenity,
               'Review': Review}

    def do_quit(self, arg):
        """
        Quit and EOF to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Quit and EOF to exit the program
        """
        return True

    def emptyline(self):
        """
        An empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file)
        and prints the id
        """
        if len(arg) < 1:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new = HBNBCommand.classes[arg]()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split(" ")
        all_objs = storage.all()
        if len(arg) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            k = args[0] + "." + args[1]
            try:
                print(all_objs[k])
            except:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split(" ")
        all_objs = storage.all()
        if len(arg) <= 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            k = args[0] + "." + args[1]
            try:
                del(all_objs[k])
                storage.save()
            except:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """
        all_objs = storage.all()
        if len(arg) < 1:
            for obj_id in all_objs.keys():
                print("[\"{}]".format(all_objs[obj_id]))
        else:
            if arg not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for k, v in all_objs.items():
                    class_name = k.split(".")
                    if class_name[0] == arg:
                        print("[\"{}]".format(all_objs[k]))

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = arg.split(" ")
        all_objs = storage.all()
        if len(arg) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing ")
        elif len(args) < 4:
            print("** value missing **")
        else:
            k = args[0] + "." + args[1]
            try:
                obj = all_objs[k]
                setattr(obj, args[2], args[3])
                storage.save()
            except:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

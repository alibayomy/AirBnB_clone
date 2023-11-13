#!/usr/bin/python3
"""Module to represent a command line interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split
import re


def arg_parse(arg):
    """Split the 'arg' string to a list of substrings
    and removing leading and trailing spaces from the string

    Arguments:
        arg (str): string to be splitted.
    """
    crl_braces = re.search(r"\{(.*?)\}", arg)
    sqr_brkt = re.search(r"\[(.*?)\]", arg)
    if crl_braces is None:
        if sqr_brkt is None:
            return [i.strip(",") for i in split(arg)]
        else:
            args_l = split(arg[:sqr_brkt.span()[0]])
            result = [i.strip(",") for i in args_l]
            result.append(sqr_brkt.group())
            return result
    else:
        args_l = split(arg[:crl_braces.span()[0]])
        result = [i.strip(",") for i in args_l]
        result.append(crl_braces.group())


class HBNBCommand(cmd.Cmd):
    """Class to contains the entry point of the command interpreter

    Attributes:
        prompt (str): Custom propmt for the command interpreter.
        __classes_names (list): list of classes names used in this package.
    """

    prompt = "(hbnb) "
    __classes_names = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
    }

    def do_quit(self, arg):
        """Exit the program when enter 'exit' command"""
        return True

    def do_EOF(self, arg):
        """Exit the program when press CTRL+D from keyboard"""
        print()
        return True

    def do_help(self, arg: str):
        """Documented commands (type help <topic>)"""
        return super().do_help(arg)

    def emptyline(self):
        """Nothing is done when enter an empty line"""
        pass

    def __syntax_check(args_list, all_objcs=None, f1=None, f2=None):
        """Handle syntax error messages

        Arguments:
            args_list (list): list of strings to be checked.
            all_objects (dict): storage.__objects, or None if not given.
            f1 (str): indicate 's' syntax to add more 'show()' syntax checks.
            f2 (str): indicate 'u' syntax to add more 'update()' syntax checks.
        """
        if len(args_list) == 0:
            print("** class name missing **")
            return False
        elif args_list[0] not in HBNBCommand.__classes_names:
            print("** class doesn't exist **")
            return False
        elif f1 == "s":
            if len(args_list) == 1:
                print("** instance id missing **")
                return False
            elif all_objcs is not None:
                if "{}.{}".format(args_list[0], args_list[1]) not in all_objcs:
                    print("** no instance found **")
                    return False
                elif f2 == "u":
                    if len(args_list) < 3:
                        print("** attribute name missing **")
                        return False
                    elif len(args_list) == 3:
                        try:
                            type(eval(args_list[2])) != dict
                        except NameError:
                            print("** value missing **")
                            return False
                    elif len(args_list) > 4:
                        pass
                    elif len(args_list) < 4:
                        print("** value missing **")
                        return False
                    else:
                        return True
        else:
            return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel class, save it to JSON file
        and print its id"""
        args_list = arg_parse(arg)
        if HBNBCommand.__syntax_check(args_list) is False:
            return
        else:
            class_obj = eval(args_list[0])()
            print(class_obj.id)
            storage.save()

    def do_show(self, arg):
        """Print the string representation of an instance
        based on the class name and id"""
        all_objs = storage.all()
        args_list = arg_parse(arg)
        if HBNBCommand.__syntax_check(args_list, all_objs, "s") is False:
            return
        else:
            found_obj = all_objs["{}.{}".format(args_list[0], args_list[1])]
            print(found_obj)

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id
        and save the changes to the JSON file"""
        all_objs = storage.all()
        args_list = arg_parse(arg)
        if HBNBCommand.__syntax_check(args_list, all_objs, "s") is False:
            return
        else:
            to_del_obj = "{}.{}".format(args_list[0], args_list[1])
            del storage.all()[to_del_obj]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not
        on the class name"""
        args_l = arg_parse(arg)
        if len(args_l) > 0 and args_l[0] not in HBNBCommand.__classes_names:
            print("** class doesn't exist **")
        else:
            all_objs = []
            for obj in storage.all().values():
                if len(args_l) == 0:
                    all_objs.append(obj.__str__())
                elif len(args_l) > 0 and args_l[0] == obj.__class__.__name__:
                    all_objs.append(obj.__str__())
            print(all_objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute and save changes to the JSON file"""
        args_list = arg_parse(arg)
        all_objs = storage.all()
        if HBNBCommand.__syntax_check(args_list, all_objs, "s", "u") is False:
            return
        else:
            c_name = args_list[0]
            insta_id = args_list[1]
            attrib_name = args_list[2]
            attrib_str = args_list[3]
            if attrib_str.startswith('"') and attrib_str.endswith('"'):
                attrib_value = attrib_str[1:-1]
            else:
                attrib_value = attrib_str

            simple_types = ["string", "integer", "float"]

            if len(args_list) == 4:
                obj_key = all_objs["{}.{}".format(c_name, insta_id)]
                dict_keys = obj_key.__class__.__dict__
                if attrib_name in dict_keys.keys():
                    attrib_type = type(dict_keys[attrib_name])
                    obj_key.__dict__[attrib_name] = attrib_type(attrib_value)
                else:
                    obj_key.__dict__[attrib_name] = attrib_value

            elif type(eval(attrib_name)) == dict:
                obj_key = all_objs["{}.{}".format(c_name, insta_id)]
                dict_keys = obj_key.__class__.__dict__
                for key, value in eval(attrib_name).items():
                    if (key in dict_keys.keys()
                            and type(dict_keys[key]) in simple_types):
                        attrib_type = type(dict_keys[key])
                        obj_key.__dict__[key] = attrib_type(value)
                    else:
                        obj_key.__dict__[key] = value

            storage.save()

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        cmd_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }
        ptrn_mtch = re.search(r"\.", arg)
        if ptrn_mtch is not None:
            argl = [arg[:ptrn_mtch.span()[0]], arg[ptrn_mtch.span()[1]:]]
            ptrn_mtch = re.search(r"\((.*?)\)", argl[1])
            if ptrn_mtch is not None:
                cmd = [argl[1][:ptrn_mtch.span()[0]], ptrn_mtch.group()[1:-1]]
                if cmd[0] in cmd_dict.keys():
                    call = "{} {}".format(argl[0], cmd[1])
                    return cmd_dict[cmd[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_count(self, arg):
        """count the instances of a given class."""
        args_list = arg_parse(arg)
        count = 0
        for obj in storage.all().values():
            if args_list[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()

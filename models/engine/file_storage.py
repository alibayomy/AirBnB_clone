#!/usr/bin/python3
"""Module to represent FileStorage class"""
import json
from os.path import exists, isfile


class FileStorage():
    """Class to represent the file storage for the AirBnB clone project

    Attributes:
        __file_path (str): JSON file path
        __object (dict): dictionary of objects to be saved in the JSON file
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return the dictionary of objects saved in '__objects' attribute"""
        return self.__objects

    def new(self, obj):
        """Set the obj with the formatted key in the '__objects' dictionary

        Args:
            obj (any): the object to be saved.
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serialize '__objects' and save it to the JSON file"""
        serialized_dict = self.__objects
        new_objs_dict = {}
        for obj in serialized_dict.keys():
            new_objs_dict[obj] = serialized_dict[obj].to_dict()

        with open(self.__file_path, 'w') as file_json:
            json.dump(new_objs_dict, file_json, indent=2)

    def reload(self):
        """Deserialize the JSON file to '__objects'
        only if the JSON file exists; otherwise, nothing return"""
        from models import base_model
        __class_type = {'BaseModel': base_model.BaseModel}
        if exists(FileStorage.__file_path) and isfile(self.__file_path):
            with open(FileStorage.__file_path, 'r') as file_json:
                data = json.load(file_json)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_obj = __class_type.get(class_name)
                    if class_obj:
                        instance = class_obj(**value)
                        self.new(instance)

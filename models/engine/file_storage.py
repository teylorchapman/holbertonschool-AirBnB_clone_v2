#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models import city, place, review, state, amenity, user, base_model


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    classes = {
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'Amenity': amenity.Amenity,
        'User': user.User
    }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage if cls specified, only returns that class"""
        if cls is not None:
            if cls in self.classes.keys():
                cls = self.classes.get(cls)
            spec_rich = {}
            for ky, vl in self.__objects.items():
                if cls == type(vl):
                    spec_rich[ky] = vl
            return spec_rich
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'City': city.City,
            'Place': place.Place,
            'Review': review.Review,
            'State': state.State,
            'Amenity': amenity.Amenity,
            'User': user.User
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes an obj from __objects if it's inside"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """Deserializes the JSON file to objects"""
        self.reload()

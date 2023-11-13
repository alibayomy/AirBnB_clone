#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel siper
                class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        mb1 = BaseModel()
        mb2 = BaseModel()
        self.assertNotEqual(mb1.id, mb2.id)

    def test_two_models_different_created_at(self):
        mb1 = BaseModel()
        sleep(0.05)
        mb2 = BaseModel()
        self.assertLess(mb1.created_at, mb2.created_at)

    def test_two_models_different_updated_at(self):
        mb1 = BaseModel()
        sleep(0.05)
        mb2 = BaseModel()
        self.assertLess(mb1.updated_at, mb2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        mb = BaseModel()
        mb.id = "123456"
        mb.created_at = mb.updated_at = dt
        mbstr = mb.__str__()
        self.assertIn("[BaseModel] (123456)", mbstr)
        self.assertIn("'id': '123456'", mbstr)
        self.assertIn("'created_at': " + dt_repr, mbstr)
        self.assertIn("'updated_at': " + dt_repr, mbstr)

    def test_args_unused(self):
        mb = BaseModel(None)
        self.assertNotIn(None, mb.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        mb = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(mb.id, "345")
        self.assertEqual(mb.created_at, dt)
        self.assertEqual(mb.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        mb = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(mb.id, "345")
        self.assertEqual(mb.created_at, dt)
        self.assertEqual(mb.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testting Save method of the BaseModel super class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        mb = BaseModel()
        sleep(0.05)
        first_updated_at = mb.updated_at
        mb.save()
        self.assertLess(first_updated_at, mb.updated_at)

    def test_two_saves(self):
        mb = BaseModel()
        sleep(0.05)
        first_updated_at = mb.updated_at
        mb.save()
        second_updated_at = mb.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        mb.save()
        self.assertLess(second_updated_at, mb.updated_at)

    def test_save_with_arg(self):
        mb = BaseModel()
        with self.assertRaises(TypeError):
            mb.save(None)

    def test_save_updates_file(self):
        mb = BaseModel()
        mb.save()
        mbid = "BaseModel." + mb.id
        with open("file.json", "r") as f:
            self.assertIn(mbid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        mb = BaseModel()
        self.assertTrue(dict, type(mb.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        mb = BaseModel()
        self.assertIn("id", mb.to_dict())
        self.assertIn("created_at", mb.to_dict())
        self.assertIn("updated_at", mb.to_dict())
        self.assertIn("__class__", mb.to_dict())

    def test_to_dict_contains_added_attributes(self):
        mb = BaseModel()
        mb.name = "Holberton"
        mb.my_number = 98
        self.assertIn("name", mb.to_dict())
        self.assertIn("my_number", mb.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        mb = BaseModel()
        mb_dict = mb.to_dict()
        self.assertEqual(str, type(mb_dict["created_at"]))
        self.assertEqual(str, type(mb_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        mb = BaseModel()
        mb.id = "123456"
        mb.created_at = mb.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(mb.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        mb = BaseModel()
        self.assertNotEqual(mb.to_dict(), mb.__dict__)

    def test_to_dict_with_arg(self):
        mb = BaseModel()
        with self.assertRaises(TypeError):
            mb.to_dict(None)


if __name__ == "__main__":
    unittest.main()

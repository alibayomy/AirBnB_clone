#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        revw = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(revw))
        self.assertNotIn("place_id", revw.__dict__)

    def test_user_id_is_public_class_attribute(self):
        revw = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(revw))
        self.assertNotIn("user_id", revw.__dict__)

    def test_text_is_public_class_attribute(self):
        revw = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(revw))
        self.assertNotIn("text", revw.__dict__)

    def test_two_reviews_unique_ids(self):
        revw1 = Review()
        revw2 = Review()
        self.assertNotEqual(revw1.id, revw2.id)

    def test_two_reviews_different_created_at(self):
        revw1 = Review()
        sleep(0.05)
        revw2 = Review()
        self.assertLess(revw1.created_at, revw2.created_at)

    def test_two_reviews_different_updated_at(self):
        revw1 = Review()
        sleep(0.05)
        revw2 = Review()
        self.assertLess(revw1.updated_at, revw2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        revw = Review()
        revw.id = "123456"
        revw.created_at = revw.updated_at = dt
        revwstr = revw.__str__()
        self.assertIn("[Review] (123456)", revwstr)
        self.assertIn("'id': '123456'", revwstr)
        self.assertIn("'created_at': " + dt_repr, revwstr)
        self.assertIn("'updated_at': " + dt_repr, revwstr)

    def test_args_unused(self):
        revw = Review(None)
        self.assertNotIn(None, revw.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        revw = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(revw.id, "345")
        self.assertEqual(revw.created_at, dt)
        self.assertEqual(revw.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review
        inhirted class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

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
        revw = Review()
        sleep(0.05)
        first_updated_at = revw.updated_at
        revw.save()
        self.assertLess(first_updated_at, revw.updated_at)

    def test_two_saves(self):
        revw = Review()
        sleep(0.05)
        first_updated_at = revw.updated_at
        revw.save()
        second_updated_at = revw.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        revw.save()
        self.assertLess(second_updated_at, revw.updated_at)

    def test_save_with_arg(self):
        revw = Review()
        with self.assertRaises(TypeError):
            revw.save(None)

    def test_save_updates_file(self):
        revw = Review()
        revw.save()
        revwid = "Review." + revw.id
        with open("file.json", "r") as f:
            self.assertIn(revwid, f.read())


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review
        inhirted class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        revw = Review()
        self.assertIn("id", revw.to_dict())
        self.assertIn("created_at", revw.to_dict())
        self.assertIn("updated_at", revw.to_dict())
        self.assertIn("__class__", revw.to_dict())

    def test_to_dict_contains_added_attributes(self):
        revw = Review()
        revw.middle_name = "Holberton"
        revw.my_number = 98
        self.assertEqual("Holberton", revw.middle_name)
        self.assertIn("my_number", revw.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        revw = Review()
        revw_dict = revw.to_dict()
        self.assertEqual(str, type(revw_dict["id"]))
        self.assertEqual(str, type(revw_dict["created_at"]))
        self.assertEqual(str, type(revw_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        revw = Review()
        revw.id = "123456"
        revw.created_at = revw.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(revw.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        revw = Review()
        self.assertNotEqual(revw.to_dict(), revw.__dict__)

    def test_to_dict_with_arg(self):
        revw = Review()
        with self.assertRaises(TypeError):
            revw.to_dict(None)


if __name__ == "__main__":
    unittest.main()

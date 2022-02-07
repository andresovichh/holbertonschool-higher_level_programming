#!/usr/bin/python3
  
"""Unittest for the Base class"""
import json
import unittest
from models.base import Base
import pep8



"""
Tests for the Base CLASS
 """


class TestBase(unittest.TestCase):

    def test_documentation(self):
        """documentation"""

        self.assertTrue(len(Base.__doc__) > 0)
    
    def test_documentations(self):
        """check if method has doc"""

        self.assertTrue(len(Base.to_json_string.__doc__) > 0)

    def test_documentations1(self):
        """check if method has doc"""

        self.assertTrue(len(Base.save_to_file.__doc__) > 0)
    
    def test_documentations2(self):
        """check if method has doc"""

        self.assertTrue(len(Base.from_json_string.__doc__) > 0)
    
    def test_documentations3(self):
        """check if method has doc"""

        self.assertTrue(len(Base.create.__doc__) > 0)
    
    def test_documentations4(self):
        """check if method has doc"""

        self.assertTrue(len(Base.load_from_file.__doc__) > 0)    
    
    def test_documentation5(self):
        """documentation"""

        self.assertTrue(len(Base.__init__.__doc__) > 0)
    
    #1
    
    def test_usual_case(self):
        """ Basic test case with:
        negative id,
        large number, 
        assignment of id"""
        Base._Base__nb_objects = 0
        b1 = Base(10)
        self.assertEqual(b1.id, 10)
        b2 = Base()
        self.assertEqual(b2.id, 1)
        b3 = Base(1)
        self.assertEqual(b3.id, 1)
        b4 = Base()
        self.assertEqual(b4.id, 2)
        b5 = Base(500000)
        self.assertEqual(b5.id, 500000)
        b6 = Base()
        self.assertEqual(b6.id, 3)
        b7 = Base(500000)
        self.assertEqual(b7.id, 500000)
        b8 = Base(-90)
        self.assertEqual(b8.id, -90)
        b9 = Base()
        self.assertEqual(b9.id, 4)


    #2
    def test_noidprovided(self):
        # need to equal to 0 so overrides previous id
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)

    #3

    def test_nodatapassed(self):
        Base._Base__nb_objects = 0
        a1 = Base()
        a2 = Base()
        self.assertEqual(a2.id, 2)   



    def test_onlywithargs(self):
        """ test only with args"""
        Base._Base__nb_objects = 0

        j = Base(122)
        k = Base(-54)
        l = Base(25)
        self.assertEqual(j.id, 122)
        self.assertEqual(k.id, -54)
        self.assertEqual(l.id, 25)
    
    def test_onlywithargs1(self):
        """ passing a str"""
        Base._Base__nb_objects = 0

        j = Base("ok")
        self.assertEqual(j.id, 'ok')

    def test_onlywithargs2(self):
        """ passing three args"""
        Base._Base__nb_objects = 0

        messages = "TypeError: __init__() takes from 1 to 2 positional arguments but 3 were given"
        with self.assertRaises(TypeError) as err:

            j = Base(1, 2)
            self.assertEqual(messages, str(err.exception))
    
    def test_createaRectangle(self):
        """ Check they are two different objects"""

        from models.rectangle import Rectangle
        Base._Base__nb_objects
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertNotEqual(r1, r2)
         
    # def test_createaRectangle(self):
    #     """ Passing an empty dictionary"""

    #     from models.rectangle import Rectangle
    #     Base._Base__nb_objects


    #     errmssg = "AttributeError: 'dict' object has no attribute 'to_dictionary'"
    #     with self.assertRaises(AttributeError) as err:
    #         r1 = {}
    #         r1_dictionary = [r1.to_dictionary()]
    #         r2 = Rectangle.create(**r1_dictionary)
    #         self.assertEqual(errmssg, str(err.exception))
    
    
    # def test_to_json_str(self):
    #     """ to json string testing usual case"""
    #     from models.rectangle import Rectangle
    #     r1 = Rectangle(10, 7, 2, 8)
    #     dictionary = r1.to_dictionary()
    #     json_dictionary = Base.to_json_string([dictionary])
    #     str_totest = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
    #     to_jsn = (dict(str_totest))
    #     self.assertDictEqual(to_jsn, json_dictionary)


        # with self.assertRaises(TypeError) as i:
        #     Base.to_json_string()
        # self.assertEqual("to_json_string() missing 1 required positional " +
        #     "argument: 'list_dictionaries'", str(i.exception))



    # def test_string(self):
    #     #!/usr/bin/python3
    #     b1 = Base()
    #     self.assertEqual(b1.id, 1)
    #     b2 = Base()
    #     self.assertEqual(b2.id, 2)
    #     b3 = Base()
    #     self.assertEqual(b3.id, 3)
    #     b4 = Base()
    #     self.assertEqual(b4.id, 4)


""" 0-main """
from models.base import Base

# if __name__ == "__main__":

#     b1 = Base()
#     print(b1.id)

#     b2 = Base()
#     print(b2.id)

#     b3 = Base()
#     print(b3.id)

#     b4 = Base(12)
#     print(b4.id)

#     b5 = Base()
#     print(b5.id)


class TestCodeFormat(unittest.TestCase):
    def test_pep8_conformance(self):
        # """Test that we conform to PEP8."""
        # pep8style = pep8.StyleGuide(quiet=True)
        # result = pep8style.check_files(['base.py'])
        # print(result)
        # self.assertEqual(result.total_errors, 0,
        #                  "Found code style errors (and warnings).")
        # https://pep8.readthedocs.io/en/release-1.7.x/intro.html
        fchecker = pep8.Checker('models/base.py', show_source=True)
        file_errors = fchecker.check_all()

        print("Found %s errors (and warnings)" % file_errors)


if __name__ == "__main__":
    unittest.main()
import unittest
import circle, rectangle, square, triangle

class TestCircle(unittest.TestCase):
    
    def test_area_valid(self):
        self.assertAlmostEqual(circle.area(4), 50.24, places=1)
        self.assertAlmostEqual(circle.area(5), 78.539816, places=6)

    def test_perimeter_valid(self):
        self.assertAlmostEqual(circle.perimeter(4), 25.13274, places=5)
        self.assertAlmostEqual(circle.perimeter(5), 31.41592653589793, places=14)

    def test_area_type_error(self):
        with self.assertRaises(TypeError):
            circle.area("ark")

    def test_perimeter_type_error(self):
        with self.assertRaises(TypeError):
            circle.perimeter("ark")

    def test_area_value_error(self):
        with self.assertRaises(ValueError):
            circle.area(-1)

    def test_perimeter_value_error(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-2)


class TestRectangle(unittest.TestCase):
    
    def test_area_valid(self):
        self.assertEqual(rectangle.area(4, 5), 20)
        self.assertEqual(rectangle.area(6, 7), 42)

    def test_perimeter_valid(self):
        self.assertEqual(rectangle.perimeter(4, 5), 18)
        self.assertEqual(rectangle.perimeter(6, 7), 26)

    def test_area_type_error(self):
        with self.assertRaises(TypeError):
            rectangle.area("ark", 5)

    def test_perimeter_type_error(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(4, "ark")

    def test_area_value_error(self):
        with self.assertRaises(ValueError):
            rectangle.area(-4, 5)

    def test_perimeter_value_error(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-4, 5)


class TestSquare(unittest.TestCase):
    
    def test_area_valid(self):
        self.assertEqual(square.area(4), 16)
        self.assertEqual(square.area(5), 25)

    def test_perimeter_valid(self):
        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(6), 24)

    def test_area_type_error(self):
        with self.assertRaises(TypeError):
            square.area("ark")

    def test_perimeter_type_error(self):
        with self.assertRaises(TypeError):
            square.perimeter("ark")

    def test_area_value_error(self):
        with self.assertRaises(ValueError):
            square.area(-4)

    def test_perimeter_value_error(self):
        with self.assertRaises(ValueError):
            square.perimeter(-5)


class TestTriangle(unittest.TestCase):
    
    def test_area_valid(self):
        self.assertEqual(triangle.area(6, 7), 21)

    def test_perimeter_valid(self):
        self.assertEqual(triangle.perimeter(6, 7, 8), 21)

    def test_area_type_error(self):
        with self.assertRaises(TypeError):
            triangle.area("ark", 7)

    def test_perimeter_type_error(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(6, "ark", 8)

    def test_area_value_error(self):
        with self.assertRaises(ValueError):
            triangle.area(6, -7)

    def test_perimeter_value_error(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(6, -7, 8)


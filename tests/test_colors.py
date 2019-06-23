import unittest2
from six import iteritems, string_types


class TestControlAsHSV(unittest2.TestCase):
    def test_red(self):
        self.assertEqual(self.RED.as_hsv(), (0.0, 1, 1))

    def test_green(self):
        self.assertEqual(self.GREEN.as_hsv(), (0.3333333333333333, 1, 1))

    def test_blue(self):
        self.assertEqual(self.BLUE.as_hsv(), (0.6666666666666666, 1, 1))

    def test_mid(self):
        self.assertEqual(self.MID.as_hsv(), (0, 0, 0.5))

    def test_black(self):
        self.assertEqual(self.WHITE.as_hsv(), (0, 0, 1.0))

    def test_white(self):
        self.assertEqual(self.BLACK.as_hsv(), (0, 0, 0))


class TestControlAsHSV360(unittest2.TestCase):
    def test_red(self):
        self.assertEqual(self.RED.as_hsv_360(), (0.0, 1, 1))

    def test_green(self):
        self.assertEqual(self.GREEN.as_hsv_360(), (120, 1, 1))

    def test_blue(self):
        self.assertEqual(self.BLUE.as_hsv_360(), (240, 1, 1))

    def test_mid(self):
        self.assertEqual(self.MID.as_hsv_360(), (0, 0, 0.5))

    def test_black(self):
        self.assertEqual(self.WHITE.as_hsv_360(), (0, 0, 1.0))

    def test_white(self):
        self.assertEqual(self.BLACK.as_hsv_360(), (0, 0, 0))


class TestControlAsRGBNormalized(unittest2.TestCase):
    def test_red(self):
        self.assertEqual(self.RED.as_rgb_normalized(), (1, 0, 0))

    def test_green(self):
        self.assertEqual(self.GREEN.as_rgb_normalized(), (0, 1, 0))

    def test_blue(self):
        self.assertEqual(self.BLUE.as_rgb_normalized(), (0, 0, 1))

    def test_mid(self):
        self.assertEqual(self.MID.as_rgb_normalized(), (0.5, 0.5, 0.5))

    def test_black(self):
        self.assertEqual(self.WHITE.as_rgb_normalized(), (1.0, 1.0, 1.0))

    def test_white(self):
        self.assertEqual(self.BLACK.as_rgb_normalized(), (0, 0, 0))

import unittest

import utils


class SlugifyTests(unittest.TestCase):
    def test_my_slugify_symbols(self):
        self.assertEqual(utils.my_slugify("#*<foo$@.;!"), "foo")

    def test_my_slugify_spaces(self):
        self.assertEqual(utils.my_slugify("   foo bar "), "foo-bar")

    def test_my_slugify_mixed_use(self):
        self.assertEqual(utils.my_slugify("Foo? Bar! #123"), "foo-bar-123")


if __name__ == "__main__":
    unittest.main()

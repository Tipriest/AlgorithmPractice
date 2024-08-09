import unittest
# def showMsg(msg):
#     return "%s"%(msg)
# def do_divide(a, b):
#     return (a/b)
# def showTrue(flag):
#     return flag
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    def test_split(self):
        s = 'hello_world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
    # def testrun(self):
    #     self.assertEqual('OK', showMsg('OK'))
    #     self.assertNotEqual('OK', showMsg('NO'))
    #     self.assertTrue(do_divide(1,2))
    #     self.assertIs(showTrue(False), False)
    #     self.assertIs(int(do_divide(1,2)), 1)
if __name__ == '__main__':
    unittest.main()

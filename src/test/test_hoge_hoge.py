import unittest
import sys
sys.path.append('../main')
import hoge_hoge

class TestHogeHoge(unittest.TestCase):
    '''
    ../src/hoge_hogeモジュールをテスト
    '''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_(self):
        '''
        '''
        x_1 = hoge_hoge.return_num()
        x_2 = 2
        self.assertEqual(x_1, x_2)

if __name__ == '__main__':
    unittest.main()

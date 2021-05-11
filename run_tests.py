import cmdb_unittest

test_dir = './test_case'
suits = cmdb_unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    runner = cmdb_unittest.TextTestRunner()
    runner.run(suits)
# 119

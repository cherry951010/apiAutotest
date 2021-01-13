'''
入口
'''
import pytest

if __name__ == '__main__':
    pytest.main(['testcases','-v','--html=report/reports.html'])
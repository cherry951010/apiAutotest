'''
入口
'''
import pytest
import time

if __name__ == '__main__':
    current_data = time.strftime('%Y-%m-%d %H:%M:%S')
    pytest.main(['testcases','-v',f'--html=report/reports{current_data}.html'])
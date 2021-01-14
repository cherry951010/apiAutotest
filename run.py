'''
入口
'''
import pytest
import time


def run_all_cases():
    current_data = time.strftime('%Y-%m-%d %H:%M:%S')
    pytest.main(['testcases', '-v','-s', f'--html=report/reports{current_data}.html'])

if __name__ == '__main__':
    run_all_cases()
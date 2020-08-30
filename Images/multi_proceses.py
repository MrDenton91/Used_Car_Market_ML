import os
from multiprocessing import Pool

def run_process(processess):
        os.system('python {}'.format(processess))

if __name__ == '__main__':
    processess = ( 'split2.py', 'split3.py',  'split5.py', 'split10.py', 'split12.py', 'split14.py', 'split17.py', 'split18.py', 'split19.py' )


    pool = Pool(processes = 20)
    pool.map(run_process, processess)
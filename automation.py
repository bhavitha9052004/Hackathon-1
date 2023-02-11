import joblib
import logging
from joblib import Parallel, delayed
from joblib import parallel_backend
import encrypt_decrypt as ed
import file_operations as fp

logging.basicConfig(filename="logging.log",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

iterations = input("\nPlease enter the number of iterations:")
with parallel_backend('threading', n_jobs=2):
   Parallel()(delayed(fp.startautomation)(iterations, i) for i in range(10))


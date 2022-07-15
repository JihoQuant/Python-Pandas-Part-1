import numpy as np
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell

def init() -> None:
    InteractiveShell.ast_node_interactivity = "all"
    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    pd.options.display.max_columns = None
    np.random.seed(1)

CSV_BASE_DIR = 'part1/inflearn_pandas_part1_material/my_data/'

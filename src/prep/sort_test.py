import pandas as pd

from src.common.my_data import Data

data = Data()
#
# sort_data = pd.read_table(data.input.test_agg).sort_values('USRID')
# # print(sort_data)
# sort_data.to_csv(data.output.sorted_test_agg, sep='\t', index=None)
#

# sort_data = pd.read_table(data.input.test_log).sort_values('USRID')
# # print(sort_data)
# sort_data.to_csv(data.output.sorted_test_log, sep='\t', index=None)


sort_data = pd.read_table(data.output.no_log_usr_test).sort_values('USRID')
# print(sort_data)
sort_data.to_csv(data.output.no_log_usr_test, sep='\t', index=None)

from Lda import Lda
from PreProcess import PreProcess

data = PreProcess("/Users/eirinimilaiou/Documents/ucl/CACI/test_data/","Example_Data.xlsx").initialProcess()
Lda(data).model_results(5,"mallet")
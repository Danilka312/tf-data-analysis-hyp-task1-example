import pandas as pdimport numpy as np
from statsmodels.stats.proportion import proportions_ztestfrom scipy. special import logsumexp

chat_id = 6122152745
def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
    tmp = ((x_success+y_success) * y_cnt)/(x_cnt+y_cnt)    
    sqr = (y_success - tmp)**2/tmp
    if sqr < 6.63:        
      return False
    else:        
      return True

# --------------------------------------------------------------------------------


#                          功能：  加载配置文件

# 加载设置好的配置文件
# 加载好后作为网络的超参数
# 使用import加载配置文件即可
# 如果你喜欢也可以自己写成*.cfg *.txt *.yaml


# ---------------------------------------------------------------------------------
# 在此处import你自己的配置参数.py文件
from config import config_example

# ---------------------------------------------------------------------------------

cfg = config_example.get_cfg()
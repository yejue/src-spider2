class SimpleArgvSplit:
    """简易参数分解工具类
     - 初始化给定外部传参列表，传参函数映射表
     - 分解出实际所需要的键值对
    """

    def __init__(self, argv_list: list, key_dict: dict):
        self.argv_list = argv_list
        self.key_dict = key_dict

    def split(self):
        """分解函数"""
        res = {}

        for key in self.key_dict.keys():
            if key in self.argv_list[1:]:
                try:
                    index = self.argv_list.index(key)
                    value = self.argv_list[index+1]
                    if self.key_dict[key]["type"] == "string":
                        res.update({self.key_dict[key]["name"]: value})
                    elif self.key_dict[key]["type"] == "int":
                        value = int(value)
                        res.update({self.key_dict[key]["name"]: value})
                    else:
                        if value.isdigit():  # 布尔值0, 1 的字符处理
                            value = int(value)
                        res.update({self.key_dict[key]["name"]: bool(value)})
                except IndexError as e:
                    raise Exception(f"ParamsError: 参数输入错误 {e}")
        return res

# coding=utf-8

class ListStack:

    def __init__(self):
        self._data = [1,2]

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0
    
    def l_pop(self): # 从栈顶取数据
        if self.is_empty():
            return None
        return self._data.pop(0)
    
    def r_pop(self): # 从栈底取数据
        if self.is_empty():
            return None
        return self._data.pop(-1)
    
    def l_push(self, e): #压入栈底
        self._data.append(e)
        return self._data
    
    def r_push(self, e):  # 压入栈顶
        self._data.insert(0,e)
        return self._data

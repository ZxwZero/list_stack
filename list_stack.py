# coding=utf-8

# class ListStack:

#     def __init__(self):
#         self._data = [1,2]

#     def __len__(self):
#         return len(self._data)

#     def is_empty(self):
#         return len(self._data) == 0
    
#     def l_pop(self): # 从栈顶取数据
#         if self.is_empty():
#             return None
#         return self._data.pop(0)
    
#     def r_pop(self): # 从栈底取数据
#         if self.is_empty():
#             return None
#         return self._data.pop(-1)
    
#     def l_push(self, e): #压入栈底
#         self._data.append(e)
#         return self._data
    
#     def r_push(self, e):  # 压入栈顶
#         self._data.insert(0,e)
#         return self._data


class RightStack():
    def __init__(st,size):
        st.stack=[]
        st.size=size
        st.top=-1

    def empty(st):
        if st.top==-1:
            return True
        else:
            return False

    def full(st):
        if st.top==st.size:
            return True
        else:
            return False

    def r_push(st,data):
        if st.full():
            print "RightStack is full"
        else:
            st.stack.append(data)
            st.top=st.top+1

    def r_pop(st):
        if st.empty():
            print "RightStack is empty"
        else:
            st.top=st.top-1


class LeftStack():
    def __init__(st,size):
        st.stack=[]
        st.size=size
        st.top=-1

    def empty(st):
        if st.top==-1:
            return True
        else:
            return False

    def full(st):
        if st.top==st.size:
            return True
        else:
            return False

    def l_push(st,data):
        if st.full():
            print "LeftStack is full"
        else:
            st.stack.insert(0, data)
            st.top=st.top+1

    def l_pop(st):
        if st.empty():
            print "LeftStack is empty"
        else:
            for i in xrange(1, len(st.stack)):
                st.stack[i-1] = st.stack[i]
            st.top=st.top-1

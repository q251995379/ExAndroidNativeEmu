from ..java_class_def import JavaClassDef
from ..java_field_def import JavaFieldDef
from ..java_method_def import java_method_def, JavaMethodDef

class Array(metaclass=JavaClassDef, jvm_name='java/lang/reflect/Array'):

    def __init__(self, pyitems):
        self.__pyitems = pyitems
    #

    def get_py_items(self):
        return self.__pyitems
    #

    def __len__(self):
        return len(self.__pyitems)
    #

    def __getitem__(self,index):
        return self.__pyitems[index]
    #

    def __setitem__(self,index,value):
        self.__pyitems[index] = value
    #

    def __repr__(self):
        return "JavaArray(%r)"%self.get_py_items()
    #

    @staticmethod
    @java_method_def(name='set', signature='(Ljava/lang/Object;I)Ljava/lang/Object;', native=False)
    def set(emu, obj, index):
        raise NotImplementedError()
    #
    
#
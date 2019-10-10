# -*- coding: utf-8 -*-

def SingletonDecorator(cls):
    """
    Implement singleton through decorator.
    Usage:
        @SingletonDecorator
        class A:
            pass
    """
    class Single(cls):
        __doc__ = cls.__doc__
        _initialized = False
        _instance = None
        
        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super(Single, cls).__new__(cls, *args, **kwargs)
            return cls._instance
                       
        def __init__(self, *args, **kwargs):
            if self._initialized:
                return
            super(Single, self).__init__(*args, **kwargs)
            self.__class__._initialized = True
    return Single

class SingletonMeta(type):   
    """
    Implement singleton through metaclass.
    Usage:
        class A(metaclass=SingletonMeta):
            pass
    """
    
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class SingletonMeta2(type):
    """
    Implement singleton through metaclass with global table
    Usage:
        class A(metaclass=SingletonMeta2):
            pass
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta2, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# =============================================================================
# A few examples
# =============================================================================
if __name__ == "__main__":
    
    @SingletonDecorator
    class Decorated:
        pass
    decorated = Decorated()
    print(decorated)
    print("is instance of Decorated : " + str(isinstance(decorated, Decorated)))
    
    class WithMetaclass(metaclass=SingletonMeta):
        pass
    withMetaclass = WithMetaclass()
    print(withMetaclass)
    print("is instance of WithMetaclass : " + str(isinstance(withMetaclass, WithMetaclass)))
    
    class WithMetaclass2(metaclass=SingletonMeta2):
        pass
    withMetaclass2 = WithMetaclass2()
    print(withMetaclass2)
    print("is instance of WithMetaclass2 : " + str(isinstance(withMetaclass2, WithMetaclass2)))
    print("is instance of WithMetaclass : " + str(isinstance(withMetaclass2, WithMetaclass)))
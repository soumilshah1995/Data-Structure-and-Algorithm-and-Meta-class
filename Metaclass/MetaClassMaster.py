
try:
    import functools
    import datetime
    import os
    import sys
    import logging
    from abc import  ABC, ABCMeta,abstractmethod
except Exception as e:
    print("Some Modules are Missing {}".format(e))


class MetaClass(type):

    """ Meta class """

    _instance = {}

    def __call__(cls, *args, **kwargs):

        """ Implementing Singleton Design Pattern  """
        print("**kwargs", kwargs)

        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]

    def __init__(cls, name, base, attr):

        """ Defining Your Own Rules  """

        if cls.__name__[0].isupper():

            """ Create class only if First Letter is Capital    """

            for k, v in attr.items():
                if hasattr(v, '__call__'):

                    if v.__name__[0] == '_' or v.__name__[0].islower():

                        """  check name function starts with _ or lower case  """

                        if v.__doc__ is None:

                            """  Check is User has provided Documentation """

                            raise ValueError("Make sure to Provide Documentation check {}".format(v.__name__))
                        else:

                            """ if function has Doccumentation pass """

                            pass
                    else:

                        """ function name starts with upper case throw error  """

                        raise ValueError("Function should start with Lower case :{}".format(v.__name__))
        else:
            raise ValueError("Class Name  should start with Capital Letter :{} ".format(cls.__name__[0]))


class Test(metaclass=MetaClass):

    def __init__(self):
        """ Constructor """
        super(Test, self).__init__()

    def method(self):

        """ Method """

        print("Hello World ")


if __name__ == "__main__":
    obj = Test()
    print(obj.method())



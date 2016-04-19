from .pp import pp_class


class ImmutableBase(type):
    def __setattr__(cls, name, value):
        raise AttributeError("Cannot alter '{}' class".format(pp_class(cls)))


class ImmutableClass(object, metaclass=ImmutableBase):
    _frozen = False

    def __setattr__(self, name, value):
        if self._frozen:
            raise AttributeError(
                "Cannot alter instance of '{}'".format(pp_class(self))
            )
        else:
            super(ImmutableClass, self).__setattr__(name, value)
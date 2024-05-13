class GUITracker:

    # the dictionary holding gui components
    dic_components = {}

    @classmethod
    def set(cls, name, component):
        """adds the pair (name, component) to the global dictionary keeping track of all GUI components"""
        if name in cls.dic_components:
            raise Exception("The key name already exist in the dictionary")
        else:
            cls.dic_components[name] = component

    @classmethod
    def get(cls, name):
        """returns the GUI object with the given name"""
        return cls.dic_components[name]
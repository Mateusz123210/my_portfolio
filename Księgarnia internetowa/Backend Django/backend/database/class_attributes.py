

class ClassAttributes:
    @staticmethod
    def get_class_attributes(cl):
        fields = cl.__doc__
        fields = fields[6:]
        fields = fields[:-1]
        return list(fields.split(", "))
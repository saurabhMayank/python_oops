"""

Instance Method
Instance methods are regular methods that can modify the object instance's state. They take self as the first parameter.

Static Method
Static methods do not modify the object's state or class state. They don't take self or cls as a parameter. 
They are utility functions related to the class but not dependent on class or instance state.
Memory for static methods is allocated once per class, regardless of the number of instances

Class Method
Class methods modify the class state and take cls as the first parameter. They can be called on the class itself.
Memory for static methods is allocated once per class, regardless of the number of instances

"""

class Schema:
    def __init__(self, schema_name):
        self.schema_name = schema_name

    def validate(self, data):
        # Instance method to validate data against the schema
        pass


class DataValidator:
    @staticmethod
    def is_valid_format(data):
        # Static method to check if data format is valid
        return isinstance(data, dict)



class SchemaTracker:
    schema_count = 0

    def __init__(self, schema_name):
        self.schema_name = schema_name
        SchemaTracker.schema_count += 1

    @classmethod
    def get_schema_count(cls):
        return cls.schema_count

class DataField:
    def __init__(self, offset):
        self.offset = offset

    def __get__(self, instance, owner):
        return instance.data[self.offset]


class StringField(DataField):
    def __get__(self, instance, owner):
        raw_data = super().__get__(instance, owner)
        return raw_data.decode('utf-8')


class IntField(DataField):
    def __get__(self, instance, owner):
        raw_data = super().__get__(instance, owner)
        return int(raw_data.decode('utf-8'))

from marshmallow import Schema, fields

class PacketSchema(Schema):
    id = fields.Int()
    type = fields.Str()
    timestamp = fields.DateTime()
    client_id = fields.Str()


class DataPacketSchema(Schema):
    id = fields.Int()
    data_packet = fields.Nested(PacketSchema)
    data = fields.Str()

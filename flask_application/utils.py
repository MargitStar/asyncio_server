from marshmallow import Schema, fields

class PacketShema(Schema):
    id = fields.Int()
    packet = fields.Str()
    timestamp = fields.DateTime()
    client_id = fields.Str()


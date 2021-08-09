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


class MultipartPacketScema(Schema):
    id = fields.Int()
    start_packet_id = fields.Int()
    end_packet_id = fields.Int()


class MultipartDataSchema(Schema):
    id = fields.Int()
    data = fields.Str()
    idx = fields.Int()
    packet = fields.Nested(PacketSchema)
    mp_packet = fields.Nested(MultipartPacketScema)
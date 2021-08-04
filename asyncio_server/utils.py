async def read_data(reader):
    data = await reader.read()
    return data

def parse_connection_number(data):
    connection_number = int(convert_data_to_string(data[0:4]))
    data_type = convert_data_to_string(data[4:7])
    return connection_number, data_type

def get_packets_amount(data):
    return int(convert_data_to_string(data[7:11]))

def get_dtp_data(data):
    return data[7:]

def convert_data_to_string(connection):
    return connection.decode('utf-8')

def convert_data_to_int(number):
    return int.from_bytes(number)


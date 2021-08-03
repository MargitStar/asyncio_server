async def read_data(reader):
    connection = await reader.readline()
    data = await reader.readuntil(b'\xdd\xcc\xbb\xaa')
    data_type = await reader.readline()
    return connection, data, data_type

def convert_data_to_string(connection):
    connection = connection.strip()
    return connection.decode('utf-8')  
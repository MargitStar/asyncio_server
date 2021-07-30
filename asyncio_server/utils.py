async def read_data(reader):
    connection = await reader.readline()
    data = await reader.readuntil(b'\xdd\xcc\xbb\xaa')
    return connection, data 

def get_connection_number(connection):
    connection = connection.strip()
    return connection.decode('utf-8')  
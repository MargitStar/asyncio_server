from asyncio_client.utils import convert_str_to_bytes


async def read_data_info(reader):
    connection = await reader.readline()
    data_type = await reader.readline()
    return connection, data_type

async def read_data(reader, data_type):
    if data_type == 'DP':
        data = await reader.readuntil(b'\xdd\xcc\xbb\xaa')
    elif data_type == 'MPS':
        data = await reader.readuntil(b'MPS')
        remove_chars_str(data)
    elif data_type == 'MPB':
        data = await reader.readuntil(b'MPB')
        remove_chars_str(data)
    elif data_type == 'MPE':
        data = await reader.readuntil(b'MPE')
    return data


def convert_data_to_string(connection):
    connection = connection.strip()
    return connection.decode('utf-8')

def remove_chars_str(data):
    return data[:-3] 

def convert_mp_start_data(data):
    str_data = convert_str_to_bytes(data)
    return remove_chars_str(str_data)


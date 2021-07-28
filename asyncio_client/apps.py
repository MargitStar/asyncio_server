from client import tcp_echo_client
from config import read_config

async def main():
    config = read_config('config.json')
    await tcp_echo_client(config['port'], config['host'])
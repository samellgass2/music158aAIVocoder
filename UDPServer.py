# python-osc docs: https://python-osc.readthedocs.io/en/latest/
# pypi page: https://pypi.org/project/python-osc/

import argparse

from pythonosc import udp_client
from pythonosc import dispatcher
from pythonosc import osc_server


def print_volume_handler(unused_addr, args, volume):
    print("[{0}] ~ {1}".format(args[0], volume))


def print_compute_handler(unused_addr, args, volume):
    try:
        print("[{0}] ~ {1}".format(args[0], args[1](volume)))
    except ValueError:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--RecieveIP",
                        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--ReceivePort",
                        type=int, default=5005, help="The port to listen on")
    parser.add_argument("--SendPort",
                        type=int, default=5006, help="The port to send to")
    parser.add_argument("--SendIP",
                        default="127.0.0.1", help="The ip to send to")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/filter", print)
    dispatcher.map("/volume", print_volume_handler, "Volume")

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

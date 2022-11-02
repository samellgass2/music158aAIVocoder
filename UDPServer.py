# python-osc docs: https://python-osc.readthedocs.io/en/latest/
# pypi page: https://pypi.org/project/python-osc/

import argparse

from pythonosc import udp_client
from pythonosc import dispatcher
from pythonosc import osc_server

from harmonizer import *

#TODO: Replace


def print_volume_handler(unused_addr, args, volume):
    print("[{0}] ~ {1}".format(args[0], volume))

#TODO: Replace


def print_compute_handler(unused_addr, args, volume):
    try:
        print("[{0}] ~ {1}".format(args[0], args[1](volume)))
    except ValueError:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--recieveIP",
                        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--receivePort",
                        type=int, default=5005, help="The port to listen on")
    parser.add_argument("--sendPort",
                        type=int, default=5006, help="The port to send to")
    parser.add_argument("--sendIP", default="127.0.0.1",
                        help="The ip to send to")
    parser.add_argument("--key", default=0, help="They key to use")
    parser.add_argument("--voices", default=4, help='The number of voices')
    args = parser.parse_args()

    # UDP Server Stuff ----------------------------------------------

    # Create the dispatcher. This is where we bind functions and their OSC variables / addresses.
    # TODO: Change below.We probably map some sort of 'change' to the main function here.
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/filter", print)
    dispatcher.map("/volume", print_volume_handler, "Volume")

    # Start the UDP server with the dispatcher
    server = osc_server.ThreadingOSCUDPServer(
        (args.receiveIP, args.receivePort), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()

    # Create the client to send OSC info back to max.
    global client
    client = udp_client.SimpleUDPClient(args.sendIP, args.sendPort)

    # Create the harmonizer
    global majorHarmonizer
    majorHarmonizer = majorCounterPointHarmonizer(key=args.key, voices=args.voices)
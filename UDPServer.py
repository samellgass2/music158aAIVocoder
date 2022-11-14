# python-osc docs: https://python-osc.readthedocs.io/en/latest/
# pypi page: https://pypi.org/project/python-osc/


# Voices
import argparse

from pythonosc import udp_client
from pythonosc import dispatcher
from pythonosc import osc_server

from harmonizer import *

def returnNextChord(unused_addr, args):
    try:
        print(f'Note received!: {args}')
        nextchord = majorHarmonizer.harmonize(args)
        print(f'Current Chord: {majorHarmonizer.currchord}')
        print(f'Next Chord: {nextchord}')
        client.send_message('/chordList', nextchord)
    except ValueError:
        print('Value Error')
        print('Args:', args)
        print('Unused Addresses', unused_addr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--receiveIP",
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


    # Create the harmonizer
    # TODO: get UDP packet of key & voices (for now, just read from CLI)

    global majorHarmonizer
    majorHarmonizer = majorCounterPointHarmonizer(voices=args.voices, key=args.key)

    # Create the client to send OSC info back to max.
    global client
    client = udp_client.SimpleUDPClient(args.sendIP, args.sendPort)

    # UDP Server Stuff ----------------------------------------------

    # Create the dispatcher. This is where we bind functions and their OSC variables / addresses.
    # TODO: Change below.We probably map some sort of 'change' to the main function here.
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map('/midiNoteIn', returnNextChord)

    # Start the UDP server with the dispatcher
    server = osc_server.ThreadingOSCUDPServer(
        (args.receiveIP, args.receivePort), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
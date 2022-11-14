# python-osc docs: https://python-osc.readthedocs.io/en/latest/
# pypi page: https://pypi.org/project/python-osc/


import argparse

from pythonosc import udp_client
from pythonosc import dispatcher
from pythonosc import osc_server

from harmonizer import *

def returnNextChord(unused_addr, args):
    try:
        print(type(Harmonizer))
        print(f'Note received!: {args}')
        nextchord = Harmonizer.harmonize(args)
        print(f'Current Chord: {Harmonizer.currchord}')
        print(f'Next Chord: {nextchord}')
        client.send_message('/chordList', nextchord)
    except ValueError:
        print('Value Error')
        print('Args:', args)
        print('Unused Addresses', unused_addr)

def editNumVoices(unused_addr, args):
    try:
        global numVoices
        if args == numVoices:
            return
        print(f'New number of voices received: {args}')
        numVoices = args
        createHarmonizer()
    except ValueError:
        print('Value Error')
        print('Args:', args)
        print('Unused Addresses', unused_addr)

def editKey(unused_addr, args):
    try:
        global key
        if args == key:
            return
        print(f'New key received: {args}')
        key = args
        createHarmonizer()
    except ValueError:
        print('Value Error')
        print('Args:', args)
        print('Unused Addresses', unused_addr)

def editHarmonizerType(unused_addr, args):
    try:
        global harmonizerType
        if args == harmonizerType:
            return
        print(f'New Harmonizer Type received: {args}')
        harmonizerType = args
        createHarmonizer()
    except ValueError:
        print('Value Error')
        print('Args:', args)
        print('Unused Addresses', unused_addr)

def createHarmonizer():
    global Harmonizer
    global numVoices
    global key
    if harmonizerType == 1:
        Harmonizer = majorCounterPointHarmonizer(numVoices, key)
    elif harmonizerType == 2:
        Harmonizer = minorCounterPointHarmonizer(numVoices, key)
    elif harmonizerType == 3:
        Harmonizer = powerChordHarmonizer(numVoices, key)
    else:
        raise RuntimeError('Wrong type of Harmonizer submitted!')

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

    global numVoices
    numVoices = args.voices

    global harmonizerType
    harmonizerType = 0

    global key
    key = args.key

    global majorHarmonizer
    Harmonizer = majorCounterPointHarmonizer(voices=args.voices, key=args.key)

    # Create the client to send OSC info back to max.
    global client
    client = udp_client.SimpleUDPClient(args.sendIP, args.sendPort)

    # UDP Server Stuff ----------------------------------------------

    # Create the dispatcher. This is where we bind functions and their OSC variables / addresses.
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map('/midiNoteIn', returnNextChord)
    dispatcher.map('/voices', editNumVoices)
    dispatcher.map('/h', editHarmonizerType)
    dispatcher.map('/key', editKey)


    # Start the UDP server with the dispatcher
    server = osc_server.ThreadingOSCUDPServer(
        (args.receiveIP, args.receivePort), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
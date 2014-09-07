"""
"""

from funcy.seqs import imap, first
from evdev import InputDevice, list_devices, resolve_ecodes

def look_up(ident, config):
    device = InputDevice(ident)

    if not config:
        # TODO get config based on device
        pass

    mapping = lambda x: (x, first(resolve_ecodes({x.type: [x.code]})))

    return mapping, device

def event_stream(ident, config=None):
    mapping, device = look_up(ident, config)
    return imap(mapping, device.read_loop())

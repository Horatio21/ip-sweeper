import argparse
import ipaddress
import pythonping
import ifaddr


def sweep_network(args):
    ip_interface = ipaddress.IPv4Interface(args.ip + "/" + args.netmask)
    for ip in ip_interface.network:
        r = str(pythonping.ping(str(ip), count=1, timeout=args.timeout))
        if "Reply" in r:
            tokens = r.split(" ")
            print(tokens[2].strip(","))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This script sweeps ips, by pinging everything in a given network"
    )
    parser.add_argument(
        "ip", nargs="?",
        help="a network ip, or a host ip (default: this device's network will be swept)",
        default=ifaddr.get_adapters()[0].ips[-1].ip
    )
    parser.add_argument(
        "netmask", nargs="?",
        help="the netmask for the ip provided (default: 255.255.255.0)",
        default="255.255.255.0"
    )
    parser.add_argument(
        "-t", "--timeout", nargs="?",
        help="how much to wait for a response from ping, in seconds (default = 0.5)",
        default="0.5", type=float
    )

    args = parser.parse_args()
    sweep_network(args)

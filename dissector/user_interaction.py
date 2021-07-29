from argparse import ArgumentParser, RawTextHelpFormatter


def print_logo() -> None:
    """
    Print the Dissector logo
    Returns:
        None
    """
    print('''
    ____  _                     __            
   / __ \(_)____________  _____/ /_____  _____
  / / / / / ___/ ___/ _ \/ ___/ __/ __ \/ ___/
 / /_/ / (__  |__  )  __/ /__/ /_/ /_/ / /    
/_____/_/____/____/\___/\___/\__/\____/_/     
''')


def get_argument_parser() -> ArgumentParser:
    """
    Get the configured command line argument parser
    Returns:
        ArgumentParser
    """
    parser = ArgumentParser(prog='Dissector', usage='%(prog)s [options]',
                            epilog="Example: ./%(prog)s -f ./pcap_samples/sample1.pcap --summary --upload ",
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument('-f', '--filename', nargs='+', help="Traffic capture file(s) (pcap / flows)")
    parser.add_argument("--version", help="Show application version and exit", action="store_true")
    parser.add_argument("-v", "--verbose", help="Show info log statements", action="store_true")
    parser.add_argument("-d", "--debug", help="Show debug log statements", action="store_true")
    parser.add_argument("-q", "--quiet", help="Do not animate loading", action="store_true")
    parser.add_argument("--dbstatus", help="Check availability of DDoSDB instances", action="store_true")
    parser.add_argument("-s", "--summary", help="Present fingerprint evaluation summary", action="store_true")
    parser.add_argument("-u", "--upload", help="Upload to the first or selected DDoSDB instance", action="store_true")
    parser.add_argument("--log", default='dissector.log', nargs='?', help="Log filename. Default ./dissector.log")
    parser.add_argument("--fingerprint_dir", default='fingerprints', nargs='?',
                        help="Fingerprint storage directory. Default ./fingerprints")
    parser.add_argument("--dbconfig", default='ddosdb.conf', nargs='?',
                        help="Configuration File. Default ./ddosdb.conf")
    parser.add_argument("--host", help="DDoSDB host URL")
    parser.add_argument("--user", help="DDoSDB username")
    parser.add_argument("--passwd", help="DDoSDB password")
    parser.add_argument("-n", "--noverify",
                        help="disable verification of the host certificate (for self-signed certificates)",
                        action="store_true")
    # parser.add_argument("-g", "--graph",  # FIXME
    #                     help="build dot file (graphviz). It can be used to plot a visual representation\n of the "
    #                          "attack using the tool graphviz. When this option is set, youn will\n received "
    #                          "information how to convert the generate file (.dot) to image (.png).",
    #                     action="store_true")

    return parser
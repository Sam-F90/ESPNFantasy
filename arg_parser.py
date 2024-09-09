import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Process arguments")
    parser.add_argument("-y", "--year", help="Input Year", required=True)
    parser.add_argument("-u", "--upload", action="store_true",help="Update html with data?")
    parser.add_argument("-l", "--leagueid", help="Input League ID", required=True)
    parser.add_argument("-e", "--espn_s2", help="Input League ID", required=True)
    parser.add_argument("-s", "--swid", help="Input SWID", required=True)


    group = parser.add_mutually_exclusive_group()
    group.add_argument("-w", "--week", help="Input Week")
    group.add_argument("-r", "--range", nargs=2, help="Range")

    return parser.parse_args()

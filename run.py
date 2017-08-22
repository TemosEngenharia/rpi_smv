import os
import argparse

import app

parser = argparse.ArgumentParser(description='Start radar daemon.',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
opr_group = parser.add_mutually_exclusive_group()
parser.add_argument('--config',
                    default='/etc/radar/config.py',
                    help='the full path to config file')
opr_group.add_argument('-D', '--dev',
                       action='store_true',
                       help='used to operate on develop env')
opr_group.add_argument('-Q', '--qa',
                       action='store_true',
                       help='used to operate on quality assurance env')
opr_group.add_argument('-P', '--prod',
                       action='store_true',
                       help='used to operate on production env')
parser.add_argument('--addr',
                    default='127.0.0.1',
                    help='ip address to bind')
parser.add_argument('--port',
                    type=int,
                    default=5000,
                    help='TCP port to bind')
args = parser.parse_args()

if args.dev:
    os.environ["RADAR_CONFIG"] = '/etc/radar/dev_config.py'
    print('Develop')
    print(os.environ["RADAR_CONFIG"])
elif args.qa:
    os.environ["RADAR_CONFIG"] = '/etc/radar/qa_config.py'
    print('Quality and Assurance')
    print(os.environ["RADAR_CONFIG"])
elif args.prod:
    os.environ["RADAR_CONFIG"] = '/etc/radar/config.py'
    print('Production')
    print(os.environ["RADAR_CONFIG"])
else:
    os.environ["RADAR_CONFIG"] = '/etc/radar/config.py'
    print('Production')
    print(os.environ["RADAR_CONFIG"])

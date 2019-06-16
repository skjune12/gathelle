#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import datetime
import getpass
import os
import telnetlib

import yaml


def main():
    parser = argparse.ArgumentParser(description="gathelle fetches junos configuration files via telnet.")
    parser.add_argument("-f",
            "--file",
            help="specity the configuration file",
            default="./config.yml")
    parser.add_argument("-o",
            "--out",
            help="specify the directory storing the output",
            default="./result")
    args = parser.parse_args()

    if not os.path.exists(args.out):
        os.mkdir(args.out)

    # loading config.yml
    with open(args.file, "r") as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)

    for i in config:
        password = getpass.getpass(prompt="Password for user {0}: ".format(i["username"]))

        for host in i["hosts"]:
            configuration = get_configuration(i["username"], password, host)
            with open("{0}/{1}.conf".format(args.out, host["hostname"]), "w") as f:
                f.write(configuration)


def get_configuration(username, password, host):
    # setup telnet client
    tn = telnetlib.Telnet(host["address"])

    tn.read_until(b"login:")
    tn.write(username.encode("ascii") + b"\n")
    
    if password:
        tn.read_until(b"Password:")
        tn.write(password.encode("ascii") + b"\n")

    if host["set"] == True:
        tn.write(b"show configuration | display set | no-more\n")
        tn.write(b"quit\n")

    elif host["set"] == False:
        tn.write(b"show configuration | no-more\n")
        tn.write(b"quit\n")

    configuration = tn.read_all().decode("ascii")

    return configuration


if __name__ == "__main__":
    main()


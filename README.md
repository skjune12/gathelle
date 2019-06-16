# gathelle

gathelle is a command line tool that gathers junos configuration via telnet.

## Usage

```
$ python3 main.py -h
usage: main.py [-h] [-f FILE] [-o OUT]

gathelle fetches junos configuration files via telnet.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  specity the configuration file
  -o OUT, --out OUT     specify the directory storing the output
```

## Configuration

Here is the example of the configuration file.
To run this script, you need to specify the configuration in `config.yml` for fitting the script to your environment.

```
- username: admin
  hosts:
  - hostname: rt1.myhome.net
    address: 192.168.0.1
    set: true
  - hostname: sw1.myhome.net
    address: 192.168.0.2
    set: false
```

- `username` (string): specify the username you login via telnet. The script asks password per username.
- `hosts` (string): the script tries to login the items from top to below under the `hosts`.
    - `hostname` (string): enter the hostname. this is used by saving the configuration file. for example when you specify hostname `rt1.myhome.net`, the script saves its configuration file by `rt1.myhome.net.conf`.
    - `address` (string): specify the IPv4 or IPv6 address of the target host.
    - `set` (bool): if you specify this field `true`, the script saves the configuration by `display set`. otherwise, the script saves the configuration by hierarchical format.

## Author

Kohei Suzuki ([https://github.com/skjune12](@skjune12))

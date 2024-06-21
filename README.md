# GeoIP2Fast v1.2.2

GeoIP2Fast is the fastest GeoIP2 country/city/asn lookup library. A search takes less than 0.00003 seconds. It has its own data file updated with Maxmind-Geolite2-CSV, supports IPv4 and IPv6, works on Python3, Pypy3 and is Pure Python!

With it´s own datafile (geoip2fast.dat.gz), can be loaded into memory in ~0.07 seconds and has a small footprint for all data, so you don´t need to make requests to any webservices or connect to an external database. And it works on Linux, Windows and MacOS!

And now you can download .dat.gz from your own application or via the command line. See more at [Update your database automatically](#automatic-update-of-datgz-files)

GeoIP2Fast returns ASN NAME, COUNTRY ISO CODE, COUNTRY NAME, CITY NAME/STATE/DISTRICT and CIDR. There is no external dependencies, you just need the ```geoip2fast.py``` file and the desired data file ```.dat.gz```. The lookup speed is the same for any data file. 

### Country and ASN databases with IPv4 and IPv6

| Download Content | File Name | File Size | Load Time | RAM Footprint |
| ---------- | :---------: | ---------: | --------: | ---------: |
| [Country IPv4](https://github.com/rabuchaim/geoip2fast/releases/latest/download/geoip2fast.dat.gz) | ```geoip2fast.dat.gz``` | 1.2 MiB | ~0.04 sec | ~22.0 MiB |
| [Country IPv4+IPv6](https://github.com/rabuchaim/geoip2fast/releases/latest/download/geoip2fast-ipv6.dat.gz)  | ```geoip2fast-ipv6.dat.gz``` | 1.8 MiB | ~0.07 sec | ~41.0 MiB |
| [Country+ASN IPv4](https://github.com/rabuchaim/geoip2fast/releases/latest/download/geoip2fast-asn.dat.gz)  | ```geoip2fast-asn.dat.gz```  | 2.3 MiB | ~0.08 sec | ~40.0 MiB |
| [Country+ASN IPv4+IPv6](https://github.com/rabuchaim/geoip2fast/releases/latest/download/geoip2fast-asn-ipv6.dat.gz)  | ```geoip2fast-asn-ipv6.dat.gz``` | 3.1 MiB    | ~0.15 sec    | ~97.0 MiB    |

### City and ASN databases with IPv4 and IPv6

City databases are not included in the pip installation package, if you want to:
- download them manually from [DAT Files LATEST Release](https://github.com/rabuchaim/geoip2fast/releases/LATEST) 
- or create them yourself using ```geoip2dat.py```. *City data already includes country data.* 
- or download using the new function GeoIP2Fast.update_all() [read more below](#automatic-update-of-datgz-files)

| Download Content | File Name | File Size | Load Time | RAM Footprint |
| ---------- | :---------: | ---------: | --------: | ---------: |
| [City IPv4](https://github.com/rabuchaim/geoip2fast/releases/latest/download/geoip2fast-city.dat.gz)  | ```geoip2fast-city.dat.gz``` | 12 MiB | ~0.50 sec | ~270.0 MiB |
| [City IPv4+IPv6](https://github.com/rabuchaim/geoip2fast/releases/latest/download/geoip2fast-city-ipv6.dat.gz)  | ```geoip2fast-city-ipv6.dat.gz``` | 14 MiB | ~0.60 sec | ~400.0 MiB |
| [City+ASN IPv4](https://github.com/rabuchaim/geoip2fast/releases/latest/download/geoip2fast-city-asn.dat.gz)  | ```geoip2fast-city-asn.dat.gz``` | 13 MiB | ~0.60 sec | ~310.0 MiB |
| [City+ASN IPv4+IPv6](https://github.com/rabuchaim/geoip2fast/releases/latest/download/geoip2fast-city-asn-ipv6.dat.gz)  | ```geoip2fast-city-asn-ipv6.dat.gz``` | 17 MiB | ~0.70 sec | ~430.0 MiB |

> *If you are using pypy3, the loading time will increase a little, but the speed will be a little faster and the memory footprint will be lower.* 

**The new v1.2.X databases are not compatible with versions equal to or older than v1.1.X, and vice versa, obviously. The last version with support only for countries and ASN only is v1.1.X, which is still available with this command line: ```pip install geoip2fast==1.1.10```.**

```
What's new in v1.2.2 - 20/Jun/2024
- DAT files updated with MAXMIND:GeoLite2-CSV_20240618
- Removed the line "sys.tracebacklimit = 0" that was causing some problems 
  in Django. This line is unnecessary (https://github.com/rabuchaim/geoip2fast/issues/10)
- Maxmind inserted a new field into the CSV files called "is_anycast", and this broke 
  geoip2dat.py CSV reader. Insertion of the new field in the list of "fields" of
  the CSV reader that generates the .dat.gz files so that they can be updated.

- There are 2 reduced versions available for you to copy and paste
  into your own code without any dependencies and fast as always!
  Check these files in your library path:
    - geoip2fastmin.py (429 lines) 
    - geoip2fastminified.py (183 lines)
  It's in testing, but please open an issue if you have any problems 
  with either of these 2 versions.

- Removed functools.lru_cache. It is very useful when you have a function 
  that is repeated several times but takes a long time, which is not the 
  case of GeoIP2Fast where functions take milliseconds. On each call, 
  functools checks whether the value is already cached or not, and this 
  takes time. And we noticed that without functools and using the processor 
  and operating system's own cache makes GeoIP2Fast much faster without it
  even if you are searching for an IP for the first time.
  You can run tests and you will see that without functools.lru_cache 
  it is faster. If you want to use lru_cache, you can uncomment the 
  respective lines of code. There are 5 lines commented with @functools.lru_cache 

- As requested, 2 new methods to return a coverage of IPv4 and IPv6.
    def get_ipv4_coverage()->float
    def get_ipv6_coverage()->float

- New function get_database_info() that returns a dictionary with 
  detailed information about the data file currently in use.

- Made some adjustments to the --missing-ips and --coverage functions.  

- Now you can specify the data filename to be used on geoip2fast cli:
    geoip2fast geoip2fast-ipv6.dat.gz --self-test
    geoip2fast 9.9.9.9,1.1.1.1,2a10:8b40:: geoip2fast-asn-ipv6.dat.gz

- New functions to generate random IP addresses to be used in tests. 
  Returns a list if more than 1 IP is requested, otherwise returns a 
  string with only 1 IP address. If you request an IPv6 and the database
  loaded does not have IPv6 data, returns False. And the fuction of
  private address, returns an random IPv4 from network 10.0.0.0/8 or
  172.16.0.0/12 or 192.168.0.0/16.
    def generate_random_private_address(self,num_ips=1)->string or a list
    def generate_random_ipv4_address(self,num_ips=1)->string or a list
    def generate_random_ipv6_address(self,num_ips=1)->string or a list

- Put some flowers

```
<br>

![](https://raw.githubusercontent.com/rabuchaim/geoip2fast/main/images/geoip2fast_selftest.jpg)

<br>

## Installation
```bash
pip install geoip2fast
```
<br>

## DAT files updates

- You can create your own dat.gz file using [geoip2dat.py](#geoip2dat---update-geoip2fastdatgz-file-anytime) file.
- You can also [download the latest dat files](https://github.com/rabuchaim/geoip2fast/releases/tag/LATEST) that are updated automatically on Tuesdays and Fridays 
- And you can [update the dat files downloading from our releases repository](#automatic-update-of-datgz-files), via code or via command line.

<br>

## How does it work?

GeoIP2Fast has 4 datafiles included. Tha main file is ```geoip2fast.dat.gz``` with support Country lookups and only IPv4. Usually, these files are located into the library directory (```/usr/local/lib/python3.XX/dist-packages/geoip2fast```), but you can place it into the same directory of your application. The library automatically checks both paths, And the directory of your application overlaps the directory of the library. You can use an specific location also. 

The ```bisect()``` function is used together with some ordered lists of integers to search the Network/CountryCode (Yes! an IP address has an integer representation, try to ping this number: ```ping 134744072``` or this ```ping 2130706433``` ).

If GeoIP2Fast does not have a network IP address that was requested, a "not found in database" error will be returned. Unlike many other libraries that when not finding a requested network, gives you the geographical location of the network immediately below. The result is not always correct. 

Data file updates are made available twice a week in our [github releases](https://github.com/rabuchaim/geoip2fast/releases/latest). Files with City data and IPv6 support can also be downloaded there.

There are network gaps in the files we use as a source of data, and these missing networks are probably addresses that those responsible have not yet declared their location. Of all IPv4 on the internet (almost 4.3 billions IPs), our coverage is around 99.64% and we do not have information on approximately 15 million of them (~0,36%). It must be remembered that the geographical accuracy is the responsibility of the network block owners. If the owner (aka ASN) of the XXX.YYY.ZZZ.D/24 network range declares that his network range is located at "Foo Island", we must believe that an IP address of that network is there. 

> *Don't go to Foo Island visit a girl you met on the internet just because you looked up her IP on GeoIP2Fast and the result indicated that she is there.*

<br>

## Quick Start

Once the object is created, GeoIP2Fast loads automatically all needed data into memory. The lookup function returns an object called ```GeoIPDetail```. And you can get the values of it's properties just calling the name of proprerty: ```result.ip```, ```result.country_code```, ```result.country_name```, ```result.city.name```, ```result.city.subsubdivision_code```, ```result.city.subsubdivision_name```, ```result.cidr```, ```result.is_private```, ```result.asn_name```,```result.asn_cidr``` and ```result.elapsed_time```. Or use the function ```to_dict()``` to get the result as a dict. You can get values like ```result.to_dict()['country_code']```

When using it as a Python library, if you want to load a file other than ```geoip2fast.dat.gz```, you simply create the object by typing the name of the file you want to work with. The library first looks for the given file in the current directory and then in the library directory. If desired, you can directly specify the path. If don´t specify any file, the default ```geoip2fast.dat.gz``` will be used. Example: 

```python
>>> from geoip2fast import GeoIP2Fast
>>> geoip = GeoIP2Fast(geoip2fast_data_file="/my_data_files_path/geoip2fast-city-asn-ipv6.dat.gz",verbose=True)
GeoIP2Fast v1.2.1 is ready! geoip2fast-city-asn-ipv6.dat.gz loaded with 4.488.721 networks in 0.54506 seconds and using 426.28 MiB.
>>> print(geoip.lookup("191.251.128.1").pp_json())
{
   "ip": "191.251.128.1",
   "country_code": "BR",
   "country_name": "Brazil",
   "city": {
      "name": "Araraquara",
      "subdivision_code": "SP",
      "subdivision_name": "Sao Paulo"
   },
   "cidr": "191.251.128.0/20",
   "hostname": "",
   "asn_name": "TELEFONICA BRASIL S.A",
   "asn_cidr": "191.250.0.0/15",
   "is_private": false,
   "elapsed_time": "0.000147356 sec"
}
>>> geoip.get_database_path()
'/my_data_files_path/geoip2fast-city-asn-ipv6.dat.gz'
>>>
>>> result = geoip.lookup("3.2.35.65")
>>> result.city.name
'São Paulo'
>>> result.city.subdivision1_code
'SP'
>>> result.country_name
'Brazil'
>>> result.country_code
'BR'
>>> result.asn_name
'AMAZON-02'
>>> result.elapsed_time
'0.000011612 sec'
>>>
>>> result = geoip.lookup("10.20.30.40")
>>> result.country_name
'Private Network Class A'
>>> result.cidr
'10.0.0.0/8'
>>> result.is_private
True
>>>
```


```python
from geoip2fast import GeoIP2Fast

GEOIP = GeoIP2Fast()
result = GEOIP.lookup("200.204.0.10")
print(result)

# to use the country_code property
print(result.country_code)

# to print the ASN name property
print(result.asn_name)

# Before call the function get_hostname(), the property hostname will always be empty.
print("Hostname: "+result.hostname)
result.get_hostname()
print("Hostname: "+result.hostname)

# to work with output as a dict, use the function to_dict()
print(result.to_dict()['country_code'],result.to_dict()['country_name'])

# to check the date of the CSV files used to create the .dat file
print(GEOIP.get_source_info())

# to show the path of current loaded dat file
print(GEOIP.get_database_path())

# info about internal cache
print(GEOIP.cache_info())

# clear the internal cache
print(GEOIP.clear_cache())

# to see the difference after clear cache
print(GEOIP.cache_info())
```
There is a method to pretty print the result as json.dumps():
```python
>>> result = MyGeoIP.lookup("191.251.128.1")
>>> print(result.pp_json())
{
   "ip": "191.251.128.1",
   "country_code": "BR",
   "country_name": "Brazil",
   "city": {
      "name": "Araraquara",
      "subdivision_code": "SP",
      "subdivision_name": "Sao Paulo"
   },
   "cidr": "191.251.128.0/20",
   "hostname": "",
   "asn_name": "TELEFONICA BRASIL S.A",
   "asn_cidr": "191.250.0.0/15",
   "is_private": false,
   "elapsed_time": "0.000147356 sec"
}
```
or simply: ```result.pp_json(print_result=True)```

To see the start-up line without set ```verbose=True``` :
```python
>>> from geoip2fast import GeoIP2Fast
>>> G = GeoIP2Fast()
>>> G.startup_line_text
'GeoIP2Fast v1.2.0 is ready! geoip2fast.dat.gz loaded with 459.270 networks in 0.03393 seconds and using 25.25 MiB.'
>>>
```

Private/Reserved networks were included in the database just to be able to provide an answer if one of these IPs is searched. When it happens, the country_code will return "--", the "network name" will be displayed in the country_name and the range of that network will be displayed in the cidr property, and the property **is_private** is setted to **True**.

```python
>>> from geoip2fast import GeoIP2Fast
>>> geoip = GeoIP2Fast(verbose=True)
'GeoIP2Fast v1.2.0 is ready! geoip2fast.dat.gz loaded with 459.270 networks in 0.03393 seconds and using 25.25 MiB.'
>>>
>>> G.lookup("10.20.30.40")
{'ip': '10.20.30.40', 'country_code': '--', 'country_name': 'Private Network Class A', 'cidr': '10.0.0.0/8', 'hostname': '', 'asn_name': 'IANA.ORG', 'asn_cidr': '10.0.0.0/8', 'is_private': True, 'elapsed_time': '0.000015946 sec'}
>>> G.lookup("169.254.10.20")
{'ip': '169.254.10.20', 'country_code': '--', 'country_name': 'APIPA Automatic Priv.IP Addressing', 'cidr': '169.254.0.0/16', 'hostname': '', 'asn_name': 'IANA.ORG', 'asn_cidr': '169.254.0.0/16', 'is_private': True, 'elapsed_time': '0.000093106 sec'}
>>>
```

You can change the behavior of what will be returned in country_code property of "private networks" and for "networks not found":

```python
>>> from geoip2fast import GeoIP2Fast
>>> G = GeoIP2Fast()
>>> G.set_error_code_private_networks("@@")
'@@'
>>> G.lookup("10.20.30.40")
{'ip': '10.20.30.40', 'country_code': '@@', 'country_name': 'Private Network Class A', 'cidr': '10.0.0.0/8', 'hostname': '', 'asn_name': 'IANA.ORG', 'asn_cidr': '10.0.0.0/8', 'is_private': True, 'elapsed_time': '0.000144236 sec'}
>>>
>>> G.set_error_code_network_not_found("##")
'##'
>>> G.lookup("23.142.129.0")
{'ip': '23.142.129.0', 'country_code': '##', 'country_name': '<not found in database>', 'cidr': '', 'hostname': '', 'asn_name': '', 'asn_cidr': '', 'is_private': False, 'elapsed_time': '0.000012352 sec'}
>>>
```
You can use it as a CLI also from any path:

```bash
# geoip2fast
GeoIP2Fast v1.2.0 Usage: geoip2fast.py [-h] [-v] [-d] <ip_address_1>,<ip_address_2>,<ip_address_N>,...
# geoip2fast 9.9.9.9,15.20.25.30 -d
{
   "ip": "9.9.9.9",
   "country_code": "US",
   "country_name": "United States",
   "cidr": "9.9.9.9/32",
   "hostname": "dns9.quad9.net",
   "asn_name": "",
   "asn_cidr": "",
   "is_private": false,
   "elapsed_time": "0.000034214 sec",
   "elapsed_time_hostname": "0.001079759 sec"
}
{
   "ip": "15.20.25.30",
   "country_code": "US",
   "country_name": "United States",
   "cidr": "15.0.0.0/10",
   "hostname": "<Unknown host>",
   "asn_name": "",
   "asn_cidr": "",
   "is_private": false,
   "elapsed_time": "0.000022537 sec"
}
# geoip2fast "2.3.4.5, 4.5.6.7, 8.9.10.11" | jq -r '.country_code'
FR
US
US
# geoip2fast 8.8.8.8,1.1.1.1,200.204.0.10 -d | jq -r '.hostname'
dns.google
one.one.one.one
resolver1.telesp.net.br
```

## How fast is it?

With an virtual machine with 1 CPU and 4Gb of RAM, we have lookups **lower than 0,00003 seconds**. And if the lookup still in library´s internal cache, the elapsed time goes down to 0,000003 seconds. **GeoIP2Fast can do more than 100K queries per second, per core**. It takes less than 0,07 seconds to load the datafile into memory and get ready to lookup. Use ```verbose=True``` to create the object GeoIP2Fast to see the spent time to start.

Now some tests are included in the geoip2fast.py file. 

```bash
# geoip2fast -h
GeoIP2Fast v1.2.2 Usage: geoip2fast.py [-h] [-v] [-d] <ip_address_1>,<ip_address_2>,<ip_address_N>,...

Tests parameters:
  --self-test         Starts a self-test with some randomic IP addresses.
  --self-test-city    Starts a self-test with some randomic IP addresses and with city names support.
  --speed-test        Do a speed test with 1 million on randomic IP addresses.
  --random-test       Start a test with 1.000.000 of randomic IPs and calculate a lookup average time.

  --coverage [-v]     Shows a statistic of how many IPs are covered by current dat file.
  --missing-ips [-v]  Print all IP networks that doesn't have geo information (only for IPv4).

Automatic update:
  --update-all [-v]    Download all dat.gz files available in the repository below:
                       https://github.com/rabuchaim/geoip2fast/releases/download/LATEST/

  --update-file <geoip2fast_dat_filename> [-v]
                       Download a specific filename from the repository. Only one file is allowed.
                       Allowed values are: geoip2fast.dat.gz OR geoip2fast-ipv6.dat.gz OR
                                           geoip2fast-asn.dat.gz OR geoip2fast-asn-ipv6.dat.gz OR
                                           geoip2fast-city.dat.gz OR geoip2fast-city-ipv6.dat.gz OR
                                           geoip2fast-city-asn.dat.gz OR geoip2fast-city-asn-ipv6.dat.gz

  --dest <a directory path or a filename> [-v]
                       Specify the destination directory for the downloaded files. When combined with
                       the '--update-file' parameter, you can specify an existing directory, with or
                       without a file name, or you can just specify a file name. In the absence of
                       this parameter or directory information, the library directory will be used
                       as default value. This parameter is optional. The filename must end
                       with .dat.gz extension.

                       Use the verbose parameter (-v) if you want to see the download progress,
                       otherwise there will be no output. You also have to use this parameter
                       to view possible errors in your console.

More options:
  -d                  Resolve the DNS of given IP address.
  -h                  Show this help text.
  -v                  Verbose mode.
  -vvv                Shows the location of current dat file in use.
```

```geoip2fast --self-test```
```bash
# geoip2fast --self-test
GeoIP2Fast v1.2.0 is ready! geoip2fast.dat.gz loaded with 459.270 networks in 0.09268 seconds and using 71.04 MiB.

Starting a self-test...

> 266.266.266.266          <invalid ip address>           [0.000018189 sec]  Cached > [0.000003038 sec]
> 192,0x0/32               <invalid ip address>           [0.000002468 sec]  Cached > [0.000001868 sec]
> 10.20.30.40           -- Private Network Class A        [0.000020032 sec]  Cached > [0.000001231 sec] IANA.ORG
> 38.174.13.98          CA Canada                         [0.000015079 sec]  Cached > [0.000001414 sec] AS-NSL-261
> 102.195.139.98        -- <not found in database>        [0.000004650 sec]  Cached > [0.000000471 sec]
> 139.5.38.161          IN India                          [0.000012635 sec]  Cached > [0.000000845 sec] Five network Broadband Solution Pvt Ltd
> 4.219.112.222         NO Norway                         [0.000009926 sec]  Cached > [0.000000727 sec] MICROSOFT-CORP-MSN-AS-BLOCK
> 137.44.167.24         GB United Kingdom                 [0.000009575 sec]  Cached > [0.000000663 sec] Jisc Services Limited
> 28.92.226.103         US United States                  [0.000009599 sec]  Cached > [0.000000605 sec] DNIC-AS-00749
> 180.115.120.126       CN China                          [0.000010468 sec]  Cached > [0.000000702 sec] Chinanet
(.....)
```

```geoip2fast --speed-test```
```bash
# geoip2fast --speed-test
GeoIP2Fast v1.2.0 is ready! geoip2fast.dat.gz loaded with 459.270 networks in 0.09292 seconds and using 71.05 MiB.

Calculating current speed... wait a few seconds please...

Current speed: 143159.49 lookups per second (1.000.000 IPs with an average of 0.000006985 seconds per lookup) [6.98522 sec]
```

```geoip2fast --coverage```
```bash
# geoip2fast --coverage
GeoIP2Fast v1.2.0 is ready! geoip2fast.dat.gz loaded with 4.488.723 networks in 0.47685 seconds and using 408.66 MiB.

Use the parameter '-v' to see all networks included in your /opt/geoip2fast/geoip2fast/geoip2fast.dat.gz file.

Current IPv4 coverage:  99.64% (4.279.552.038 IPv4 in 3.246.406 networks) [0.59747 sec]
Current IPv6 coverage:   0.40% (1.364.444.943.175.748.876.962.337.373.462.462.464 IPv6 in 1.242.317 networks) [0.59747 sec]
```
```geoip2fast --coverage -v```
```bash
# geoip2fast --coverage -v
GeoIP2Fast v1.2.0 is ready! geoip2fast.dat.gz loaded with 753.871 networks in 0.13392 seconds and using 103.54 MiB.

Use the parameter '-v' to see all networks included in your /usr/local/lib/python3.11/dist-packages/geoip2fast/geoip2fast.dat.gz file.

- Network: 0.0.0.0/8           IPs: 16777216   -- Reserved for self identification    0.000042983 sec
- Network: 1.0.0.0/24          IPs: 256        AU Australia                           0.000017615 sec
- Network: 1.0.1.0/24          IPs: 256        CN China                               0.000011633 sec
- Network: 1.0.2.0/23          IPs: 512        CN China                               0.000009464 sec
- Network: 1.0.4.0/22          IPs: 1024       AU Australia                           0.000008925 sec
(.....)
- Network: 2c0f:ffc0::/32      IPs: 79228162514264337593543950336 ZA South Africa                        0.000026057 sec
- Network: 2c0f:ffc8::/32      IPs: 79228162514264337593543950336 ZA South Africa                        0.000028565 sec
- Network: 2c0f:ffd0::/32      IPs: 79228162514264337593543950336 ZA South Africa                        0.000026283 sec
- Network: 2c0f:ffd8::/32      IPs: 79228162514264337593543950336 ZA South Africa                        0.000026832 sec
- Network: 2c0f:ffe8::/32      IPs: 79228162514264337593543950336 NG Nigeria                             0.000027137 sec
- Network: 2c0f:fff0::/32      IPs: 79228162514264337593543950336 NG Nigeria                             0.000028008 sec
- Network: fd00::/8            IPs: 1329227995784915872903807060280344576 -- Reserved for Unique Local Addresses 0.000031203 sec

Current IPv4 coverage:  99.64% (4.279.420.966 IPv4 in 459.270 networks) [64.13669 sec]
Current IPv6 coverage:   0.40% (1.364.444.943.175.748.876.962.337.373.462.462.464 IPv6 in 294.601 networks) [64.13669 sec]
```

```geoip2fast --missing-ips``` 
```bash
# geoip2fast --missing-ips
GeoIP2Fast v1.2.0 is ready! geoip2fast.dat.gz loaded with 753.871 networks in 0.13392 seconds and using 103.54 MiB.

Searching for missing IPs... 

From 1.34.65.179     to 1.34.65.179     > Network 1.34.65.180/32     > Missing IPs: 1
From 1.46.23.235     to 1.46.23.235     > Network 1.46.23.236/32     > Missing IPs: 1
From 2.12.211.171    to 2.12.211.171    > Network 2.12.211.172/32    > Missing IPs: 1
(.....)
From 220.158.148.0   to 220.158.151.255 > Network 220.158.152.0/22   > Missing IPs: 1024
From 223.165.0.0     to 223.165.3.255   > Network 223.165.4.0/22     > Missing IPs: 1024

>>> Valid IP addresses without geo information: 15.551.441 (0.36% of all IPv4) [27.17811 sec]
```
> Some IPs are excluded as described in page "Do Not Sell My Personal Information Requests" at Maxmind website.

<br>

## GeoIP2Dat - update geoip2fast.dat.gz file anytime

The updates of geoip2fast.dat.gz file will be published twice a week on Github https://github.com/rabuchaim/geoip2fast/releases/LATEST. You can also create your own dat file whenever you want, see instructions below.

Download the Geolite2 (COUNTRY, CITY and ASN) CSV files from Maxmind website and place it into some diretory (in this example, was placed into ```/opt/maxmind/```). Extract all zip files in this directory and run ```geoip2dat``` to see the options.

![](https://raw.githubusercontent.com/rabuchaim/geoip2fast/main/images/geoip2dat01.jpg)

![](https://raw.githubusercontent.com/rabuchaim/geoip2fast/main/images/geoip2dat02.jpg)

The options \(```--country-dir``` OR ```--city-dir```\) AND ```--output-dir``` are mandatory. Specify the path of extracted files in ```--country-dir``` or ```--city-dir``` option. And for ```--output-dir```, put the current path ```./```. 

If you want to add support for ASN data, add the option ```--asn-dir```. And if you want to add IPv6 support, just add ```--with-ipv6``` to your command line.

You can choose the language of country locations. The default is ```en```.

After creation of ```geoip2dat.dat.gz``` file, move or copy this file to the directory of your application or to the directory of GeoIP2Fast library. You choose. 

![](https://raw.githubusercontent.com/rabuchaim/geoip2fast/main/images/geoip2dat03.jpg)

**From now you don't depend on anyone to have your data file updated.** There's no point the code being open-source if you're dependent of a single file. 

> *The Philosophers call it 'Libertas'* 

<br>

## Automatic update of dat.gz files

From version v1.2.1 onwards, it is now possible to update the dat.gz files that were made available in our releases repository. You can update via command line or via code.

- Download the file "geoip2fast-asn-ipv6.dat.gz" and save it as "geoip2fast.dat.gz":

```python
>>> from geoip2fast import GeoIP2Fast
>>> G = GeoIP2Fast(verbose=True)
GeoIP2Fast v1.2.1 is ready! geoip2fast.dat.gz loaded with 459270 networks in 0.03297 seconds and using 25.12 MiB.
>>> update_result = G.update_file('geoip2fast-asn-ipv6.dat.gz','geoip2fast.dat.gz',verbose=False)
>>> G.reload_data(verbose=True)
GeoIP2Fast v1.2.1 is ready! geoip2fast.dat.gz loaded with 753871 networks in 0.12917 seconds and using 113.54 MiBTrue
>>>
```
- Update all files:

```python
>>> from geoip2fast import GeoIP2Fast
>>> G = GeoIP2Fast()
>>> update_result = G.update_all(verbose=True)
- Opening URL https://github.com/rabuchaim/geoip2fast/releases/download/LATEST/geoip2fast.dat.gz
- Last Modified Date: Mon, 27 Nov 2023 02:40:08 GMT
- Downloading geoip2fast.dat.gz... 100.00% of 1.06 MiB [6.51 MiB/s] [0.163 sec]
- File saved to: /opt/geoip2fast/geoip2fast-legacy/geoip2fast/geoip2fast.dat.gz

- Opening URL https://github.com/rabuchaim/geoip2fast/releases/download/LATEST/geoip2fast-ipv6.dat.gz
- Last Modified Date: Mon, 27 Nov 2023 02:40:08 GMT
- Downloading geoip2fast-ipv6.dat.gz... 100.00% of 1.73 MiB [9.66 MiB/s] [0.179 sec]
- File saved to: /opt/geoip2fast/geoip2fast-legacy/geoip2fast/geoip2fast-ipv6.dat.gz

- Opening URL https://github.com/rabuchaim/geoip2fast/releases/download/LATEST/geoip2fast-asn.dat.gz
- Last Modified Date: Mon, 27 Nov 2023 02:40:08 GMT
- Downloading geoip2fast-asn.dat.gz... 100.00% of 3.06 MiB [8.63 MiB/s] [0.354 sec]
- File saved to: /opt/geoip2fast/geoip2fast-legacy/geoip2fast/geoip2fast-asn.dat.gz

- Opening URL https://github.com/rabuchaim/geoip2fast/releases/download/LATEST/geoip2fast-asn-ipv6.dat.gz
- Last Modified Date: Mon, 27 Nov 2023 02:40:08 GMT
- Downloading geoip2fast-asn-ipv6.dat.gz... 100.00% of 4.09 MiB [7.66 MiB/s] [0.534 sec]
- File saved to: /opt/geoip2fast/geoip2fast-legacy/geoip2fast/geoip2fast-asn-ipv6.dat.gz
>>>
```
- Update all files silently and verify if there are errors:
```python
>>> from geoip2fast import GeoIP2Fast
>>> G = GeoIP2Fast()
>>> update_result = G.update_all(verbose=False)
>>> errors_result = [item for item in update_result if item['error'] is not None]
>>> print(errors_result)
[]
```
- You can change the update URL if you want.
```
>>> G.get_update_url()
'https://github.com/rabuchaim/geoip2fast/releases/download/LATEST/'
>>> G.set_update_url("https://github.com/YOUR_OWN_REPO/YOUR_PROJECT/releases/download/latest/")
True
>>> G.get_update_url()
'https://github.com/YOUR_OWN_REPO/YOUR_PROJECT/releases/download/latest/'
>>>
```
- Update the file "geoip2fast-asn-ipv6.dat.gz" and overwrite "geoip2fast.dat.gz" and print the result. 
```python
>>> from geoip2fast import GeoIP2Fast
>>> G = GeoIP2Fast(verbose=True)
GeoIP2Fast v1.2.1 is ready! geoip2fast.dat.gz loaded with 459270 networks in 0.04414 seconds and using 5.02 MiB.
>>> update_result = G.update_file('geoip2fast-asn-ipv6.dat.gz','geoip2fast.dat.gz',verbose=False)
>>> from pprint import pprint as pp
>>> pp(update_result,sort_dicts=False)
{'error': None,
 'url': 'https://github.com/rabuchaim/geoip2fast/releases/download/LATEST/geoip2fast-asn-ipv6.dat.gz',
 'remote_filename': 'geoip2fast-asn-ipv6.dat.gz',
 'last_modified_date': 'Mon, 27 Nov 2023 02:40:08 GMT',
 'file_size': 4289564,
 'file_destination': '/opt/geoip2fast/geoip2fast-legacy/geoip2fast/geoip2fast.dat.gz',
 'average_download_speed': '4.09 MiB/sec',
 'elapsed_time': '0.587267'}
>>>
>>> G.reload_data(verbose=True)
GeoIP2Fast v1.2.1 is ready! geoip2fast.dat.gz loaded with 753871 networks in 0.12245 seconds and using 57.55 MiB.
>>>

```
- **Using the command line, no message will be displayed on the console unless you use the -v parameter**
- Update all files via command line and save them in '/tmp/' directory:
```bash
# geoip2fast --update-all --dest /tmp/ -v
- Opening URL https://github.com/rabuchaim/geoip2fast/releases/download/LATEST/geoip2fast.dat.gz
- Last Modified Date: Mon, 27 Nov 2023 02:40:08 GMT
- Downloading geoip2fast.dat.gz... 100.00% of 1.06 MiB [10.41 MiB/s] [0.102 sec]
- File saved to: /tmp/geoip2fast.dat.gz

- Opening URL https://github.com/rabuchaim/geoip2fast/releases/download/LATEST/geoip2fast-ipv6.dat.gz
- Last Modified Date: Mon, 27 Nov 2023 02:40:08 GMT
- Downloading geoip2fast-ipv6.dat.gz... 100.00% of 1.73 MiB [9.46 MiB/s] [0.183 sec]
- File saved to: /tmp/geoip2fast-ipv6.dat.gz

- Opening URL https://github.com/rabuchaim/geoip2fast/releases/download/LATEST/geoip2fast-asn.dat.gz
- Last Modified Date: Mon, 27 Nov 2023 02:40:08 GMT
- Downloading geoip2fast-asn.dat.gz... 100.00% of 3.06 MiB [7.06 MiB/s] [0.433 sec]
- File saved to: /tmp/geoip2fast-asn.dat.gz

- Opening URL https://github.com/rabuchaim/geoip2fast/releases/download/LATEST/geoip2fast-asn-ipv6.dat.gz
- Last Modified Date: Mon, 27 Nov 2023 02:40:08 GMT
- Downloading geoip2fast-asn-ipv6.dat.gz... 100.00% of 4.09 MiB [7.31 MiB/s] [0.560 sec]
- File saved to: /tmp/geoip2fast-asn-ipv6.dat.gz
```
- Update the file "geoip2fast-asn-ipv6.dat.gz" and overwrite "geoip2fast.dat.gz"
```bash
# geoip2fast --update-file geoip2fast-asn-ipv6.dat.gz --dest geoip2fast.dat.gz -v
- Opening URL https://github.com/rabuchaim/geoip2fast/releases/download/LATEST/geoip2fast-asn-ipv6.dat.gz
- Last Modified Date: Mon, 27 Nov 2023 02:40:08 GMT
- Downloading geoip2fast-asn-ipv6.dat.gz... 100.00% of 4.09 MiB [4.29 MiB/s] [0.954 sec]
- File saved to: /opt/geoip2fast/geoip2fast-legacy/geoip2fast/geoip2fast.dat.gz
```
- Update the file "geoip2fast.dat.gz" and save it in the library path
```bash
# geoip2fast --update-file geoip2fast.dat.gz -v
- Opening URL https://github.com/rabuchaim/geoip2fast/releases/download/LATEST/geoip2fast.dat.gz
- Last Modified Date: Mon, 27 Nov 2023 02:40:08 GMT
- Downloading geoip2fast.dat.gz... 100.00% of 1.06 MiB [9.54 MiB/s] [0.111 sec]
- File saved to: /opt/geoip2fast/geoip2fast-legacy/geoip2fast/geoip2fast.dat.gz
```
- Update the file "geoip2fast.dat.gz" and save it in the library path

```bash
# geoip2fast --update-file geoip2fast.dat.gz
# echo $?
0
```
- An example of a simulated download failure: 
```bash
# geoip2fast.py --update-file geoip2fast.dat.gz -v
- Opening URL https://github.com/rabuchaim/geoip2fast/releases/download/A_LATEST/geoip2fast.dat.gz
- Error: HTTP Error 404: Not Found - https://github.com/rabuchaim/geoip2fast/releases/download/A_LATEST/geoip2fast.dat.gz
# echo $?
1
```
```bash
# geoip2fast.py --update-file geoip2fast.dat.gz -v
- Opening URL https://github.com/rabuchaim/geoip2fast/releases/download/LATEST/geoip2fast.dat.gz
- Last Modified Date: Mon, 27 Nov 2023 02:40:08 GMT
PermissionError: [Errno 1] Operation not permitted: '/opt/geoip2fast/geoip2fast-legacy/geoip2fast/geoip2fast.dat.gz'
# echo $?
1
```

<br>

## Using your own networks

I´m planning to create an option to include your own networks in the database. For example, imagine you have a large private network on AWS, and each subnet is in a different region. You will be able to include them in the database to use GeoIP2Fast in your application. For now, you can edit the **reservedNetworks** variable at the beginning of the ```geoip2dat.py``` file and then generate your own data file.

Suggestions and ideas are welcome. The initial idea is to include an option ```--include-networks``` in ```geoip2dat.py``` where you enter a json file.

<br>

## Create your own GeoIP CLI with 6 lines

1. Create a file named ```geoipcli.py``` and save it in your home directory with the text below:
```python
#!/usr/bin/env python3
import os, sys, geoip2fast
if len(sys.argv) > 1 and sys.argv[1] is not None:
    geoip2fast.GeoIP2Fast().lookup(sys.argv[1]).pp_json(print_result=True)
else:
    print(f"Usage: {os.path.basename(__file__)} <ip_address>")
```
2. Give execution permisstion to your file and create a symbolic link to your new file into ```/usr/sbin``` folder, like this (let's assume that you saved this file into directory ```/root```)
```bash
chmod 750 /root/geoipcli.py
ln -s /root/geoipcli.py /usr/sbin/geoipcli
```
3. Now, you just need to call ```geoipcli``` from any path.
```bash
# geoipcli
Usage: geoipcli <ip_address>
# geoipcli 1.2.3.4
{
   "ip": "1.2.3.4",
   "country_code": "AU",
   "country_name": "Australia",
   "cidr": "1.2.3.0/24",
   "hostname": "",
   "is_private": false,
   "elapsed_time": "0.000019727 sec"
}
```
<br>

## GeoIP libraries that inspired me

**GeoIP2Nation - https://pypi.org/project/geoip2nation/** (Created by Avi Asher)

This library uses sqlite3 in-memory tables and use the same search concepts as GeoIP2Fast (based on search by the first´s IPs). Simple and fast! Unfortunately it is no longer being updated and that is why I developed GeoIP2Fast.

**GeoIP2 - https://pypi.org/project/geoip2/** (Created by Maxmind)

This is the best library to work with Maxmind paid subscription or with the free version. You can use http requests to Maxmind services or work with local Maxmind MMDB binary files. Pretty fast too. Sign-up to have access to all files of the free version https://dev.maxmind.com/geoip/geolite2-free-geolocation-data

**\* Maxmind is a registered trademark** - https://www.maxmind.com

## TO DO list
- a GeoIP2Fast Server that supports our dat.gz and any kind of mmdb file; **<<< In final tests! the FASTORNADO Server **
- a version to support any kind of MMDB file with coordinates and more; **<<< ON THE WAY! **
- a better manual, maybe at readthedocs.io;
- a mod_geoip2fast for NGINX;
- **Done in v1.1.10/v1.2.1** - automatic update of dat.gz files;
- **Done in v1.2.0** - a version with cities;
- **Done in v1.1.0** - *IPv6 support*.
- **Done in v1.0.5** - *a version with ASN*.
- **Done in v1.0.2** - *provide a script to update the base. If you have the paid subscription of Maxmind, you can download the files, extract into some directory and use this script to create your own geoip2fast.dat.gz file with the most complete, reliable and updated GeoIP information*.

## Sugestions, feedbacks, bugs, wrong locations...
E-mail me: ricardoabuchaim at gmail.com

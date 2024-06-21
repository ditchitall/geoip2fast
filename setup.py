import codecs
from setuptools import setup, find_packages

setup(
    name='geoip2fast',
    version='1.2.2',
    description='GeoIP2Fast is the fastest GeoIP2 country/city/asn lookup library that supports IPv4 and IPv6. A search takes less than 0.00003 seconds. It has its own data file updated twice a week with Maxmind-Geolite2-CSV, supports IPv4/IPv6 and is Pure Python!',
    url='https://github.com/rabuchaim/geoip2fast',
    author='Ricardo Abuchaim',
    author_email='ricardoabuchaim@gmail.com',
    maintainer='Ricardo Abuchaim',
    maintainer_email='ricardoabuchaim@gmail.com',
    project_urls={
        "Issue Tracker": "https://github.com/rabuchaim/geoip2fast/issues",
        "Source code": "https://github.com/rabuchaim/geoip2fast",
        "Latest DAT files": "https://github.com/rabuchaim/geoip2fast/releases/latest",
        "Legacy v1.1.X DAT files": "https://github.com/rabuchaim/geoip2fast/releases/tag/LEGACY",
    },    
    bugtrack_url='https://github.com/rabuchaim/geoip2fast/issues',    
    license='MIT',
    keywords=['geoip','geoip2','geolite2','maxmind','geoip2fast','geolocation','geolocalization','geo ip','ipaddress','ip','geo','ipv4','ipv6','pure-python','purepython','pure python','geoiptofast','geoiptoofast','geoip2dat','mmdb','tools'],
    packages=['geoip2fast'],
    py_modules=['geoip2fast', 'geoip2dat'],
    package_dir = {'geoip2fast': 'geoip2fast'},
    include_package_data=True,
    zip_safe = False,
    package_data={
        'geoip2fast': [
            'CHANGELOG', 
            'geoip2fast.dat.gz',
            'geoip2fast-ipv6.dat.gz',
            'geoip2fast-asn.dat.gz',
            'geoip2fast-asn-ipv6.dat.gz',
            'tests/geoip2fast_test.py',
            'tests/speed_test.py',
            'tests/coverage_test.py',
            'tests/compare_with_mmdb.py',
            'tests/random_test.py',
            'tests/geoipcli.py',
        ],
    },
    entry_points={
        'console_scripts': [
            'geoip2fast = geoip2fast.geoip2fast:main_function',
            'geoip2dat = geoip2fast.geoip2dat:main_function'
        ]
    },
    python_requires=">=3.7",
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Security',
        'Topic :: Internet',
        'Topic :: Internet :: Finger',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 11',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',  
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: MIT License',
    ],
    long_description=codecs.open("README.md","r","utf-8").read(),
    long_description_content_type='text/markdown',
)

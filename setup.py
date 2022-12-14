from setuptools import setup
import os, re

def read(*names, **kwargs):
    with open(os.path.join(os.path.dirname(__file__), *names), encoding='utf8') as fp:
        return fp.read()

def find_value(name):
    data_file = read('honeypot_vpn', '__doc__.py')
    data_match = re.search(r"^__%s__ += ['\"]([^'\"]*)['\"]" % name, data_file, re.M)
    if data_match:
        return data_match.group(1)
    raise RuntimeError(f"Unable to find '{name}' string.")

setup(
    name                = find_value('title'),
    version             = find_value('version'),
    description         = find_value('description'),
    long_description    = read('README.rst'),
    url                 = find_value('url'),
    author              = find_value('author'),
    author_email        = find_value('email'),
    license             = find_value('license'),
    python_requires     = '>=3.6',
    keywords            = find_value('keywords'),
    packages            = ['honeypot_vpn'],
    package_data= {
        "honeypot_vpn": [
        "logger.cfg"
        ]
    },
    classifiers         = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires    = [
        'pycryptodome >= 3.7.2',
        'pproxy >= 2.0.0',
        'python-logstash >= 0.4.8',
        'requests >= 2.28.1',
    ],
    entry_points        = {
        'console_scripts': [
            'honeypot-vpn=honeypot_vpn.server:main',
        ],
    },
)

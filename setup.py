from setuptools import setup


setup(
    name='mercuro',
    version='0.1.1',
    author='Brian Cline',
    author_email='brian.cline@gmail.com',
    description=('A simple daemon that listens for syslog events and '
                 'forwards them to a Riemann server.'),
    license = 'Apache',
    keywords = 'syslog rsyslog riemann logging',
    url = 'https://github.com/briancline/mercuro',
    packages=['mercuro'],
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)

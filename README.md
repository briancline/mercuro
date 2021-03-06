Mercuro
=======

Mercuro is a non-concurrent, unintelligent, Python-based threaded syslog
listener that forwards all its events to a [Riemann][1] server.

All interaction with Riemann is handled via the [Bernhard][2] library.

You probably shouldn't use Mercuro in production yet, at least until it
provides concurrency, forking, and a config file.

See test.py for example use.


## Installing

This is all you need:

    pip install mercuro

Or, if you want to install from source:

    git clone https://github.com/briancline/mercuro.git
    cd mercuro
    sudo python setup.py install


  [1]: http://riemann.io/
  [2]: https://github.com/banjiewen/bernhard

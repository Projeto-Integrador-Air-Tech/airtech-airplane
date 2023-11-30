import logging
from cheroot.wsgi import Server as WSGIServer, PathInfoDispatcher
from cheroot.ssl.builtin import BuiltinSSLAdapter
from routes.aircraft import run_app as run_aircraft_app
from routes.model import run_app as run_model_app

AIRCRAFT = run_aircraft_app()
MODEL = run_model_app()
DISPATCHER = PathInfoDispatcher([('/aircraft', AIRCRAFT), ('/model', MODEL)])

PORT = 8060
SERVER = WSGIServer(('0.0.0.0', PORT), DISPATCHER)

if __name__ == '__main__':
    logging.basicConfig(format='', level=logging.INFO)
    logging.info('Running server on port %s', PORT)
    SERVER.safe_start()

from OpenSSL import SSL
from twisted.internet import ssl, reactor
from twisted.internet.protocol import Protocol, Factory
import json
import os
import time
import widget_handler

PORT = 9500
# Note:  The port number for the server doesn't really matter since the "proxy" (socat) will be used to redirect the
# Widget traffic to wherever we want.   If you changed this port to 5000 and ran the server on the BeagleBone's host
# computer then you wouldn't need socat.  However, you should make sure that your system is tested with a proxy
# because it will be necessary for connecting to the live server.

class DoorServerFactory(Factory):
    """
    Builds the DoorServer to be used in handling widget requests.
    """
    def buildProtocol(self, addr):
        return DoorServer()


# TODO: Make this thread-safe and/or figure out what will happen when multiple requests come in simultaneously
class DoorServer(Protocol):
    """
    Handles incoming requests on TCP port.
    Expect request data to be formatted as a JSON object with:
        type:     open_door | register_device | master_change_password | tenant_change_password
        device_id: <any unique identifier for the device>
        pin:   The pin encoded as ASCII -- only sent with 'open_door' request.
        current_pin:  Sent with tenant_change_password request.
        new_pin:      Sent with tenant_change_password request.
        master_pin:   Sent with master_change_password request.
    """

    # this function is called whenever we receive new data
    def dataReceived(self, data):
        """
        Function that determines if the request is valid, then sends the data to the handler
        """
        success = 0
        error = None
        flag = None

        try:
            request = json.loads(data)
        except ValueError:
            # Bad data
            self.send_response(0)
            return

        # TODO:  Should verify that the json object has all the fields that we expect smile emoticon

        (success, error, flag) = widget_handler.handle_request(request)

        self.send_response(success, error, flag)



    def send_response(self, success, error, flag):
        """
        Send a response back to the Widget device with success value of 0 or 1
        and if success==1, then also send the flag
        """

        d = {'success' : success}
        # Add the flag if we have one and if we had success
        if (error is not None):
            d['error'] = error
        if (flag is not None):
            d['flag'] = flag

        self.transport.write(json.dumps(d))

# def verifyCallback(connection, x509, errnum, errdepth, ok):
#     if not ok:
#         print 'Invalid Cert from subject:', x509.get_subject()
#         return False
#     return True

def main():
    """
    Loads the registered-widgets file.
    Opens up ServerFactory to listen for requests on the specified port.
    """
    widget_handler.setup();

    # contextFactory = ssl.DefaultOpenSSLContextFactory(
    #     'keys/server.key', 'keys/server.crt'
    #     )
    #
    # context = contextFactory.getContext(
    #     SSL.VERIFY_PEER | SSL.VERIFY_FAIL_IF_NO_PEER_CERT,
    #     verifyCallback
    #     )
    #
    # context.set_verify()

    # factory = protocol.ServerFactory()
    # factory.protocol = DoorServer
    print "Starting DoorApp server listening on port %d" % PORT
    reactor.listenSSL(PORT, DoorServerFactory(),
                      ssl.DefaultOpenSSLContextFactory(
            'certs/key.pem', 'certs/cert.pem'))
    reactor.run()

if __name__ == '__main__':
    main()

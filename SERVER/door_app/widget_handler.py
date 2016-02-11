import json
import os

ROOTDIR = os.path.dirname(__file__)
REGISTERED_FILE = os.path.join(ROOTDIR, 'registered-widgets.txt')
REQUESTED_FILE = os.path.join(ROOTDIR, 'requested-widgets.txt')
REGISTERED_DEVICES = {}
PASSWORD_ATTEMPTS = {}

def setup():
    print "Hello from the other file."
    open(REGISTERED_FILE, 'a').close() # touch the file so that it exists

    with open(REGISTERED_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip lines that start with '#' so that we can comment-out lines
            if line.startswith('#'): continue
            print "Loading line: '%s'" % line

            new_widget = Widget(json_str=line)
            if new_widget.device_id in REGISTERED_DEVICES:
                print "Skipping duplicate device ID %s" % repr(new_widget.device_id)
            else:
                REGISTERED_DEVICES[new_widget.device_id] = new_widget

class Widget(object):
    """
    Represents a Widget Device
    """

    def __init__(self, json_str):
        # Populate object attributes from JSON object
        data = json.loads(json_str)
        # TODO: Validate JSON
        self.device_id = data.get('device_id', None)
        self.pin = data.get('pin', None)
        self.flag = data.get('flag', None)
        self.device_key = data.get('device_key', None)


def handle_request(request):
    success = 0         # 1 indicates success, 0 indicates failure
    errorMsg = None     # Will be error msg if success = 0
    flag = None         # Will contain flag if required by request and sucess = 1

    # Register Request
    if request["type"] == 'register_device':
        print "Register request (%s)" % repr(request)
        success, errorMsg, flag = add_reg_request(request['device_key'], request['device_id'])
        return (success, errorMsg, flag);

    else:
        # For all requests other than register_device, we need to verify the device id and key
        if (request['device_id'] not in REGISTERED_DEVICES or
            REGISTERED_DEVICES[request['device_id']].device_key != request['device_key']):
            errorMsg = "Denying request with invalid device_id or invalid device_key"
            return (0, errorMsg, None)


    if request["type"] == 'open_door':
        #print "Open door request (%s)" % repr(request)
        (success, errorMsg, flag) = open_door_request(request)

    elif request["type"] == 'master_change_password':
        print "PIN change request using master PIN (%s)" % repr(request)
        if request["master_pin"] == MASTER_PIN:
            success = update_registered(request['device_id'], request['new_pin'])
        else:
            success = 0

    elif request["type"] == 'tenant_change_password':
        print "Tenant PIN change request (%s)" % repr(request)
        success,_ = verify_correct_pin(request['device_id'], request['current_pin'])
        if success:
            success = update_registered(request['device_id'], request['new_pin'])
    else:
        print "Unknown request (%s)" % repr(request)
        success = 0

def verify_correct_pin(device_id, pin):
    """
    Verify that the correct pin was sent for the given device_id.
    Returns tuple of (success_code, errorMsg)
    """
    if device_id not in REGISTERED_DEVICES:
        # This device isn't registered
        return 0

    if not verify_attempt_timeout(device_id):
        # Must wait to attempt again
        return (0, "Exceeded 1 pasword attempt per minute.  Please wait to try again.")


    if REGISTERED_DEVICES[device_id].pin == pin:
        return (1, None)
    else:
        return (0, "Invalid pin")


def open_door_request(request):
    """
    Validates open door request for a given request object.
    Returns tuple of (success_code, error_msg, flag)
    """
    success, msg = verify_correct_pin(request['device_id'], request['pin']);
    if (not success):   # Incorrect pin
        return (success, msg, None)
    else:
        return (success, None, REGISTERED_DEVICES[request['device_id']].flag)


def verify_attempt_timeout(device_id):
    """
    Verify that the requested device has not tried to guess password
    in last 59 sec.
    """
    if DANGEROUS_DEBUG_MODE:
        return True

    if device_id not in PASSWORD_ATTEMPTS:
        PASSWORD_ATTEMPTS[device_id] = time.time()
        return True
    else:
        lastAttempt = PASSWORD_ATTEMPTS[device_id]
        if (time.time() <= lastAttempt + 59):
            # Too soon
            return False
        else:
            PASSWORD_ATTEMPTS[device_id] = time.time()
            return True

def update_registered(device_id,new_pin):
    """"
    Update the registered widget file (and working memory) with new pins.
    Returns success code (0 or 1).
    """

    if device_id not in REGISTERED_DEVICES:
        # This device isn't registered
        return 0

    # Update memory
    REGISTERED_DEVICES[device_id].pin = new_pin

    # Write updated devices back to disk
    with open(REGISTERED_FILE, 'w') as f:
        for (_, device) in REGISTERED_DEVICES.items():
            print >> f, json.dumps(device.__dict__)

    return 1


def add_reg_request(device_key, device_id):
    """
    Add registration request to requested-widgets file
    """

    d = {'device_id': device_id,
         'device_key' : device_key,
         'flag' : DEFAULT_FLAG,
         'pin'  : DEFAULT_PIN}

    with open(REQUESTED_FILE, 'a+') as f:
        print >> f, json.dumps(d)

    return (1, None, None)

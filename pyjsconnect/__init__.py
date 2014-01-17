import json
from hashlib import md5
from urllib import urlencode


class JSConnectError(Exception):
    pass


def make_jsconnect_response(client_id,
                            secret,
                            request_data,
                            user_data,
                            hash_func=None):
    """
    Generate a response for a jsConnect request.
    """

    if hash_func is None:
        hash_func = md5

    try:

        if not request_data.get('client_id'):
            raise JSConnectError("The client_id parameter is missing.")

        if request_data['client_id'] != client_id:
            raise JSConnectError(
                "Unknown client %s." % request_data['client_id']
            )

        if not request_data.get('timestamp'):
            raise JSConnectError("The timestamp parameter is missing.")

    except JSConnectError, e:

        response = {
            'error': "invalid_request",
            'message': str(e),
        }

    else:

        # Remove null values
        for key in user_data:
            if user_data[key] is None:
                user_data[key] = ""

        # Calculate signature
        query_str = urlencode(user_data)
        signature = hash_func("%s%s" % (query_str, secret)).hexdigest()

        user_data.update({
            'client_id': client_id,
            'signature': signature,
        })

        response = user_data

    json_response = json.dumps(response)

    if request_data.get('callback'):
        json_response = "%s(%s)" % (request_data['callback'], json_response)
        mimetype = "application/javascript"
    else:
        mimetype = "application/json"

    return json_response, mimetype

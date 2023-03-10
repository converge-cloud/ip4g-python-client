"""Demonstrate a simple API call.

The purpose of this code is to demonstrate the ip4g OAuth2 flow and
basic API usage.

Please note that this implementation is for demonstration purposes
only.  In production code care should be taken to protect the refresh
token.

To execute this code in a Docker container, from the root directory:

  $ docker run -w /tmp/py -v$(pwd):/tmp/py -it --rm python bash
  # pip install -r requirements.txt
  # export ip4g_cloud_instance_id=<your-cloud-instance-id>
  # python examples/client.py

You will be prompted to visit the Google OAuth sign-in URL and enter
the supplied code.  Once completed, the client.py program will resume
within ten seconds.

"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import ip4g
from ip4g.rest import ApiException
from pprint import pprint
import time

# configuration parameters
cloud_instance_id = os.environ['ip4g_cloud_instance_id']
configuration = ip4g.Configuration()
configuration.host = os.environ.get('ip4g_endpoint',
    "https://service-broker-api.gpcloudtest.com")
configuration.debug = False


refresh_token_file = "/tmp/refresh_token"


def api_client(configuration):
    """Return an ApiClient."""
    client = ip4g.ApiClient(configuration=configuration)
    token = authenticate(client)
    return ip4g.ApiClient(configuration=configuration,
                                    header_name="Authorization",
                                    header_value=f"Bearer {token}")


def read_token():
    """Read the token from the refresh_token_file."""
    refresh_token = None
    try:
        tok_file = open(refresh_token_file, "r")
        refresh_token = tok_file.readline()
        tok_file.close()
    except:
        pass
    return refresh_token


def write_token(token):
    """Write a token to the refresh_token_file."""
    tok_file = open(refresh_token_file, "w")
    tok_file.write(token)
    tok_file.close()


def authenticate(client):
    """Return a valid bearer token."""
    auth_api = ip4g.AuthenticationApi(client)
    refresh_token = read_token()
    try:
        body = ip4g.TokenRequest(refresh_token=refresh_token)
        token = auth_api.service_broker_auth_token_post(body)
    except:
        try:
            device = auth_api.service_broker_auth_device_code_post()
        except ApiException as e:
            pprint("Exception: %s\n" % e)

        print("Visit ", device.verification_url)
        print("Code: ", device.user_code)
        token = poll_for_device_code(auth_api, device)

    return token.access_token


def poll_for_device_code(a, device_code):
    """Poll until a device code is returned or expires time reached."""
    token = None
    while token is None and device_code.expires_in > 0:
        time.sleep(device_code.interval)
        new_expires = device_code.expires_in - device_code.interval
        device_code.expires_in = new_expires
        body = ip4g.Body(device_code.device_code)
        try:
            token = a.service_broker_auth_device_token_post(body)
            write_token(token.refresh_token)
        except:
            pass
    return token


if __name__ == '__main__':
    """Create a new network."""
    client = api_client(configuration)
    api = ip4g.PCloudNetworksApi(client)
    network_name = "newNetwork"
    cidr = "10.1.1.0/24"
    dns = "8.8.8.8"
    gateway = "10.1.1.1"
    ip_range = [{"startingIPAddress": '10.1.1.4',
                 "endingIPAddress": '10.1.1.254'}]
    body = ip4g.NetworkCreate(name='newNetwork',\
                              cidr='10.1.1.0/24',\
                              dns_servers=['8.8.8.8'],\
                              gateway='10.1.1.1',\
                              ip_address_ranges = [{"startingIPAddress": '10.1.1.4',
                                                    "endingIPAddress": '10.1.1.254'}])
    try:
        api_response = \
            api.pcloud_networks_post(cloud_instance_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception: %s\n" % e)

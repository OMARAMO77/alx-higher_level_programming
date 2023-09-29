#!/bin/bash
# Get request to the URL and causes the server to respond with a message containing You got me!, in the body of the response
curl -s -X PUT -H "User-Agent: You got me!" 0.0.0.0:5000/catch_me

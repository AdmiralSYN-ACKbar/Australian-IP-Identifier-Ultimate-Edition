<h3>AUSTRALIAN IP IDENTIFIER: ULTIMATE EDITION</h3>

<i>Requirements: Python3 with Request module installed</i>

Inspired by the most popular challenge of the Fall 2022 National Cyber League Team Competition, this script will identify all IP addresses possible in a number string and identify which ones are Australian. The script will also return the organization name registered to Australian IPs.

The vast majority of this code is "borrowed" from Ankitrai01's program to return all valid IP addreses from a string (https://tinyurl.com/2tfvf9va). Thanks Aniktrai01!
After valid IPs are identified, they are submitted to ipapi.co for geolocation and organizational identification (if Australian). There is an IPAPI free-tier limit of 1000 checks per month, so ration accordingly!

![screenshot](https://github.com/AdmiralSYN-ACKbar/Australian-IP-Identifier-Ultimate-Edition/blob/main/screenshot.png "Example Output")

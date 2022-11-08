#!/usr/bin/env python

"""
AUSTRALIAN IP IDENTIFIER: ULTIMATE EDITION
By Admiral SYN-ACKBar

Inspired by the most popular challenge of the Fall 2022 National Cyber League Team Competition, this script will identify all IP addresses possible in a number string and identify which ones are Australian. The script will also return the organization name registered to Australian IPs.

The vast majority of this code is "borrowed" from Ankitrai01's program to return all valid IP addreses from a string (https://tinyurl.com/2tfvf9va). Thanks Aniktrai01!
After valid IPs are identified, they are submitted to ipapi.co for geolocation and organizational identification (if Australian). There is an IPAPI free-tier limit of 1000 checks per month, so ration accordingly!
"""

from requests import get

def GetAllValidIpAddress(result, givenString, index, count, ipAddress) :

	# If index greater than givenString size and we have four blocks
	if (len(givenString) == index and count == 4) :

		# Remove the last dot
		ipAddress.pop();

		# Add ip-address to the results
		result.append(ipAddress);
		return;

	# To add one index to ip-address
	if (len(givenString) < index + 1) :
		return;

	# Select one digit and call the	same function for other blocks
	ipAddress = (ipAddress + givenString[index : index + 1] + ['.']);
	
	GetAllValidIpAddress(result, givenString, index + 1, count + 1, ipAddress);

	# Backtrack to generate another possible ip address so we remove two indexes (one for the digit and other for the dot) from the end
	ipAddress = ipAddress[:-2];

	# Select two consecutive digits and call the same function for other blocks
	if (len(givenString) < index + 2 or givenString[index] == '0') :
		return;
		
	ipAddress = ipAddress + givenString[index:index + 2] + ['.'];
	GetAllValidIpAddress(result, givenString, index + 2, count + 1, ipAddress);

	# Backtrack to generate another possible ip address so we remove three indexes from the end
	ipAddress = ipAddress[:-3];

	# Select three consecutive digits and call the same function for other blocks
	if (len(givenString)< index + 3 or
		int("".join(givenString[index:index + 3])) > 255) :
		return;
	ipAddress += givenString[index:index + 3] + ['.'];
	GetAllValidIpAddress(result, givenString, index + 3, count + 1, ipAddress);

	# Backtrack to generate another possible ip address and remove four indexes from the end
	ipAddress = ipAddress[:-4];

if __name__ == "__main__" :
	givenString = list(input("Sauron's forces are on their way to Australia, but we don't know who they're targeting! \nOur spy network has intercepted a secret number. Quickly, enter it into the console!\nSecret Number: "));
	result = [] ; # Fill result with all valid ip-addresses
	numIPs = 0;
	ausIPs = 0;
	GetAllValidIpAddress(result, givenString, 0, 0, []);
	
	# Print IPs and return results for Australia
	print ("\nMany Bothans died to bring us this information:\n"); #Lest we forget
	for i in range(len(result)) :
		numIPs += 1;
		joinedIP = "".join(result[i]);
		countryCode = get(f"https://ipapi.co/{joinedIP}/country").text;	#Get country code of IP
		if countryCode == 'AU':
			org = get(f"https://ipapi.co/{joinedIP}/org").text; #Get organization if country code is Australia
			message = f"AUSTRALIAN IP DETECTED! Our spy network tell us that it belongs to {org}"
			ausIPs += 1;
		else:
			message = "NOT AN AUSTRALIAN IP :-("
		print(f"{joinedIP}", f"{message}");
	if (numIPs > 0 and ausIPs == 0):
		print("\nNo Australian IP addresses found! Have you tried a reverse phone number search?")
	if numIPs == 0 :
		print("No valid IP addresses found! Have you tried a reverse phone number search?")
				
# Special thanks to Ankitrai01, IPAPI.com and YOU

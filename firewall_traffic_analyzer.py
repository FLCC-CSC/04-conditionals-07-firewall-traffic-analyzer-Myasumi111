# FILE NAME - firewall_traffic_analyzer.py

# NAME: Makiko Michelle Yasumi
# DATE: October 2, 2025
# BRIEF DESCRIPTION:  This program inputs IP address and data transfer size and outputs the risk assessment.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    analyzer()

def analyzer():
    print("=== Network Traffic Security Analyzer ===")
    print()

    port = int(input("Enter the port number (e.g., 80, 22, 443, 3389): "))
    size = int(input("Enter the data transfer size in megabytes (MB): "))
    if port == 22 and size == 100:
        risk = "HIGH RISK: Potential unauthorized remote access detected!"
    elif port == 3389 and size == 100:
         risk = "HIGH RISK: Potential unauthorized remote access detected!"       
    elif port == 22 and size > 500:
        risk = "HIGH RISK: Potential unauthorized remote access detected!"
    elif port == 80 and size > 100:
        risk = "MEDIUM RISK: Large unencrypted data transfer detected."
    elif port == 443:
        risk = "LOW RISK: Secure encrypted transfer detected."
    else:
        risk = "UNKNOWN: Unrecognized traffic pattern."

    print()
    print("FIREWALL LOG:")
    print(f"Port: {port}, Transfer Size: {size} MB")

    print(f"Risk Assessment: {risk}")

main()

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 80
Enter the data transfer size in megabytes (MB): 120

FIREWALL LOG:
Port: 80, Transfer Size: 120 MB
Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 22
Enter the data transfer size in megabytes (MB): 1200

FIREWALL LOG:
Port: 22, Transfer Size: 1200 MB
Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 443
Enter the data transfer size in megabytes (MB): 1024

FIREWALL LOG:
Port: 443, Transfer Size: 1024 MB
Risk Assessment: LOW RISK: Secure encrypted transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 1725
Enter the data transfer size in megabytes (MB): 234567

FIREWALL LOG:
Port: 1725, Transfer Size: 234567 MB
Risk Assessment: UNKNOWN: Unrecognized traffic pattern.
------------------------
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you get tripped up using the `or` or `and` operators? If so, how?

No, I didn't.

'''

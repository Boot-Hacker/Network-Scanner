# Network Scanning Tool

This is a basic network scanning tool using python-3.9. 
We can use this tool to find out how many system's are connected and there corrosponding ip's and MAC address. 

DETAILS OF USES LIBARIES : 

 1.Scapy : Scapy is a powerful Python-based interactive packet manipulation program and library.
           It is able to forge or decode packets of a wide number of protocols, send them on the wire, capture them, store or read them using pcap files, match
           requests and replies, and much more. It is designed to allow fast packet prototyping by using default values that work.
           official link :  https://pypi.org/project/scapy/
           => For executing scapy module we need root priviledge that's why we use sudo before execution.
  
  **
Steps To Follow **
---------------------------------------------------------------------

-> Install all necessary libary file into your system.[scapy]

-> Download netscanner.py

-> Go to the path where download ".py" file.

-> chmod +x netscanner.py{Linux}

-> command : "sudo python3 netscanner.py -h"


**Example :**
---------------------------------------------------------------------
-> Get help for arguments to execute command.

      command : sudo python3 netscanner.py -h
   
   ![Screenshot_2022-06-25_09_41_01](https://user-images.githubusercontent.com/87462515/175778535-ebbf924d-b40a-4991-8169-efd7a55cd6dd.png)

      command : sudo python3 netscanner.py 192.168.228.0/24
 
 ![Screenshot_2022-06-25_09_46_18](https://user-images.githubusercontent.com/87462515/175778717-459009f6-a812-4e0f-bf77-57e4a27d0ddd.png)

      
   

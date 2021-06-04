import random
from random import randint
from random import choice

i = 0
score = 0

list1 = [
    "\nWhat service uses port 21?\n(a) FTP [UDP]\n(b) POP3 [TCP]\n(c) TFTP [UDP]\n\n",
    "\nWhat service uses port 22?\n(a)SSH\n(b) LDAP [SSL/TLS]\n(c) HTTP [TCP]\n\n",
    "\nWhat service uses port 23?\n(a) SNMP|tcp/ip\n(b) Telnet|tcp/udp\n(c) syslog|udp\n\n",
    "\nWhat service uses port 25?\n(a) SMTP [TCP]\n(b) Syslog [UDP]\n(c)\n PPTP [TCP/UDP]\n\n",
    "\nWhat service uses port 53?\n(a) TFTP [UDP]\n(b) DNS [TCP/UDP]\n(c) LDAP [TCP/UDP]\n\n",
    "\nWhat service uses port 69?\n(a) Telnet [TCP/UDP]\n(b) PPTP [TCP/UDP](c) TFTP [UDP]\n\n",
    "\nWhat service uses port 80?\n(a) DNS [TCP/UDP]\n(b) HTTPS [SSL/TLS]\n(c) HTTP [TCP]\n\n",
    "\nWhat service uses port 88?\n(a) Kerberos [TCP/UDP]\n(b) SMB [TCP]\n(c) Ms-sql-S [TCP]\n\n",
    "\nWhat service uses port 110?\n(a) POP3 [TCP]\n(b) NNTP [UDP]\n(c) SMTP [SSL/TLS]\n\n",
    "\nWhat service uses port 119?\n(a) TFTP [UDP]\n(b) NNTP [UDP]\n(c) PTP [TCP/UDP]\n\n",
    "\nWhat service uses port 135?\n(a) RPC/Dcom-scm [TCP/UDP]\n(b) NetBios [TCP/UDP]\n(c) SNMP [UDP]\n\n",
    "\nWhat's the port range of Netbios services?\n(a) 53-57\n(b) 137-139\n(c) 134-137\n\n",
    "\nWhat service uses port 143?\n(a) Imaps\n(b) SNMP Trap [TCP/UDP]\n(c) RADIUS [UDP]\n\n",
    "\nWhat service uses port 161?\n(a) SNMP [UDP]\n(b) NNTP [UDP]\n(c) SMB [TCP]\n\n",
    "\nWhat service uses port 162?\n(a) FTPS [TCP]\n(b) SNMP Trap [TCP/UDP]\n(c) Kerberos [TCP/UDP]\n\n",
    "\nWhat service uses port 389?\n(a) SMTP [TCP]\n(b) DNS [TCP/UDP]\n(c) LDAP [TCP/UDP]\n\n",
    "\nWhat service uses port 443?\n(a) HTTPS [SSL/TLS]\n(b) TFTP [UDP]\n(c) HTTP [TCP]\n\n",
    "\nWhat service uses port 445?\n(a) SMB [TCP]\n(b) RADIUS [UDP]\n(c) IMAP4 [SSL/TLS]\n\n",
    "\nWhat's the port range of SMTP services?\n(a) 465-587\n(b)442-455\n(c) 460-468\n\n",
    "\nWhat service uses port 514?\n(a) DNS [TCP/UDP]\n(b) NetBios [TCP/UDP]\n(c) Syslog [UDP]\n\n",
    "\nWhat service uses port 636?\n(a) LDAP [SSL/TLS]\n(b) Idaps\n(c) PPTP [TCP/UDP]\n\n",
    "\nWhat service uses port 860?\n(a) RADIUS [UDP]\n(b) ISCSI[TCP]\n(c) Imap [TCP]\n\n",
    "\nWhat's the port range of FTPS services?\n(a) 689/990\n(b)640-657\n(c) 460-505\n\n",
    "\nWhat service uses port 993?\n(a) IMAP4 [SSL/TLS]\n(b) Kerberos [TCP/UDP]\n(c) LDAP [SSL/TLS]\n\n",
    "\nWhat service uses port 995?\n(a) TFTP [UDP]\n(b) POP3\n(c) Syslog [UDP]\n\n",
    "\nWhat service uses port 1433?\n(a) SNMP [UDP]\n(b) SMB [TCP]\n(c) Ms-sql-S [TCP]\n\n",
    "\nWhat's the port range of RADIUS services?\n(a) 1465-1587\n(b)1672-1673\n(c) 1645-1646\n\n",
    "\nWhat service uses port 1701?\n(a) L2TP\n(b) TFTP [UDP]\n(c) PPTP [TCP/UDP]\n\n",
    "\nWhat service uses port 1723?\n(a) NNTP [TCP/UDP]\n(b) PPTP [TCP/UDP]\n(c) POP3 [TCP/UDP]\n\n",
    "\nWhat service uses port 3225?\n(a) FCIP\n(b) NNTP [UDP]\n(c) Ms-sql-S [TCP]\n\n",
    "\nWhat service uses port 3260?\n(a) NetBios [TCP/UDP]\n(b) PPTP [TCP'UDP]\n(c) iSCSI[TCP]\n\n",
    "\nWhat service uses port 3389?\n(a) SNMP [UDP]\n(b) FTPS [TCP]\n(c)RDP [TCP/UDP]\n\n",
    "\nWhat service uses port 3868?\n(a) SSH\n(b) TFTP [UDP]\n(c) Diameter [TCP/UDP]\n\n",
    "\nWhat service uses port 6514?\n(a) Syslog [UDP]\n(b) Syslog [TLS]\n(c) Syslog [TCP]\n\n"
]

list2 = [
    "a", "a", "b", "a", "b", "c", "c", "a", "a", "b", "a", "b", "a", "a", "b", "c", "a", "a", "a","c", "b", "b","a", "a", "b", "c", "c", "a", "b", "a", "c", "c", "c", "c"
]

print("Welcome!")
print("\nTry to guess the correct service associated with the presented network port.")
print("\nPlease don't answer with UPPER CASE letters. Input validation isn't implemented.")


while i < 10:
    answer = dict(zip(list1,list2))
    x = random.randint(0,len(list1)-1)
    y = list1[x]
    print(y)

    user_answer = input("Your Answer: ")
    if user_answer == answer[y]:
        score += 1
        i += 1
        print("Right on!")
        print("Score: ", score, "/ 10")
        print()
        print("#########################################")
    else:
        i += 1
        print("Incorrect.")
        print("Score: ", score, "/ 10")
        print()
        print("#########################################")
        
if (score < 5):
    print("Ok, champ. You need to study more.")
    print("You got merely ", score, " /10 questions right.")

elif (score == 6 or score <8):
    print("Well done. You've got ", score, " / 10 questions right. Good, but you can do better.")

else :
    print()
    print("Bloody well done!")
    print("You managed to answer ", score, "/ 10 questions correctly. You are amazing!")
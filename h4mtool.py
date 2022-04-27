#All Rights reserved to https://github.com/SuccessCod3
#if you found some bug/error please report it in my discord <3
#https://discord.gg/BaStk83sPu

import os
import colorama
import platform
from colorama import Fore
systemdet = platform.system()

errormsg = "Something is wrong!, if you think it is a error please report it on discord"
title = Fore.RED+"""                                                                                      
                        888    888     d8888  888b     d888 88888888888                888 
                        888    888    d8P888  8888b   d8888     888                    888 
                        888    888   d8P 888  88888b.d88888     888                    888 
                        8888888888  d8P  888  888Y88888P888     888   .d88b.   .d88b.  888 
                        888    888 d88   888  888 Y888P 888     888  d88""88b d88""88b 888 
                        888    888 8888888888 888  Y8P  888     888  888  888 888  888 888 
                        888    888       888  888   "   888     888  Y88..88P Y88..88P 888 
                        888    888       888  888       888     888   "Y88P"   "Y88P"  888"""


menu = Fore.WHITE+"""
     ╔═════════════════════════════════════════════╦═══════════════════════════════════════════════════╗
     ║                Executor                     ║                    Function                       ║
     ║                                             ║                                                   ║
     ║═════════════════════════════════════════════║═══════════════════════════════════════════════════║ 
     ║  scan (nmap scan)                           ║    use nmap to scan a port ip/range               ║
     ║  qubo (just for minecraft ports)            ║    use qubo scanner to scan ip/range (mc ports)   ║
     ║  subdomains (Avaible in v1.x)               ║    scan a subdomain list in a domain              ║
     ║  poisoning (Avaible in v1.x)                ║    Create a proxy connection that redirects to a  ║
     ║                                             ║    server and captures commands                   ║
     ║  clear                                      ║    Clear screen                                   ║
     ╚═════════════════════════════════════════════╩═══════════════════════════════════════════════════╝
                                    https://es.namemc.com/ipforwarding
                                      https://github.com/SuccessCod3                              """

menuscan = Fore.WHITE+"""
     ╔═════════════════════════════════════════════╦═══════════════════════════════════════════════════╗
     ║                Executor                     ║                    Function                       ║
     ║                                             ║                                                   ║
     ║═════════════════════════════════════════════║═══════════════════════════════════════════════════║ 
     ║  fast: (1-100,25565-25600)                  ║    Fast scan - ranges/ip                          ║
     ║  medium: (1-10000,25000-30000)              ║    medium scan - not recommended for ranges       ║
     ║  slow: (1-65535)                            ║    slow scan - not recommended for ranges         ║
     ║  custom                                     ║    custom scan - you select port range            ║
     ║                                             ║                                                   ║
     ║  clear                                      ║    Clear screen                                   ║
     ╚═════════════════════════════════════════════╩═══════════════════════════════════════════════════╝
                                    https://es.namemc.com/ipforwarding
                                      https://github.com/SuccessCod3                              """

def clear():
    if systemdet=="Linux":
        os.system("clear")
    else:
        os.system("cls")

def main():
    if systemdet=="Linux":
        os.system("clear")
    else:
        os.system("cls")

    print(title)
    print(menu)
    cmd = input('Select your option: ')

    if cmd=="scan":
        clear()
        scan()
        pass
    elif cmd=="qubo":
        clear()
        qubo()
        pass
    elif cmd=="clear":
        clear()
        print(menu)
        pass
    else:
        main()
        pass

def scan():
    print(title)
    print(menuscan)
    cmd = input('Select your option: ')
    if cmd=="fast":
        ipz = input('Insert ip: ')
        if systemdet=="Linux":
            os.system("mkdir output")
            os.system("touch output/"+ipz+"_fast.txt")
            print(Fore.RED+"WARNING"+Fore.WHITE+": Scan will be printed in output/"+ipz+"_fast.txt")
            os.system("nmap -p 1-100,25565-25600 -T4 -A --open -v -Pn "+ipz+" >>output/"+ipz+"_fast.txt")
            exitit = input('Do you want continue?: <y/n> ')
            if exitit=="y":
                main()
            elif exitit=="n":
                exit()
            else:
                main()
            pass
        else:
            print(Fore.RED+"WARNING"+Fore.WHITE+": Scan will be printed in "+ipz+"_output_fast.txt")
            f = open(ipz+"_output_fast.txt", "w+")
            f.close()
            os.system("nmap -p 1-100,25565-25600 -T4 -A --open -v -Pn "+ipz+" >>"+ipz+"_output_fast.txt")
            exitit = input('Do you want continue?: <y/n> ')
            if exitit=="y":
                main()
            elif exitit=="n":
                exit()
            else:
                main()
            pass
            pass
        pass
    elif cmd=="medium":
        ipz = input('Insert ip: ')
        if systemdet=="Linux":
            os.system("mkdir output")
            os.system("touch output/"+ipz+"_medium.txt")
            print(Fore.RED+"WARNING"+Fore.WHITE+": Scan will be printed in output/"+ipz+"_medium.txt")
            os.system("nmap -p 1-10000,25000-30000 -T4 -A --open -v -Pn "+ipz+" >>output/"+ipz+"_medium.txt")
            exitit = input('Do you want continue?: <y/n> ')
            if exitit=="y":
                main()
            elif exitit=="n":
                exit()
            else:
                main()
            pass
        else:
            print(Fore.RED+"WARNING"+Fore.WHITE+": Scan will be printed in "+ipz+"_output_medium.txt")
            f = open(ipz+"_output_medium.txt", "w+")
            f.close()
            os.system("nmap -p 1-10000,25000-30000 -T4 -A --open -v -Pn "+ipz+" >>"+ipz+"_output_medium.txt")
            exitit = input('Do you want continue?: <y/n> ')
            if exitit=="y":
                main()
            elif exitit=="n":
                exit()
            else:
                main()
            pass
            pass
        pass
    elif cmd=="slow":
        ipz = input('Insert ip: ')
        if systemdet=="Linux":
            os.system("mkdir output")
            os.system("touch output/"+ipz+"_slow.txt")
            print(Fore.RED+"WARNING"+Fore.WHITE+": Scan will be printed in output/"+ipz+"_slow.txt")
            os.system("nmap -p 1-10000,25000-30000 -T4 -A --open -v -Pn "+ipz+" >>output/"+ipz+"_slow.txt")
            exitit = input('Do you want continue?: <y/n> ')
            if exitit=="y":
                main()
            elif exitit=="n":
                exit()
            else:
                main()
            pass
        else:
            print(Fore.RED+"WARNING"+Fore.WHITE+": Scan will be printed in "+ipz+"_output_slow.txt")
            f = open(ipz+"_output_slow.txt", "w+")
            f.close()
            os.system("nmap -p 1-10000,25000-30000 -T4 -A --open -v -Pn "+ipz+" >>"+ipz+"_output_slow.txt")
            exitit = input('Do you want continue?: <y/n> ')
            if exitit=="y":
                main()
            elif exitit=="n":
                exit()
            else:
                main()
            pass
            pass
        pass
    elif cmd=="custom":
        ipz = input('Insert ip: ')
        portr = input('Insert ports: ')
        if systemdet=="Linux":
            os.system("mkdir output")
            os.system("touch output/"+ipz+"_slow.txt")
            print(Fore.RED+"WARNING"+Fore.WHITE+": Scan will be printed in output/"+ipz+"_slow.txt")
            os.system("nmap -p "+portr+" -T4 -A --open -v -Pn "+ipz+" >>output/"+ipz+"_slow.txt")
            exitit = input('Do you want continue?: <y/n> ')
            if exitit=="y":
                main()
            elif exitit=="n":
                exit()
            else:
                main()
            pass
        else:
            print(Fore.RED+"WARNING"+Fore.WHITE+": Scan will be printed in "+ipz+"_output_slow.txt")
            f = open(ipz+"_output_slow.txt", "w+")
            f.close()
            os.system("nmap -p "+portr+" -T4 -A --open -v -Pn "+ipz+" >>"+ipz+"_output_slow.txt")
            exitit = input('Do you want continue?: <y/n> ')
            if exitit=="y":
                main()
                pass
            elif exitit=="n":
                exit()
                pass
            else:
                main()
                pass
            pass
        pass
    else:
        main()
        pass


def qubo():
    print(Fore.RED+"WARNING"+Fore.WHITE+": quboscanner just work with minecraft ports")
    quboopt = input('Do you have qubo.jar into h4mtool folder?: <y/n> ')
    if quboopt=="y":
        iprange = input('Insert ip/range: ')
        portrange = input('Insert ports range: ')
        timeout = input('Insert ti: ')
        threats = input('Insert th: ')
        os.system("java -Dfile.encoding=UTF-8 -jar qubo.jar -noping -ports "+portrange+" -th "+threats+" -ti "+timeout+" -all -range "+iprange)
        pass
    elif quboopt=="n":
        main()
        pass
    else:
        main()
        pass

def subdomains():
    print("Not avaible on this version")

def poisoning():
    print("will be added in the future")

main()

from os import system 
from time import sleep

blue = "\033[94;1m"
red = "\033[91;1m"

def main():
    banner = """
             _                __     _ __ 
     _    __(_)__ __ __ ___  / /__  (_) /_
    | |/|/ / / _ \\ \ // _ \/ / _ \/ / __/
    |__,__/_/_//_/_\_\/ .__/_/\___/_/\__/ 
                     /_/                                                  
    [+] Windows Exploitation search

                                      "the quieter you become,
                                    the more you are able to hear"
    """
    tipos = """
    [1] DoS
    [2] Local
    [3] Remote code execution
    [4] Shellcodes/rootkits

    """
    print(red + banner)
    print(blue + "[+] tipo de exploit")
    print(blue + tipos)
    typer = int(input(">>> "))
    print(blue + "[+] Service/Protocolo")
    service = str(input(">>> "))
    if typer == 1:
            print(red + "Exploits: \r\n")
            system("searchsploit Dos Microsoft {}".format(service))
            update()
    elif typer == 2:
            print(red + "Exploits: \r\n")
            system("searchsploit Local Microsoft {}".format(service))
            update()
    elif typer == 3:
            print(red + "Exploits: \r\n")
            system("searchsploit Remote Microsoft {}".format(service))
            update()
    elif typer == 4:
            print(red + "Exploits: \r\n")
            system("searchsploit shellcode Microsoft")
            system("searchsploit rootkit Microsoft")
            update()
    else:
        print("[+] Invalido argumento! ")
        update()

def update():
    quest = input(blue + "\r\natualizar-Base-de-Exploits[Y/N]: ")

    if quest == "n" or quest == "N":
        print(blue + "[+] Adeus  meu amigo:)")
        exit()
    elif quest == "y" or quest == "Y":
        print(blue + "[+] Atualizando base de exploits...")
        sleep(1.80)
        system("searchsploit -u")
    else:
        exit()

if __name__ == "__main__":
    main()
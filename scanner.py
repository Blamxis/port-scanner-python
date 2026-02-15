import socket
import threading
from colorama import Fore, Style, init

# J'initialise colorama pour que les couleurs fonctionnent bien sous Windows.
init()

# Dictionnaire personnalisé pour reconnaître les services non standards.
# Ça rend l'affichage beaucoup plus propre.
CUSTOM_SERVICES = {
    135: "EPMAP (Windows RPC)",
    445: "Microsoft-DS (SMB)",
    3306: "MySQL",
    3590: "Windows RPC",
    5040: "Windows Push Notification",
    5432: "PostgreSQL",
    5433: "PostgreSQL (alt)",
    7680: "Windows Delivery Optimization",
    11434: "Ollama API"
}

def print_logo():
    # Logo ASCII personnalisé pour donner une identité à l'outil.
    logo = f"""
{Fore.CYAN}
 _   _            _        _____           _ 
| | | | __ _  ___| | __   |_   _|__   ___ | |
| |_| |/ _` |/ __| |/ /_____| |/ _ \\ / _ \\| |
|  _  | (_| | (__|   <_____| | (_) | (_) | |
|_| |_|\\__,_|\\___|_|\\_\\    |_|\\___/ \\___/|_|
                HACKTOOL 1.0
{Style.RESET_ALL}
"""
    print(logo)

def get_service_name(port):
    # Je vérifie d'abord dans mon dictionnaire personnalisé.
    if port in CUSTOM_SERVICES:
        return CUSTOM_SERVICES[port]

    # Sinon je demande à Python (services officiels IANA).
    try:
        return socket.getservbyport(port)
    except:
        return "Service inconnu"

def scan_port(host, port, open_ports):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        s.connect((host, port))
        service = get_service_name(port)

        # J'affiche en vert les ports ouverts.
        print(f"{Fore.GREEN}[+] Port ouvert : {port} ({service}){Style.RESET_ALL}")

        # Je compte les ports ouverts.
        open_ports.append(port)

    except:
        pass
    finally:
        s.close()

def scan_range(host, start_port, end_port):
    print(f"\n{Fore.YELLOW}Scan en cours sur {host} ({start_port} → {end_port})...{Style.RESET_ALL}\n")

    threads = []
    total_ports = end_port - start_port + 1
    scanned = 0
    open_ports = []  # Liste pour compter les ports ouverts

    for port in range(start_port, end_port + 1):
        scanned += 1

        # Affichage de la progression
        print(f"{Fore.BLUE}Scanning port {scanned}/{total_ports}...{Style.RESET_ALL}", end="\r")

        t = threading.Thread(target=scan_port, args=(host, port, open_ports))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"\n\n{Fore.MAGENTA}Scan terminé.{Style.RESET_ALL}")

    # Résumé final
    if len(open_ports) == 0:
        print(f"{Fore.RED}Aucun port ouvert trouvé.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}Total ports ouverts : {len(open_ports)}{Style.RESET_ALL}")

def main():
    print_logo()

    # Menu interactif
    print(f"{Fore.YELLOW}=== MENU ==={Style.RESET_ALL}")
    print(f"{Fore.CYAN}1 - Scan rapide (1 → 1024){Style.RESET_ALL}")
    print(f"{Fore.CYAN}2 - Scan moyen (1 → 20000){Style.RESET_ALL}")
    print(f"{Fore.CYAN}3 - Scan complet (1 → 65535){Style.RESET_ALL}")
    print(f"{Fore.CYAN}4 - Scan personnalisé (range){Style.RESET_ALL}")
    print(f"{Fore.CYAN}5 - Scan d’un seul port{Style.RESET_ALL}")

    choice = input(f"\n{Fore.YELLOW}Votre choix : {Style.RESET_ALL}")
    host = input(f"{Fore.CYAN}Adresse IP cible : {Style.RESET_ALL}")

    if choice == "1":
        scan_range(host, 1, 1024)

    elif choice == "2":
        scan_range(host, 1, 20000)

    elif choice == "3":
        scan_range(host, 1, 65535)

    elif choice == "4":
        start_port = int(input("Port de début : "))
        end_port = int(input("Port de fin : "))
        scan_range(host, start_port, end_port)

    elif choice == "5":
        port = int(input("Port à scanner : "))
        scan_range(host, port, port)

    else:
        print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()

import os
import subprocess
import logging

# Configure logging
logging.basicConfig(
    filename=os.path.expanduser("~/security_tools.log"), level=logging.INFO
)


# Define color codes for formatted output in the terminal
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[0;36m"
MAGENTA = "\033[0;35m"
NC = "\033[0m"  # No Color (reset to default)


def display_banner():
    """Display a colorful banner for the tool."""
    banner = (
        f"{CYAN}========================{NC}\n"
        + f"{GREEN}  SecureInsight v1.0  {NC}\n"
        + f"{CYAN}========================{NC}\n"
        + f"{MAGENTA}  Author: Mohamed Gebril  {NC}\n"
    )
    print(banner)


def display_main_menu():
    """Display the main menu for the security tools."""
    print(f"{GREEN}Main Menu:{NC}")
    print(f"{YELLOW}1) Penetration Testing Tools{NC}")
    print(f"{YELLOW}2) Secure Code Review Tools{NC}")
    print(f"{YELLOW}3) Exit{NC}")


def display_penetration_testing_tools_menu():
    """Display the menu for penetration testing tools."""
    print(f"{GREEN}Penetration Testing Tools:{NC}")
    print(f"{YELLOW}1) nmap: Network exploration and security auditing tool{NC}")
    print(f"{YELLOW}2) nikto: Web server scanner{NC}")
    print(f"{YELLOW}3) LEGION: Automated web application security scanner{NC}")
    print(f"{YELLOW}4) OWASP ZAP: Web application security testing tool{NC}")
    print(f"{YELLOW}5) John the Ripper: Password cracking tool{NC}")
    print(f"{YELLOW}6) SQLmap: SQL Injection and database takeover tool{NC}")
    print(f"{YELLOW}7) Metasploit Framework: Penetration testing framework{NC}")
    print(f"{YELLOW}8) Go Back{NC}")


def run_tool(command):
    """Run a shell command and handle errors."""
    try:
        subprocess.run(command, check=True)
        logging.info(f"Executed command: {' '.join(command)}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing command: {e}")
        print(f"{RED}An error occurred: {e}{NC}")


def run_nmap():
    """Run nmap for network exploration and auditing."""
    url = input(f"{YELLOW}Enter URL or IP address to scan: {NC}")
    output_to_file = input(f"{YELLOW}Output to file? (y/n): {NC}")
    output_file = f"nmap_output_{url}.txt" if output_to_file.lower() == "y" else None
    command = ["nmap"]
    if output_file:
        command += ["-oN", output_file]
    command.append(url)
    run_tool(command)


def run_nikto():
    """Run nikto for web server scanning."""
    url = input(
        f"{YELLOW}Enter URL and port to scan (Example: http://localhost:4200): {NC}"
    )
    output_to_file = input(f"{YELLOW}Output to file? (y/n): {NC}")
    if output_to_file.lower() == "y":
        format = input(f"{YELLOW}Enter the output format (txt, html, xml): {NC}")
        command = [
            "nikto",
            "-h",
            url,
            "-o",
            f"nikto_output_{url}.{format}",
            "-Format",
            format,
        ]
    else:
        command = ["nikto", "-h", url]
    run_tool(command)


def run_legion():
    """Run LEGION for web application security scanning."""
    subprocess.run(["sudo", "legion"])


def run_owasp_zap():
    """Run OWASP ZAP for web application security testing."""
    url = input(
        f"{YELLOW}Enter URL and port to scan (Example: http://localhost:4200): {NC}"
    )
    command = ["zap", "-quickurl", url]
    run_tool(command)


def run_john():
    """Run John the Ripper for password cracking."""
    password_file = input(f"{YELLOW}Enter the path to the password file to crack: {NC}")
    output_to_file = input(f"{YELLOW}Output to file? (y/n): {NC}")
    output_file = (
        f"john_output_{password_file}.txt" if output_to_file.lower() == "y" else None
    )
    command = ["john", password_file]
    if output_file:
        command += ["--session", output_file]
    run_tool(command)


def run_sqlmap():
    """Run SQLmap for SQL injection testing."""
    url = input(
        f"{YELLOW}Enter URL to scan (e.g., http://example.com/vuln.php?id=1): {NC}"
    )
    output_to_file = input(f"{YELLOW}Output to file? (y/n): {NC}")
    output_file = f"sqlmap_output_{url}.txt" if output_to_file.lower() == "y" else None
    command = ["sqlmap", "-u", url]
    if output_file:
        command += ["--output-dir", output_file]
    run_tool(command)


def run_metasploit():
    """Run Metasploit Framework for penetration testing."""
    output_to_file = input(f"{YELLOW}Output to file? (y/n): {NC}")
    if output_to_file.lower() == "y":
        subprocess.run(["sudo", "msfconsole", "|", "tee", "metasploit_output.txt"])
    else:
        subprocess.run(["sudo", "msfconsole"])


def handle_penetration_testing_tools():
    """Handle the penetration testing tools menu."""
    while True:
        display_penetration_testing_tools_menu()
        choice = input(f"{YELLOW}Choose an option: {NC}")
        if choice == "1":
            run_nmap()
        elif choice == "2":
            run_nikto()
        elif choice == "3":
            run_legion()
        elif choice == "4":
            run_owasp_zap()
        elif choice == "5":
            run_john()
        elif choice == "6":
            run_sqlmap()
        elif choice == "7":
            run_metasploit()
        elif choice == "8":
            break
        else:
            print(f"{RED}Invalid choice, please try again.{NC}")


def display_secure_code_review_tools_menu():
    """Display the menu for secure code review tools."""
    print(f"{GREEN}Secure Code Review Tools:{NC}")
    print(f"{YELLOW}1) osv-scanner: Scan a directory for vulnerabilities{NC}")
    print(f"{YELLOW}2) snyk: Test code locally or monitor for vulnerabilities{NC}")
    print(
        f"{YELLOW}3) brakeman: Scan a Ruby on Rails application for security vulnerabilities{NC}"
    )
    print(f"{YELLOW}4) Go Back{NC}")


def run_osv_scanner():
    """Run osv-scanner to detect vulnerabilities in open source projects."""
    directory = input(f"{YELLOW}Enter directory to scan: {NC}")
    output_to_file = input(f"{YELLOW}Output to file? (y/n): {NC}")
    output_file = (
        f"osv_scanner_output_{directory}.txt" if output_to_file.lower() == "y" else None
    )
    command = ["osv-scanner", "--recursive", directory]
    if output_file:
        command += ["--output", output_file]
    run_tool(command)


def run_snyk():
    """Run snyk to test code for vulnerabilities."""
    directory = input(f"{YELLOW}Enter directory to test: {NC}")
    output_to_file = input(f"{YELLOW}Output to file? (y/n): {NC}")
    command = ["snyk", "code", "test", directory]
    if output_to_file.lower() == "y":
        command += ["--all-projects"]
    run_tool(command)


def run_brakeman():
    """Run brakeman to scan a Ruby on Rails application for vulnerabilities."""
    directory = input(f"{YELLOW}Enter path to Ruby on Rails application: {NC}")
    command = ["brakeman", directory]
    run_tool(command)


def handle_secure_code_review_tools():
    """Handle the secure code review tools menu."""
    while True:
        display_secure_code_review_tools_menu()
        choice = input(f"{YELLOW}Choose an option: {NC}")
        if choice == "1":
            run_osv_scanner()
        elif choice == "2":
            run_snyk()
        elif choice == "3":
            run_brakeman()
        elif choice == "4":
            break
        else:
            print(f"{RED}Invalid choice, please try again.{NC}")


def main():
    """Main function to run the tool."""
    display_banner()  # Show the banner at the start
    while True:
        display_main_menu()
        choice = input(f"{YELLOW}Choose an option: {NC}")
        if choice == "1":
            handle_penetration_testing_tools()
        elif choice == "2":
            handle_secure_code_review_tools()
        elif choice == "3":
            break
        else:
            print(f"{RED}Invalid choice, please try again.{NC}")


if __name__ == "__main__":
    main()

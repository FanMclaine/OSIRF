from dotenv import load_dotenv
import os
import argparse

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text
import time

from module.whois_lookup import whois_lookup
from module.dns_enum import dns_enum
from module.header_check import check_headers
from module.shodan_scan import shodan_scan

console = Console()

BANNER = """
╔═════════════════════════════════════════════════╗
║   OSIRF - OSINT RECONNAISSANCE FRAMEWORK  v1.0  ║
║   Passive Footprinting & Attack Surface Map     ║
╚═════════════════════════════════════════════════╝
"""

load_dotenv()
SHODAN_API_KEY = os.getenv("api_key")

def print_banner():
    console.print(Text(BANNER, style="bold magenta"))

def print_shodan(data):
    if not data:
        console.print("[red][SHODAN] No data returned.[/red]")
        return
    table = Table(title="Shodan Intelligence", style="green", header_style="bold magenta")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="white")
    table.add_row("IP", data["ip"])
    table.add_row("Org", data["org"])
    table.add_row("ISP", data["isp"])
    table.add_row("Country", data["country"])
    table.add_row("City", data["city"])
    table.add_row("Open Ports", ", ".join(map(str, data["open_ports"])))
    table.add_row("Vulnerabilities", ", ".join(data["vulns"]) if data["vulns"] else "None detected")
    console.print(table)

def print_whois(data):
    if not data:
        console.print("[red][WHOIS] No data returned.[/red]")
        return
    table = Table(title=" WHOIS Lookup", style="green", header_style="bold magenta")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="white")
    for key, value in data.items():
        table.add_row(str(key), str(value) if value else "N/A")
    console.print(table)

def print_dns(data):
    if not data:
        console.print("[red][DNS] No data returned.[/red]")
        return
    table = Table(title="DNS Enumeration", style="green", header_style="bold magenta")
    table.add_column("Record Type", style="cyan")
    table.add_column("Values", style="white")
    for record_type, values in data.items():
        table.add_row(record_type, "\n".join(values) if values else "None")
    console.print(table)

def print_headers(data):
    if not data:
        console.print("[red][HEADERS] No data returned.[/red]")
        return
    table = Table(title="HTTP Header Analysis", style="green", header_style="bold magenta")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="white")
    table.add_row("Status Code", str(data["status_code"]))
    table.add_row("Server", data["server"])
    table.add_row("X-Powered-By", data["x_powered_by"])

    for h in data["security_headers_missing"]:
        table.add_row(f"[red]MISSING[/red] {h}", "[red]NOT PRESENT[/red]")
    for h, v in data["security_headers_present"].items():
        table.add_row(f"[green]PRESENT[/green] {h}", v)
    console.print(table)

def run_with_spinner(label, func, *args):
    with Progress(
        SpinnerColumn(),
        TextColumn(f"[bold green]{label}...[/bold green]"),
        transient=True,
    ) as progress:
        progress.add_task("", total=None)
        result = func(*args)
    return result

def main():
    parser = argparse.ArgumentParser(description="OSINT Reconnaissance Framework")
    parser.add_argument("domain", help="Target domain to investigate")
    args = parser.parse_args()
    domain = args.domain

    print_banner()
    console.print(Panel(f"[bold white]Target:[/bold white] [bold red]{domain}[/bold red]", 
                        style="green"))
    
    shodan_data = run_with_spinner("Querying Shodan Intelligence", shodan_scan, domain, SHODAN_API_KEY)
    whois_data  = run_with_spinner("Running WHOIS Lookup", whois_lookup, domain)
    dns_data    = run_with_spinner("Enumerating DNS Records", dns_enum, domain)
    header_data = run_with_spinner("Analyzing HTTP Headers", check_headers, domain)
    

    console.rule("[bold green]RESULTS[/bold green]")
    print_shodan(shodan_data)
    print_whois(whois_data)
    print_dns(dns_data)
    print_headers(header_data)

    console.rule("[bold green]SCAN COMPLETE[/bold green]")

if __name__ == "__main__":
    main()
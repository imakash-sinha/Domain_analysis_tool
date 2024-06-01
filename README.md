---

# Domain Analysis Tool

The Domain Analysis Tool is a Python-based utility that provides comprehensive analysis of domain names. It offers functionalities such as WHOIS lookup, DNS record retrieval, and SSL certificate analysis, all bundled into one convenient tool. Whether you're a cybersecurity analyst, a web developer, or simply curious about a domain's details, this tool makes it easy to gather essential information quickly.

## Features

- **WHOIS Lookup**: Retrieve registration details and administrative contact information for a domain.
- **DNS Record Retrieval**: Obtain various DNS records associated with a domain, including A, MX, NS, and TXT records.
- **SSL Certificate Analysis**: Gather information about a domain's SSL certificate, such as issuer details and expiration date.
- **Modular Design**: Easily customizable and extensible, allowing users to add new analysis modules or integrate with additional APIs.
- **Dependency Management**: Dependencies are clearly organized and listed in a requirements file for smooth installation and usage across different environments.

## Installation

Follow these steps to install and use the Domain Analysis Tool:

1. **Clone the Repository**: 
    ```bash
    git clone https://github.com/imakash-sinha/domain-analysis-tool.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd domain-analysis-tool
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Tool**:
    ```bash
    python main.py
    ```

5. **Enter a Domain Name**:
    Enter the domain name you want to analyze when prompted.

6. **View the Analysis**:
    The tool will display WHOIS information, DNS records, and SSL certificate details for the specified domain.

## Usage

- Simply run the `main.py` script and follow the on-screen instructions to input a domain name for analysis.
- Customize the tool by modifying existing modules or adding new ones according to your requirements.
- Refer to the code comments and documentation for detailed information on each module and its functionalities.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.


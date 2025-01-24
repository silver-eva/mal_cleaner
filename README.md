**Rule-Based Malware Infected PC Cleaner**
=============================================

**Table of Contents**
-----------------

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Usage](#usage)
5. [Threat Actor Malware Support](#threat-actor-malware-support)
6. [Rule-Based Cleaning](#rule-based-cleaning)
7. [Reporting](#reporting)
8. [Troubleshooting](#troubleshooting)
9. [Contributing](#contributing)

**Introduction**
---------------

This Python tool is designed to clean up PCs infected with custom threat actor malware. It uses a rule-based approach to identify and remove malware, providing a flexible and effective solution for malware removal.

**Features**
------------

* **Rule-Based Cleaning**: Define custom rules to detect and remove malware
* **Threat Actor Malware Support**: Supports cleaning of PCs infected with custom threat actor malware
* **Reporting**: Generates reports on cleaning operations
* **Configurable**: Allows for customization of cleaning rules and settings

**Requirements**
---------------

* Python 3.8+
* Windows 10+

**Usage**
-----

1. Clone the repository: `git clone https://github.com/silver-eva/mal_cleaner.git`
2. Go to the app directory: `cd mal_cleaner/`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the tool: `python mc.py -h`


**Threat Actor Malware Support**
-----------------------------

The tool supports cleaning of PCs infected with custom threat actor malware. You can add support for new malware by creating a new rule file (e.g., `malware_rule.yaml`) and adding it to the `rules` directory.

**Rule-Based Cleaning**
---------------------

The tool uses a rule-based approach to identify and remove malware. You can define custom rules using the `rule` format:
```yaml
MalwareRule:
    description: "Detects and removes malware"
    author: silver-eva
    pattern: "C:\\Windows\\Temp\\malware_*.exe"
    action: "delete"
```
**Reporting**
------------

The tool generates reports on cleaning operations. You can view reports in the `reports` directory.

**Troubleshooting**
-----------------

* Check the logs for errors: `mc.log`
* Verify startup args: `python mc.py -h`
* Check rule files for errors: `rules/*.yaml`

**Contributing**
--------------

Contributions are welcome! Please submit pull requests or issues to the repository.
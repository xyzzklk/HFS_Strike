# HFS Strike
HFS Strike is a simple Python Proof of Concept (PoC) and command line exploit tool for red teams of [CVE-2014-6287](https://www.rapid7.com/db/vulnerabilities/cve-2014-6287/), the Rejetto HTTP File Server null-byte macro injection vulnerability.

> [!WARNING]
> This script is provided strictly for educational purposes and authorised security testing in isolated lab environments you own or have explicit permission to test. Do not run against unauthorised systems. Provided "as is" without warranty of any kind; the author assumes no liability for misuse or damage.

## Affected HFS Versions:
- 2.3
- 2.3a
- 2.3b

## Usage
General usage:
```
python hfs_strike.py [options]
```

Options:
| Argument | Description |
| --- | --- |
| -t | Target url |
| -c | System (cmd) command string to execute |

Example:
```bat
python hfs_strike.py -t http://192.168.1.185/ -c "net user /add Admin 123456"
```

## Roadmap
This tool _could_ evolve to include features of exploiting more HFS RCEs, but this is not certainly planned in future.
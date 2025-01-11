
import requests
import os
from concurrent.futures import ThreadPoolExecutor


def scan_directory(url, directory):
    target_url = f"{url.rstrip('/')}/{directory}"

    try:
        response = requests.get(target_url, timeout=5)


        if response.status_code == 200:
            print(f"[200] Directory found: {target_url}")

        elif response.status_code == 403:
            print(f"[403] Access Forbidden: {target_url}")
        
        elif response.status_code == 404:
            print(f"[404] Directory Not found : {target_url}")
        
        else :
            print(f"[{response.status_code}] Unhandled response : {target_url}")


    except requests.exceptions.RequestException as e :
        print(f"Request error for {target_url}: {e}")



def dir_brute(url, wordlist, max_threads=20) :


    try:
        with open(wordlist, 'r') as f:
            directories = f.read().splitlines()

    except FileNotFoundError:
        print(f"Error: wordlist file {wordlist} not found!")
        return
    
    except Exception as e:
        print(f"Error while reading wordlist : {e}" )
        return
    
    
    with ThreadPoolExecutor(max_threads) as thread:
        thread.map(lambda dir: scan_directory(url, dir),directories)



if __name__ == "__main__":

    url = input("Enter Your Target Website-URL:  ").strip()
    wordlist = r"common.txt"


    dir_brute(url, wordlist, max_threads=20)
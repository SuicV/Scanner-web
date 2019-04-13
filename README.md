<!-- Version 1.6 -->
# Scanner Web
**Scanner Web** is a hacking tool for getting informations and searching dorks and scanning web sites , and it is compatible with`Linux` & `Windows`

> Requirements 
* Python 3.x [Download it](https://www.python.org/downloads/release/python-352/)
* You have the access to Python from command-line

> How to use it 

* you need to run **scannerweb.py file** with python from command line and pass args to the tool in the same command
* if your want to know more about arguments that you can pass use the help argument `-h` or `--help`

> Exemples 

### sample scan to a specified url 
```console
[YOUR-COMMAND-LINE] ~/scanner-web $ python3 scannerweb.py -u http://yousite.com
```
**Note :** `-u`,`--url` argument accept a url or file list of urls 

### sample scan to a specified dork 
```console
[YOUR-COMMAND-LINE] ~/scanner-web $ python3 scannerweb.py -d php?id=
```
**Note :** `-d`,`--dork` argument accept a dork or file list of dorks 

## search for a dork in specified engine 
```console
[YOUR-COMMAND-LINE] ~/scanner-web $ python3 scannerweb.py --dork /home/mylist.txt -e BING | GOOGLE
```
for engines you can use only google or bing
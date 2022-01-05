#!/bin/bash

export PYTHONHOME="C:\\Python27"
export PYTHONPATH="C:\\Python27\\Lib"
export WINEPATH="$PYTHONHOME;$PYTHONPATH"

# Can also get exact path from installer using command:
# sed -n -e "s/^Name: Path, Value: \(.*\), Action.*$/\1/p" python_install.log
# C:\Python27\;C:\Python27\Scripts;C:\windows\system32;C:\windows;C:\windows\system32\wbem;C:\windows\system32\WindowsPowershell\v1.0

wine C:\\IDA\\idat64.exe "$@"

unset PYTHONHOME PYTHONPATH WINEPATH
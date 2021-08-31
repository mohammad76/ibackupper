# backup maker with s3

this package help you to create and upload backup from a directory to s3 storage.


###install ibackupper
````
pip install ibackupper
````

###config
first you should set s3 configuration with this command:
```
ibackupper set_config 
```
this command prompt and ask your config

###usage
with this command you can backup directory and upload to s3 storage:
```
ibackupper backup
```
this command will open a prompt and ask directory for backup
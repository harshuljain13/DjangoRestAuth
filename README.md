# DjangoRestAuth
This Repository consists of implementation of various authentication techniques used in djangoRestFramework.

## Basic Authentication in Homeapp

### Get Data providing Username and Password
```
curl -X GET http://127.0.0.1:8000/notes/ -u harshul:harshulpass
```
### Post Data providing Username and Password
```
curl -d "note_title=https://harshul1610.github.io&note_description=this is my personal site and blog domain" http://127.0.0.1:8000/notes/ -u harshul:harshulpass
```


## TokenAuthentication in Tokenapp

### Get Token
```
curl -d "username=harshul&password=harshulpass" http://127.0.0.1:8000/api-token-auth/
```
### Post data using Token
```
curl -d "url_title=https://harshul1610.github.io&url_description=this is my personal site and blog domain" http://127.0.0.1:8000/urls/ -H 'Authorization: Token e91c548ad661f7ff3e74813dfb06d18a9c6daee3'
```
### Get Data using Token
```
curl -X GET http://127.0.0.1:8000/urls/ -H 'Authorization: Token e91c548ad661f7ff3e74813dfb06d18a9c6daee3'
```

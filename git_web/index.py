#!python
print("content-type: text/html; charset=utf-8")
print()
import cgi

print('''<!doctype html>
<html>
<head>
  <title>Github Info Text File Maker</title>
</head>
<body>
  <form action="save.py" method="post">
  <p>
    &nbsp;Input your Github url :
  </p>
  <p>
    &nbsp;<input type = 'url' name = 'url'></input>&nbsp;<input type = 'submit' value = 'Save'></p>
</form>
</body>
</html>''')
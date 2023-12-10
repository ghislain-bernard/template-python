## template-python

[![python.webp](python.webp)](https://www.python.org)

### usage

```console
$ python3 template.py
template@0.0.1

$ python3 -m unittest discover --start-directory=test --verbose
test_project (test_template.TestTemplate) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

$ yapf --in-place --verbose template.py test/test_template.py
Reformatting template.py
Reformatting test/test_template.py

$ pylint --verbose template.py test/test_template.py
Using config file /home/user/git/template-python/.pylintrc

$ mypy template.py test/test_template.py
Success: no issues found in 2 source files
```

> MIT License  
> ghislain.bernard@gmail.com

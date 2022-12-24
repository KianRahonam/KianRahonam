from django.test import TestCase

# Create your tests here.


maindict = {"data":{"a":1},
            "data2":{"b":2}}
a= maindict["data"]
print(list(a.values()))

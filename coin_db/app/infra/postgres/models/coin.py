from pydoc import ModuleScanner
from tortoise import fields, models


class Coin(models.Model):

    name = fields.CharField(max_length=50, null=True)
    E = fields.CharField(max_length=50, null=True)
    t = fields.CharField(max_length=50, null=True)
    T = fields.CharField(max_length=50, null=True)
    i = fields.CharField(max_length=50, null=True)
    f = fields.CharField(max_length=50, null=True)
    L = fields.CharField(max_length=50, null=True)
    o = fields.CharField(max_length=50, null=True)
    c = fields.CharField(max_length=50, null=True)
    h = fields.CharField(max_length=50, null=True)
    l = fields.CharField(max_length=50, null=True)
    v = fields.CharField(max_length=50, null=True)
    n = fields.CharField(max_length=50, null=True)
    x = fields.CharField(max_length=50, null=True)
    q = fields.CharField(max_length=50, null=True)
    V = fields.CharField(max_length=50, null=True)
    Q = fields.CharField(max_length=50, null=True)
    B = fields.CharField(max_length=50, null=True)

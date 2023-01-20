from tortoise.models import Model
from tortoise import fields


class City(Model):
    id = fields.IntField(pk=True)
    remote_id = fields.IntField(unique=True)
    name = fields.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.name

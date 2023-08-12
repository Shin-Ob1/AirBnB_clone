#!/usr/bin/python3
from models.base_model import BaseModel

"""

This module contains the user class of the which inherits
from the BaseModel class

"""


class User(BaseModel):
    """The user class which has attributes

    methods:
        __init__: the initialization method that initializes the instance

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize user class"""
        super().__init__(**kwargs)

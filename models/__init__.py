#!/usr/bin/python3
"""Module to represent this directory as package"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

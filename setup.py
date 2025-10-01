from setuptools import setup

APP = ['self_care_reminder.py']  # Update to your main script filename
OPTIONS = {
    'argv_emulation': True,
    # 'iconfile': 'icon.icns',  # Optional: add a custom icon file for your app
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
import tkinter as tk
from tkinter import messagebox
import threading # For running reminders in a separate thread to keep GUI responsive
import time
import random   # For randomizing messages and animations to keep it fun and engaging 
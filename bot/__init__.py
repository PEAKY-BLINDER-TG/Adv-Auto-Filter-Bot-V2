#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = "3020564"

API_HASH = "91c026fadfdc442f504a0bd3e5c8cd18"

BOT_TOKEN = "1853498659:AAFdnSWzBEA4wqp8qpnViDKyvOSjV4y9-vU"

DB_URI = "mongodb+srv://Wafikh:wafikh@cluster0.pjcpl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

USER_SESSION = "BQCR0BxaDQFeM9wG9OjLeg4VfgQdVSaYfWw0ViuypH-delDV2DwbOe6w1vnR9XHNoH8DQ_643spGXP9fy-VR44KNybmXgYiJKP3wLNR-JuD5FEM5dSVptK8OzJtiv_oX5QPW3ibxQlqGLu0X2jlwLLX_m_oMabdyiN6yrtIhV-goKQyP7aGVktC4tossKhDTEAmiz3rHlvh9FUSd9_AbJphWZLvIbvg4Xt3yoBWectiXfXc1C1JjGeHUaEMqugDCun3gtggItmYx-3PqVgT2gjQ6IWsDINGbg1XD5FtgDEkKtAdqXxhOl7S3ZwAe4JvPCWy-0CZ9V5cw3Ow9LNLwaDjYXQWOpQA"

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

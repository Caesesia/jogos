#!/bin/bash

source venv/bin/activate
pip freeze > requirements.txt
echo "✅ requirements.txt updated!"
echo ""

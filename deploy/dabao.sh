#!/bin/bash
cp $1 q-shorturl/putsurl/settings_local.py
cp $1 q-shorturl/getsurl/settings_local.py
tar czf q-shorturl.tar.gz --exclude=.* q-shorturl/

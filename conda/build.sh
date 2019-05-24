#!/bin/bash

# Install module
python setup.py install --single-version-externally-managed --record=record.txt

# Create catalog
mkdir -p $PREFIX/share/intake
cp mo_aws_earth/catalog.yaml $PREFIX/share/intake/mo_aws_earth.yaml

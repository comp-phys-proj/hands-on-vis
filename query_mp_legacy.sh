#!/bin/bash

if [ "$1" == "-h" -o "$1" == "--help" -o "$1" == "" ]; then
    echo "Usage: $0 <include one of> -- <must include>"
    exit 0
fi

if [ "$MP_API_KEY_LEGACY" == "" ]; then
    echo "==========================================================" >&2
    echo "You need to obtain a materials project API key!" >&2
    echo "Go to https://materialsproject.org" >&2
    echo "Click on 'Login' to login/create an account." >&2
    echo "Then go to Dashboard and 'Generate API Key'." >&2
    echo "Grab the character string an place it in an " >&2
    echo "environment variable MP_API_KEY like this:" >&2
    echo "" >&2
    echo "  export MP_API_KEY_LEGACY=\"<string>\"" >&2
    echo "==========================================================" >&2
    exit 1
fi

IN=""
while [ -n "$1" ]; do
    if [ "$1" == "--" ]; then
        shift 1
        break
    fi
    if [ -z "$IN" ]; then
        IN="\"$1\""
    else
        IN="$IN,\"$1\""
    fi
    shift 1
done

ALL=""
while [ -n "$1" ]; do
    if [ -z "$ALL" ]; then
        ALL="\"$1\""
    else
        ALL="$ALL,\"$1\""
    fi
    shift 1
done

#curl https://www.materialsproject.org/rest/v2/materials/mp-1234/vasp?API_KEY=$MP_API_KEY

CRITERIA='{"elements": {"$in": ['$IN'], "$all": ['$ALL']}}'
PROPERTIES='["material_id", "pretty_formula", "elements", "nelements", "energy", "energy_per_atom", "density", "volume", "nsites", "band_gap", "total_magnetization", "elasticity", "piezo", "diel", "copyright", "cif"]'

curl -s --header "X-API-KEY: $MP_API_KEY_LEGACY" "https://legacy.materialsproject.org/rest/v2/query" -F "criteria=$CRITERIA" -F "properties=$PROPERTIES"

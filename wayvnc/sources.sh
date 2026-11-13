#!/bin/bash
set -euo pipefail
cp "$(dirname "$1")"/*.patch "$2"/

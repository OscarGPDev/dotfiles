#!/bin/bash
alacritty --working-directory "$(readlink -e /proc/"$(pgrep -P "$(xdo pid)" | head -n 1)"/cwd)"

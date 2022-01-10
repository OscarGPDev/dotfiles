#!/bin/bash
current=$(setxkbmap -query | grep layout)
if [ "$current" == "layout:     us" ]; then
  setxkbmap es
else
  setxkbmap us
fi

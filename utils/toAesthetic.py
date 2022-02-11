#!/usr/bin/env python3
import sys
origin_text_array = input().split(' ')
result_text = ' ~ '.join([' '.join([letter for letter in word]) for word in origin_text_array])
if "--capitalize" in sys.argv:
  result_text = result_text.capitalize()
if "--upper" in sys.argv:
  result_text = result_text.upper()
if "--tagify" in sys.argv:
  result_text = f"<{result_text}/>"
print(result_text)

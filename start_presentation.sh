#!/bin/bash

ipython nbconvert ch1_intro.ipynb --to slides --reveal-prefix ../reveal.js --post serve

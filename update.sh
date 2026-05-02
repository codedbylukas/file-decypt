#/bin/bash

pip freeze | cut -d = -f 1 | xargs -n1 pip install --upgrade

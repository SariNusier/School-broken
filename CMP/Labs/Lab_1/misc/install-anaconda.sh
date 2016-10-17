
#!/bin/bash

WORK_DIR="$(mktemp -d)"
CONDA_DIR="$HOME/anaconda"

if [[ "$(uname)" == "Darwin" ]]; then
    NAME="Miniconda2-latest-MacOSX-x86_64.sh"
else
    NAME="Miniconda2-latest-Linux-x86_64.sh"
fi

cd $WORK_DIR

wget "https://repo.continuum.io/miniconda/$NAME"
bash "$NAME" -b -p "$CONDA_DIR"
echo "export PATH=$CONDA_DIR/bin:\$PATH" >> ~/.bashrc


function cleanup {
  rm -rf "$WORK_DIR"
}

trap cleanup EXIT
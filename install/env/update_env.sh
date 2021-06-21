#!/bin/bash
cd "${0%/*}" || exit 1    # run from this directory
set -e  # exit when any command fails
eval "$(conda shell.bash hook)"

echo "Installing conda-lock"
conda install -c conda-forge conda-lock  # install conda-lock in base

cd recipes
env=$1  # input conda env to update
python update_env.py -i ${env}_env.yml.meta -q -p  # this only creates .yml

cd ..
if [ "$(uname)" == "Darwin" ]; then
    conda-lock -f ./recipes/${env}_env.yml -p osx-64 --filename-template "${env}-env-mac.lock"
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    conda-lock -f ./recipes/${env}_env.yml -p linux-64 --filename-template "${env}-env-linux.lock"
else
    echo "Unrecongnized Operating System, PuMA cannot be installed."
    exit 1
fi
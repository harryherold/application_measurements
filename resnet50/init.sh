# Load required modules
# module load scorep/6.0-sampling-fosscuda-2019b
# module load TensorFlow/2.1.0-fosscuda-2019b-Python-3.7.4
module load scorep_python/fix_version scorep/fix-bfd-api

# Source/Create virtual env
if [ -d venv ]; then
    source venv/bin/activate
else
    virtualenv --system-site-packages venv
    source venv/bin/activate
    pip install -r requirements.txt
fi

export RESNET50_DIR=$PWD

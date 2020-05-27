# Dependencies
* Score-P >= 5.0
* Tensorflow >= 2.1
* Tensorflow-Datasets

# Prepare Run
* Edit `init.sh`
* Add there modules to load or set paths to dependencies
* Dependencies could also installed through `requirements.txt`, just edit the file

# Configure Score-P Measurement
* Edit `config_*_resnet50`

# Trace/Profile ResNet50
```
~> source init.sh
~> scorep_runpy.sh <exec-type> <python_app> <args>
exec-type   --cpu, --gpu
```


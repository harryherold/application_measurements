#!/usr/bin/bash

if [[ -z "$RESNET50_DIR" ]] || [[ -z "$VIRTUAL_ENV" ]];
then
    echo "ERROR: Resnet50 project is not initialized."
    echo "HINT: source init.sh"
    exit 1
fi

app="$2"
args="${@:3}"

if [[ "$1" == "--cpu" ]];
then
    source config_cpu_resnet50
    echo "CUDA_VISIBLE_DEVICES = $CUDA_VISIBLE_DEVICES"
    python -m scorep --thread=pthread --noinstrumenter $app $args
fi

if [[ "$1" == "--gpu" ]];
then
    source config_gpu_resnet50
    python -m scorep --noinstrumenter $app $args
fi


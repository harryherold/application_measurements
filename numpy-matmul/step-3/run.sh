#!/usr/bin/sh

export SCOREP_TOTAL_MEMORY=1G
export SCOREP_FILTERING_FILE=/home/cherold/workspace/numpy_openblas/numpy.filt
export SCOREP_PROFILING_MAX_CALLPATH_DEPTH=8
export SCOREP_METRIC_PAPI="PAPI_DP_OPS" 
export SCOREP_ENABLE_TRACING=false
export SCOREP_ENABLE_PROFILING=true

#export SCOREP_ENABLE_UNWINDING=true

python -m scorep "--thread=pthread:runtime" \
                 "--libwrap=runtime:/home/cherold/scorep/install/gotcha/share/scorep/openblas.libwrap" \
                 "--instrumenter-type=trace" \
                 ../matrix_improved.py


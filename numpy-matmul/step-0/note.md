# Execution
* no filtering
* blank run
```sh
export SCOREP_EXPERIMENT_DIRECTORY=$PWD/matrix-thread-profile
python -m scorep --thread=pthread:runtime matrix.py
```
# Output
```sh
[Score-P] src/measurement/profiling/scorep_profile_collapse.c:77: Warning: Score-P callpath depth limitation of 30 exceeded.
Reached callpath depth was 71.
Consider setting SCOREP_PROFILING_MAX_CALLPATH_DEPTH to 71.
```
# Conclusion
* filter importlib, random:uniform
* limit call path depth to 8


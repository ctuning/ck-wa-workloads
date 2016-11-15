
export  CK_WA_RAW_RESULT_PATH=/home/fursin/CK/local/wa-result/6d66c7034024e679/20161012-001215
export  CK_WA_SCRIPTS_PATH=/home/fursin/CK/ck-wa/script/process-wa

export PATH=/data/local/tmp/tools:$PATH; export LD_LIBRARY_PATH=/data/local/tmp:/data/local/tmp/lib:$LD_LIBRARY_PATH

export CK_WA_CMD="/home/fursin/CK/local/wa-result/6d66c7034024e679/20161012-001215/tmp-xz8fjp4p.yaml -fd /home/fursin/CK/local/wa-result/6d66c7034024e679/20161012-001215/wa-output"


echo    executing code ...
 wa run ${CK_WA_CMD} > tmp-output1.tmp 2> tmp-output2.tmp

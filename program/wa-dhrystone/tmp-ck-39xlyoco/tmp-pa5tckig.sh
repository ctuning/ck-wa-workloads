
export  CK_WA_RAW_RESULT_PATH=/home/fursin/CK/local/wa-result/c7333bf94c0f8cb4/20161013-133549
export  CK_WA_SCRIPTS_PATH=/home/fursin/CK/ck-wa/script/process-wa

export PATH=/data/local/tmp/tools:$PATH; export LD_LIBRARY_PATH=/data/local/tmp:/data/local/tmp/lib:$LD_LIBRARY_PATH

export CK_WA_CMD="/home/fursin/CK/local/wa-result/c7333bf94c0f8cb4/20161013-133549/tmp-bvqirg_s.yaml -fd /home/fursin/CK/local/wa-result/c7333bf94c0f8cb4/20161013-133549/wa-output"


echo    executing code ...
 wa run ${CK_WA_CMD} > tmp-output1.tmp 2> tmp-output2.tmp

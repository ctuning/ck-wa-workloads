
export  CK_WA_RAW_RESULT_PATH=/home/fursin/CK/local/wa-result/7334f2fbc3f88a0c/20161012-010307
export  CK_WA_SCRIPTS_PATH=/home/fursin/CK/ck-wa/script/process-wa

export PATH=/data/local/tmp/tools:$PATH; export LD_LIBRARY_PATH=/data/local/tmp:/data/local/tmp/lib:$LD_LIBRARY_PATH

export CK_WA_CMD="/home/fursin/CK/local/wa-result/7334f2fbc3f88a0c/20161012-010307/tmp-ace04mti.yaml -fd /home/fursin/CK/local/wa-result/7334f2fbc3f88a0c/20161012-010307/wa-output"


echo    executing code ...
 wa run ${CK_WA_CMD} > tmp-output1.tmp 2> tmp-output2.tmp

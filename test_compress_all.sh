echo "[OS]" > ./result_compressed/run-info.txt
cat /etc/os-release >> ./result_compressed/run-info.txt
echo "" >> ./result_compressed/run-info.txt
echo "[python-version]" >> ./result_compressed/run-info.txt
python3 --version >> ./result_compressed/run-info.txt
echo "" >> ./result_compressed/run-info.txt
echo "[redis server version]" >> ./result_compressed/run-info.txt
redis-server --version >> ./result_compressed/run-info.txt
echo "" >> ./result_compressed/run-info.txt
echo "[redis config]" >> ./result_compressed/run-info.txt
redis-cli config get *ziplist* >> ./result_compressed/run-info.txt
echo "" >> ./result_compressed/run-info.txt
echo "[redis info]" >> ./result_compressed/run-info.txt
redis-cli info >> ./result_compressed/run-info.txt
echo "" >> ./result_compressed/run-info.txt

# ひらがな1文字 ~ 100,000,000文字のデータでテスト
for i in {0..8};\
do
    STR_NUM=$(( 10 ** ${i} ))
    DESC="test${STR_NUM}"
    CMD="python3 ./src/redis_kensho_compress.py 3 3 1 ${STR_NUM} ${STR_NUM} True"

    echo "start ${DESC}"
    echo "command [${CMD}]" > "./result_compressed/${DESC}.txt"
    ${CMD} >> "./result_compressed/${DESC}.txt"
    echo "finish ${DESC}"
done;


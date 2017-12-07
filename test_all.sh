echo "[OS]" > ./result/run-info.txt
cat /etc/os-release >> ./result/run-info.txt
echo "" >> ./result/run-info.txt
echo "[python-version]" >> ./result/run-info.txt
python3 --version >> ./result/run-info.txt
echo "" >> ./result/run-info.txt
echo "[redis server version]" >> ./result/run-info.txt
redis-server --version >> ./result/run-info.txt
echo "" >> ./result/run-info.txt
echo "[redis config]" >> ./result/run-info.txt
redis-cli config get *ziplist* >> ./result/run-info.txt
echo "" >> ./result/run-info.txt
echo "[redis info]" >> ./result/run-info.txt
redis-cli info >> ./result/run-info.txt
echo "" >> ./result/run-info.txt


DESC="test101-data-100,str-10to30,hiragana"
CMD="python3 ./src/redis_kensho.py 3 3 100 10 30 True"

echo "start ${DESC}"
echo "command [${CMD}]" > "./result/${DESC}.txt"
${CMD} >> "./result/${DESC}.txt"
echo "finish ${DESC}"


DESC="test102-data-100,str-20to20,hiragana"
CMD="python3 ./src/redis_kensho.py 3 3 100 20 20 True"

echo "start ${DESC}"
echo "command [${CMD}]" > "./result/${DESC}.txt"
${CMD} >> "./result/${DESC}.txt"
echo "finish ${DESC}"


DESC="test103-data-100,str-40to40,alphabet"
CMD="python3 ./src/redis_kensho.py 3 3 100 40 40 False"

echo "start ${DESC}"
echo "command [${CMD}]" > "./result/${DESC}.txt"
${CMD} >> "./result/${DESC}.txt"
echo "finish ${DESC}"


DESC="test104-data-100,str-50to80,alphabet"
CMD="python3 ./src/redis_kensho.py 3 3 100 50 80 False"

echo "start ${DESC}"
echo "command [${CMD}]" > "./result/${DESC}.txt"
${CMD} >> "./result/${DESC}.txt"
echo "finish ${DESC}"


DESC="test105-data-100,str-70to70,alphabet"
CMD="python3 ./src/redis_kensho.py 3 3 100 70 70 False"

echo "start ${DESC}"
echo "command [${CMD}]" > "./result/${DESC}.txt"
${CMD} >> "./result/${DESC}.txt"
echo "finish ${DESC}"




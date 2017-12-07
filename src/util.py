import random
import subprocess
import string
import time

def create_test_data(dataCnt, minLength, maxLength, isJP=True):
    # http://mokicks.hatenablog.com/entry/2017/10/13/024127
    # https://qiita.com/FGtatsuro/items/92bca91ed665449ab047
	jp = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん"]
	dataDict = {}
	length = random.randint(minLength,maxLength)
	for cnt in range(dataCnt):
                if isJP:
                    word = ""
                    for i in range(length):
                        word += jp[random.randint(0,len(jp)-1)]

                else:
                    word=''.join([random.choice(string.ascii_letters + string.digits) for i in range(dataCnt)])

                dataDict["key" + str(cnt)] = word

	return dataDict

def reset_redis(r):
    r.flushall()
    time.sleep(1)

def set_redis_hash(r, dict):
	r.hmset("dict_key", dict)

def set_redis_key(r, dict):
	for k,v in dict.items():
		r.set(k, v)

def set_redis_key2(r, dict):
    r.set("dict_key", dict)

def view_redis_memory():
    #http://takuya-1st.hatenablog.jp/entry/2014/08/23/022031
    cmd = "redis-cli info | grep 'used_memory'"
    subprocess.call( cmd, shell=True) 

def get_redis_memory() -> int:
    # https://qiita.com/kentarosasaki/items/033751ba8b26cc51cf2a
    keyword = "used_memory:"
    cmd = "redis-cli info | grep '%s'" % keyword
    ret = subprocess.Popen(
                  cmd, stdout=subprocess.PIPE,
                  shell=True).communicate()[0]
    ret_str = ret.decode("utf-8")
    return int(ret_str.replace(keyword, ""))


def get_redis_debug_object():
    #https://siguniang.wordpress.com/2013/02/16/hash-reduce-memory-usage-in-redis/
    cmd = "redis-cli debug object %s" % "dict_key"
    ret = subprocess.Popen(
                  cmd, stdout=subprocess.PIPE,
                  shell=True).communicate()[0]
    return ret.decode("utf-8")



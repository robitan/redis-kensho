import util
import redis
import sys

args = sys.argv

test_cnt=int(args[1])
test_loop_cnt=int(args[2])
data_cnt=int(args[3])
data_min_length=int(args[4])
data_max_length=int(args[5])
if len(args) > 6 and args[6] == "False":
    is_jp=False
else:
    is_jp=True

for i in range(test_cnt):

    print ("----- test %d -----" % (i + 1) )
    # create test data
    data_dict = util.create_test_data(data_cnt, data_min_length, data_max_length, is_jp)

    for j in range(test_loop_cnt):
        r = redis.Redis(host='localhost', port=6379, db=0)

        print("")
        print("test %d - %d" % (i+1,j+1))

        # hash
        util.reset_redis(r)
        memory_base = util.get_redis_memory()

        util.set_redis_hash(r, data_dict)
        memory_hash = util.get_redis_memory()

        used_memory_hash = memory_hash - memory_base

        print("used_memory by hash: %d" % (used_memory_hash) )

        # key
        util.reset_redis(r)
        memory_base = util.get_redis_memory()

        util.set_redis_key(r, data_dict)
        memory_str = util.get_redis_memory()

        used_memory_str = memory_str - memory_base

        print("used_memory by key: %d" % (used_memory_str) )


        # json
        util.reset_redis(r)
        memory_base = util.get_redis_memory()

        util.set_redis_json(r, data_dict)
        memory_json = util.get_redis_memory()

        used_memory_json = memory_json - memory_base

        print("used_memory by json: %d" % (used_memory_json) )

        # compressed json
        util.reset_redis(r)
        memory_base = util.get_redis_memory()

        util.set_redis_compressed_json(r, data_dict)
        memory_compressed_json = util.get_redis_memory()

        used_memory_compressed_json = memory_compressed_json - memory_base

        print("used_memory by compressed json: %d" % (used_memory_compressed_json) )

        # div
        print("hash / str : %f" % ( float(used_memory_hash) / used_memory_str) )
        print("json / str : %f" % ( float(used_memory_json) / used_memory_str) )
        print("compressd_json / str : %f" % ( float(used_memory_compressed_json) / used_memory_str) )

        util.reset_redis(r)

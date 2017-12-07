import util
import redis
import sys

r = redis.Redis(host='localhost', port=6379, db=0)

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
        print("")
        print("test %d - %d" % (i+1,j+1))

        # hash
        util.reset_redis(r)
        memory_base = util.get_redis_memory()

        util.set_redis_hash(r, data_dict)
        memory_hash = util.get_redis_memory()
        print( util.get_redis_debug_object() )

        used_memory_hash = memory_hash - memory_base

        print("used_memory by hash: %d" % (used_memory_hash) )

        # key
        util.reset_redis(r)
        memory_base = util.get_redis_memory()

        util.set_redis_key2(r, data_dict)
        memory_key = util.get_redis_memory()

        used_memory_key = memory_key - memory_base

        print("used_memory by key: %d" % (used_memory_key) )


        # div 
        print("hash / key : %f" % ( float(used_memory_hash) / used_memory_key) )

        util.reset_redis(r)

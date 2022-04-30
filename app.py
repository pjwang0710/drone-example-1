import redis

print('good!!')
r= redis.StrictRedis(host='redis',port=6379)
r.keys("*")

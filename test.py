from redis import Redis
r = Redis()
r.set("foo","bar")
name = r.get("foo")
print(name)
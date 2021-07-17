import lru_cache

c = lru_cache.LRU(3)

c.put(3,1)
c.put(2,"something")
print(c.get_cache())
print(c.get(2))
c.put(5,7)
c.put(4,9)
c.put(8,0)
print(c.get_cache())



  
   
   
from collections import OrderedDict

class LruCache:
    
    def __init__(self, capacity):
        
        self.capacity = capacity
        self.cache = OrderedDict()
        
    def get(self, key):
        if key not in self.cache:
            print("cache is Miss")
            return -1
            
        self.cache.move_to_end(key)
        
        print(f"Cache Hit {key}")
        
        return self.cache[key]
    
    def put(self, key, value):
        
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            
        else:
            
            if len(self.cache) >= self.capacity:
                return_key , return_value = self.cache.popitem(last = False)
                
                print(f"Evicted: {return_key}") 
                
            self.cache[key] = value
            
            print(f"Existing Cache {dict(self.cache)}")
            
if __name__ == "__main__":
    
    lru = LruCache(3)
    
    lru.put("A", 100)
    lru.put("B", 200)
    lru.put("C", 300)
    
    print(lru.get("A"))
    
    lru.put("D",200)
    
                
    print("Get B:", lru.get("B"))
    print("Get A:", lru.get("A"))
                       
            
    
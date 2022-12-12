nums = set(range(1,10001))
generator_nums = set()

for num in nums:
    for i in str(num):
        num += int(i)
    
    generator_nums.add(num)
    
self_nums = nums - generator_nums

for i in sorted(self_nums):
    print(i)

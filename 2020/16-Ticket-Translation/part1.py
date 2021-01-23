from collections import defaultdict
import re

if __name__ == "__main__":
    with open('input.txt') as fp:
        lines = fp.readlines()
        ranges = defaultdict(lambda:False)
        for i in range(20):
            nums = re.findall('(\d+)-(\d+)', lines[i])
            ranges = {**ranges, **{str(i):True for i in range(int(nums[0][0]), int(nums[0][1])+1)}}
            ranges = {**ranges, **{str(i):True for i in range(int(nums[1][0]), int(nums[1][1])+1)}}
        ans = 0
        for i in range(25, len(lines)):
            print(lines[i])
            for num in lines[i].strip('\n').split(','):
                if num not in ranges:
                    ans += int(num)
    print(ans)

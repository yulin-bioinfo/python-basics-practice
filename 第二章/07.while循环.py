
  # while案例：计算1——100之间的所有偶数累加之和
i = 1
total = 0
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1
print(f"结果为{total}")



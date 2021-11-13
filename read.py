data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了總, 總共有',len(data), '筆資料')

sum_len = 0
for x in data:
	sum_len += len(x)
averge = sum_len/len(data)
print('平均長度是', averge)
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了總, 總共有',len(data), '筆資料')

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進wc字典
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

while True:
	word = input('請問你想查甚麼字: ')
	if word == 'q':
		break;
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔')
		
print('感謝使用查詢功能')

















# sum_len = 0
# for x in data:
# 	sum_len += len(x)
# averge = sum_len/len(data)
# print('留言的平均長度是', averge)

# new = []
# for i in data:
# 	if len(i) < 100:
# 		new.append(i)
# print('一共有', len(new), '筆留言長度小於100')

# good = []
# #good = [d for d in data if 'good' in d]
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '筆留言提到good')
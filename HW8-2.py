n = int(input())
xlist = input().split()
ylist = input().split()

# 設定Point為Class
# 定義一定要先輸入x與y才能使用
# 定義該點的magnitude是x平方+y平方
# 定義用self與p的magnitude比誰較小，若相同則看x誰較小，若self小於p則傳回True
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def magnitude(self):
		magnitude = self.x**2+self.y**2
		return magnitude
	def isSmallerThan(self,p):
		if self.magnitude() < p.magnitude():
			return True
		elif self.magnitude() == p.magnitude():
			if self.x < p.x:
				return True
		return False
#用n紀錄點的編號
#假設point_list裡已經有點1存在，用後續的for迴圈一個一個處理其他點
n = 0
point_list=[1]
for x, y in zip(xlist, ylist):
	n += 1
	a = Point(int(x), int(y))
	#用count紀錄要插入point_list的絕對位置
	#用false_count紀錄下列迴圈，出現false的次數
	count = -1
	false_count = 0
	#用a點，與在既有的point_list中的點一個一個比較，比較時設為點p
	for i in point_list:
		#若為第一個點，則continue(因為我們已經預先將其加入point_list)
		if [x,y] == [xlist[i-1],ylist[i-1]]:
			continue
		else:
			count += 1
			p = Point(int(xlist[i-1]),int(ylist[i-1]))
			#若a點比p點小，則將a點insert在p點的前面，並且跳出迴圈
			if a.isSmallerThan(p):
				point_list.insert(count,n)
				break
			#若a點與point_list中的所有元素p比較後接回傳false，則將a點append進point_list
			else:
				false_count += 1
				if false_count == len(point_list):
					point_list.append(n)
					
#一個一個印出point_list的element，element之間留一個空格
for element in point_list:
	if element == point_list[-1]:
		print(element)
	else:
		print(element,end=" ")
# p1 = Point(5, 8)
# p2 = Point(8, 5)
# p3 = Point(7, 4)
# print(p1.magnitude())
# print(p1.isSmallerThan(p2))
# print(p1.isSmallerThan(p3))
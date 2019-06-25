# -*- coding:utf-8 -*-
# class Solution:
#     def NumberOf1(self, n):
#         # write code here
#         count = 0
#         if n<0:
#             n = n&0xffffffff
#             print(n)
#         while n:
#             n = (n-1)&n
#             count += 1
#         return count
#
# ret = Solution().NumberOf1(-1)
# print(2**32)





# import jieba
# import jieba.analyse
#
# #第一步：分词，这里使用结巴分词全模式
# f = open("text",encoding="utf-8")
# text =f.read()
# fenci_text = jieba.cut(text)
# #print("/ ".join(fenci_text))
#
# #第二步：去停用词
# #这里是有一个文件存放要改的文章，一个文件存放停用表，然后和停用表里的词比较，一样的就删掉，最后把结果存放在一个文件中
# stopwords = {}.fromkeys([ line.rstrip() for line in open('test',encoding="utf8") ])
# final = ""
# for word in fenci_text:
#     if word not in stopwords:
#         if (word != "。" and word != "，") :
#             final = final + " " + word
# #print(final)
#
# #第三步：提取关键词
# a=jieba.analyse.extract_tags(text, topK = 20, withWeight = True, allowPOS = ())
# b=jieba.analyse.extract_tags(text, topK = 20,   allowPOS = ())
# print("关键词及相应权重：",a)
# print("关键词：",b)
# #text 为待提取的文本
# # topK:返回几个 TF/IDF 权重最大的关键词，默认值为20。
# # withWeight:是否一并返回关键词权重值，默认值为False。
# # allowPOS:仅包括指定词性的词，默认值为空，即不进行筛选。

# -*- coding:utf-8 -*-
# class Solution:
#     def __init__(self):
#         self.data = []      #数据栈
#         self.sup = []       #辅助栈
#     def push(self, node):
#         self.data.append(node)
#         if (len(self.sup)==0 or node < self.min()):
#             self.sup.append(node)
#         else:
#             self.sup.append(self.min())
#
#     def pop(self):
#         if (len(self.sup) > 0 and len(self.data) > 0):
#             self.data.pop()
#             self.sup.pop()
#
#     def top(self):
#         if self.data is not None:
#             return self.data[-1]
#
#     def min(self):
#         if(len(self.sup)>0 and len(self.data) >0):
#             return self.sup[-1]
#
#
# if __name__ == '__main__':
#     ret = Solution()
#     ret.push(1)
#     print(ret.data)

























my_file = open("test.txt", "r")
content_list = my_file. readlines()

print(len(content_list))
l = len(content_list)

i = 1
# while i < 23:
#     # for j in range(0, i * 1000):
#     #     if (j >= l):
#     #         break
#     #     print([k for k in ])
#     print(content_list[1000*(i -1): 1000*i])
#     with open("test/{}.txt".format(i), "w") as f:
#         for t in content_list[1000*(i -1): 1000*i]:
#             f.write(t)
#     i = i + 1

with open("test/{}.txt".format(23), "w") as f:
    for t in content_list[22000:]:
        f.write(t)


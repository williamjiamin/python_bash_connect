# Created by william from lexueoude.com. 更多正版技术视频讲解
# 公众号1.乐学偶得（lexueoude）2.乐学FinTech (LoveShareFinTech)

# 能够实现srt转xml->执行某一个能够实现需求的脚本——>lxod_script

# 你可以把lxod_script替换成你任意需要执行的程序，然后按照规定将list中的对象作为参数pass到你的程序中
# word->pdf
# txt->csv
# ....

# bash_script ------> python script打通


import glob, os
import subprocess

# Python官方建议如果要在python中调用bash命令，可以使用subprocess

os.chdir("subtitle")
srt_name_list = []
xml_name_list = []

for file in glob.glob("*.srt"):
    # print(file)
    srt_name_list.append(file)

# print(srt_name_list)

for name in srt_name_list:
    base, ext = os.path.splitext(name)
    new_name = base + ".fcpxml"
    xml_name_list.append(new_name)

# print(xml_name_list)

# 推荐一种直接在命令的同时变更工作路径的方式
# subprocess.run(["ls", "-al"], cwd="subtitle")

# subprocess.call("ls", shell=True, cwd="subtitle")

for srt_name, xml_name in zip(srt_name_list, xml_name_list):
    subprocess.run(["./lxod_script", "-srt", srt_name, xml_name])

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands
import os
import sys


repo_name = [
        # 要迁移的项目名称
        # "react-native-wechat",
		"Laso_data_pipeline"					
        ]

gitlab = [
        # 要迁移的项目gitlab的URL
        # "git@gitlab.com:lasoplanet/plugins/react-native-wechat.git",
		"git@gitlab.com:lasoplanet/turing/Laso_data_pipeline.git"
        ]

bitbucket = [
        # 要迁移的项目bitbucket的URL
        # "ssh://git@git.dev.genebox.cn:7999/app/react-native-wechat.git",
		"ssh://git@git.dev.genebox.cn:7999/bioinfo/laso_data_pipeline.git"
        ]

if __name__ == "__main__":
    for i, name in enumerate(repo_name):
        print(name)
        os.chdir("/Users/jiangyu/Documents/Laso/bitbucket")
        cloneCmd = "git clone --bare %s" % gitlab[i]
        status, output = commands.getstatusoutput(cloneCmd)
        print(cloneCmd)
        print("clone status: %s" % status)

        if status == 0:
			# 修改路径
            os.chdir("/Users/jiangyu/Documents/Laso/bitbucket/%s" % (gitlab[i].split('/')[-1]))
            pushCmd = "git push --mirror %s" % bitbucket[i]
            status, output = commands.getstatusoutput(pushCmd)
            print(pushCmd)
            print("push status: %s" % status)
            if status != 0:
                sys.exit(1)
			# 注意删除路径
            commands.getstatusoutput("rm -rf /Users/jiangyu/Documents/Laso/bitbucket/%s" % (gitlab[i].split('/')[-1]))

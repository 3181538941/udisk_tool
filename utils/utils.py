#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2023/1/10
# @file utils.py
import os
import json
import collections
import logging
from pprint import pprint, pformat
from .setting import Setting


class ERROR:
    """
    异常类
    """

    @staticmethod
    def FILE_NOT_EXISTS(path):
        return FileNotFoundError(f"No such file or directory: {path!r}")

    # @staticmethod
    # def FileExistsError():


def exec_(path: str):
    """
    打开文件或路径
    :param path: 文件或目录的绝对路径
    :raise FileNotFoundError
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"No such file or directory: {path!r}")
    if os.path.isfile(path):
        return os.popen(path)
    return os.popen(f"explorer {path}")


if __name__ == '__main__':
    ...
    # print(open_('123'))
    # print(open_(r'A:\01_软件环境\geek.exe'))
    # print(open_(r'A:\01_软件环境'))

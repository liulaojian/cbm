#-*- coding:utf-8 -*-
#!/usr/bin/env python

import math
import types

import CbmRtti

# 记录对象允许复制的属性类型
obj_types_set = set([types.IntType, types.FloatType, types.StringType, types.LongType])

def CopyAttribsOfCbmType(cbm_type, obj1, obj2):
    if cbm_type in CbmRtti.info:
        # print CbmRtti.info[cbm_type]
        for name, func in CbmRtti.info[cbm_type].items():
            if not hasattr(obj1, name) or not hasattr(obj2, name):continue
            a = getattr(obj1, name)
            # print name, a
            if a is not None:
                setattr(obj2, name, func(a))

def GetAttribsOfCbmType(cbm_type, obj1):
    attribs = {}
    if cbm_type in CbmRtti.info:
        for name, func in CbmRtti.info[cbm_type].items():
            if not hasattr(obj1, name):continue
            a = getattr(obj1, name)
            if a is not None:
                attribs[name] = func(a)
    return attribs

def CopyAttribs(obj1, obj2):
    for name in dir(obj1):
        if not hasattr(obj2, name):continue
        if name.startswith('__'):continue
        a = getattr(obj1, name)
        if type(a) in obj_types_set:
            setattr(obj2, name, a)

def GetAttribs(obj1):
    attribs = {}
    for name in dir(obj1):
        # if not hasattr(obj1, name):continue
        if name.startswith('__'):continue
        attribs[name] = getattr(obj1, name)
    return attribs

def DifficultEval1(decay_alpha):
    if decay_alpha < 0.003:
        return 1
    elif decay_alpha < 0.05:
        return 2
    else:
        return 3

def DifficultEval2(permeability_lambda):
    if permeability_lambda > 10:
        return 1
    elif permeability_lambda > 0.1:
        return 2
    else:
        return 3

def DifficultEvalHelper(k1, k2):
    difficult_eval_result_dict = [1, 4, 5, 4, 2, 6, 5, 6, 3]
    if k1 < 1 or k1 > 3 or k2 < 1 or k2 > 3:
        return 0
    else:
        return difficult_eval_result_dict[k1 * 3 + k2 - 4]

def PermeabilityString(permeability_k):
    if permeability_k < 5:
        return "低渗煤层"
    elif permeability_k < 20:
        return "中渗煤层"
    else:
        return "高渗煤层"

def EvalDifficultString(eval):
    eval_difficult_string = ["容易抽采", "可以抽采", "较难抽采", "容易抽采~可以抽采", "容易抽采~较难抽采", "可以抽采~较难抽采"]
    if eval < 1 or eval > 6:
        return "NULL"
    else:
        return eval_difficult_string[eval - 1]
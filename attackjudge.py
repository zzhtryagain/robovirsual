import armorDetect as ad
import math
armor_list = [-1 for i in range(30)]  # 创建队列
armor_dict = {}
def func_mid(armorgroup, args = None):                  # 选择离中心最近的装甲
    ad.target_num = args                                # 关闭数字检测
    def center(mid):                                    # 装甲中心到准心的距离
        return math.sqrt((mid[0]-320)**2 + (mid[1]-240)**2)
    mid = [center(armor.mid) for armor in armorgroup]
    return armorgroup[mid.index(min(mid))]

def func_near(armorgroup, args = None):                 # 选择距离最近的装甲
    ad.target_num = args                                # 关闭数字检测
    dist_group = [armor.dist for armor in armorgroup]   # 装甲测距
    return armorgroup[dist_group.index(min(dist_group))]
# 以下两个功能得确定数字识别率才能使用
def func_number_static(armorgroup, args):               # 静态选择固定数字
    pass

def func_number_auto(armorgroup, args):                 # 动态选择固定数字
    '''
    策略说明：如果识别到多个数字的情况，记录10帧
    每一帧会记录检测到的数字和距离，离准心的距离
    没检测到的时候会填充-1
    然后检测识别到数字最多的一个
    可以套用mid，near等函数来综合决策
    也可以只跟随出现次数最多的数字
    '''
    pass
    # global armor_list
    # if not armorgroup:
    #     armor_list.append(-1)
    # else:
    #     for armor in armorgroup:
    #         armor_list.append(armor.digit)
    # armor_set = list(set(armor_list))
    # for item in armor_set:
    #     armor_dict[item] = armor_set.count(item)
    # if(armor_dict[])

mid = 'ATTACK_MID'
near = 'ATTACK_NEAR'
static = 'ATTACK_NUMBER_STATIC'
auto = 'ATTACK_NUMBER_AUTO'
attack_mode = {               # 攻击策略字典
    mid: func_mid,
    near: func_near,
    static: func_number_static,
    auto: func_number_auto
}
def judge(armorgroup, attack = mid, args = None):
    mode = attack_mode.get(attack) # 从字典中获取攻击策略函数
    return mode(armorgroup, args)

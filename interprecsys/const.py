"""
Constants file for InterpRecSys

@Author: Zeyu Li <zyli@cs.ucla.edu> or <zeyuli@g.ucla.edu>
"""

import os


class Constant(object):
    """
    Constants of InterpRecSys
    """

    # Directory Structure
    # - data
    #   - graph: save graph objects
    #   - raw: all raw files
    #   - parse: all parsed files (order neighbors)

    DATA_DIR = os.getcwd() + "/data/"

    GRAPH_DIR = os.getcwd() + "/data/graph/"
    RAW_DIR = os.getcwd() + "/data/raw/"
    PARSE_DIR = os.getcwd() + "/data/parse/"
    LOG_DIR = os.getcwd() + "/log/"

    RANDOM_SEED = 723


class Config:
    def __init__(self, dataset):
        self.dataset = dataset

        self.TRAIN_FILE = Constant.PARSE_DIR + dataset + "/train.csv"
        self.TEST_FILE = Constant.PARSE_DIR + dataset + "/test.csv"
        self.CUS_FILE = Constant.PARSE_DIR + dataset + "/cus.csv"
        self.OBJ_FILE = Constant.PARSE_DIR + dataset + "/obj.csv"

        # Columns of categorical features
        # CAT_COL, NUM_COL, IGN_COL
        if self.dataset == "toy":
            self.CAT_COL = [
                'ps_ind_02_cat', 'ps_ind_04_cat', 'ps_ind_05_cat',
                'ps_car_01_cat', 'ps_car_02_cat', 'ps_car_03_cat',
                'ps_car_04_cat', 'ps_car_05_cat', 'ps_car_06_cat',
                'ps_car_07_cat', 'ps_car_08_cat', 'ps_car_09_cat',
                'ps_car_10_cat', 'ps_car_11_cat',
            ]

            self.NUM_COL = [
                # # binary
                # "ps_ind_06_bin", "ps_ind_07_bin", "ps_ind_08_bin",
                # "ps_ind_09_bin", "ps_ind_10_bin", "ps_ind_11_bin",
                # "ps_ind_12_bin", "ps_ind_13_bin", "ps_ind_16_bin",
                # "ps_ind_17_bin", "ps_ind_18_bin",
                # "ps_calc_15_bin", "ps_calc_16_bin", "ps_calc_17_bin",
                # "ps_calc_18_bin", "ps_calc_19_bin", "ps_calc_20_bin",
                # numeric
                "ps_reg_01", "ps_reg_02", "ps_reg_03",
                "ps_car_12", "ps_car_13", "ps_car_14", "ps_car_15",
            ]

            self.IGN_COL = [
                "id", "target",
                "ps_calc_01", "ps_calc_02", "ps_calc_03", "ps_calc_04",
                "ps_calc_05", "ps_calc_06", "ps_calc_07", "ps_calc_08",
                "ps_calc_09", "ps_calc_10", "ps_calc_11", "ps_calc_12",
                "ps_calc_13", "ps_calc_14",
                "ps_calc_15_bin", "ps_calc_16_bin", "ps_calc_17_bin",
                "ps_calc_18_bin", "ps_calc_19_bin", "ps_calc_20_bin"
            ]

        elif self.dataset == "criteoDAC":
            self.CAT_COL = ["C{:02}".format(x) for x in range(1, 26)]
            self.NUM_COL = ["I{:02}".format(x) for x in range(1, 13)]
            self.IGN_COL = []

        else:
             raise ValueError("Invalid dataset {}".format(dataset))



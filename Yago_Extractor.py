import csv
import json


class YagoExtractor:

    def __init__(self):

        # Loading Config file
        with open('config.json') as configFile:
            config = json.load(configFile)
            self.yago_files = config['yagoFiles']

    def label(self, name):
        """
        :param name: search Labels for it's tag
        :return: name's label tag or None if not found
        """

        # Loading Yago Labels
        with open(self.yago_files['Labels'], encoding='utf-8') as LabelFile:
            yago_labels = csv.reader(LabelFile, delimiter="\t")

            label_tag = None

            for label in yago_labels:
                if name in label[3]:  # Match found !
                    label_tag = label[1]
                    break

            if label_tag:
                for label in yago_labels:  # Search yago_labels from beginning to write matched lines into label's file
                    if label_tag == label[1]:
                        with open(file="./extracted_label/{}.tsv".format(label_tag), mode='a') as label_file:
                            label_file.write(str(label) + '\n')
            
        return label_tag

    def type(self, Name):

        # Loading Yago Types
        with open(self.yago_files['Types'], encoding='utf-8') as LabelFile:
            self.types = csv.reader(LabelFile, delimiter="\t")

    def fact(self, Name):

        # Loading Yago Facts
        with open(self.yago_files['Facts'], encoding='utf-8') as LabelFile:
            self.facts = csv.reader(LabelFile, delimiter="\t")

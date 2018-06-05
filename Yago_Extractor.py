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

                if label_tag is None:  # Trying to match a name with yago labels
                    if name in label[3]:
                        label_tag = label[1]
                        with open(file="./{}.tsv".format(label_tag),
                                  mode='a') as label_file:  # Writing matched label to file
                            label_file.write(str(label) + '\n')

                else:  # trying to find other lines matched with tag
                    if label_tag == label[1]:
                        with open(file="./{}.tsv".format(label_tag),
                                  mode='a') as label_file:  # Writing matched label to file
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

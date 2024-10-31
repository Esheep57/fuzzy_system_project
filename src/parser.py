# src/parser.py
import pandas as pd
from lxml import etree
from typing import List, Union
from .models import (
    FuzzySystemModel, FuzzyVariable, FuzzyTerm, Shape,
    TrapezoidShape, TriangularShape, GaussianShape, LeftGaussianShape, RightGaussianShape,
    Rule, Clause, Consequent, TrainingSample
)

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, params: List[float]) -> Shape:
        shape_type = shape_type.lower()
        if shape_type == 'trapezoidshape':
            if len(params) != 4:
                raise ValueError(f"TrapezoidShape需要4個參數，但獲取到{len(params)}個")
            return TrapezoidShape(type='TrapezoidShape', param1=params[0], param2=params[1], param3=params[2], param4=params[3])
        elif shape_type == 'triangularshape':
            if len(params) != 3:
                raise ValueError(f"TriangularShape需要3個參數，但獲取到{len(params)}個")
            return TriangularShape(type='TriangularShape', param1=params[0], param2=params[1], param3=params[2])
        elif shape_type == 'gaussianshape':
            if len(params) != 2:
                raise ValueError(f"GaussianShape需要2個參數（mean, sigma），但獲取到{len(params)}個")
            return GaussianShape(type='GaussianShape', mean=params[0], sigma=params[1])
        elif shape_type == 'leftgaussianshape':
            if len(params) != 2:
                raise ValueError(f"LeftGaussianShape需要2個參數（mean, sigma），但獲取到{len(params)}個")
            return LeftGaussianShape(type='LeftGaussianShape', mean=params[0], sigma=params[1])
        elif shape_type == 'rightgaussianshape':
            if len(params) != 2:
                raise ValueError(f"RightGaussianShape需要2個參數（mean, sigma），但獲取到{len(params)}個")
            return RightGaussianShape(type='RightGaussianShape', mean=params[0], sigma=params[1])
        else:
            raise ValueError(f"未知的形狀類型: {shape_type}")

class FuzzySystemParser:
    def __init__(self, xml_path: str):
        self.xml_path = xml_path
        self.tree = etree.parse(xml_path)
        self.root = self.tree.getroot()
        self.ns = {'ns': 'http://www.ieee1855.org'}

    def parse(self) -> FuzzySystemModel:
        # 解析 fuzzySystem 屬性
        fuzzy_system_name = self.root.get('name')
        network_address = self.root.get('networkAddress')

        model = FuzzySystemModel(
            name=fuzzy_system_name,
            network_address=network_address
        )

        # 解析模糊變數
        knowledge_base = self.root.find('ns:knowledgeBase', namespaces=self.ns)
        for fv in knowledge_base.findall('ns:fuzzyVariable', namespaces=self.ns):
            fuzzy_variable = self.parse_fuzzy_variable(fv)
            model.fuzzy_variables.append(fuzzy_variable)

        # 解析規則
        rule_base = self.root.find('ns:mamdaniRuleBase', namespaces=self.ns)
        for rule_elem in rule_base.findall('ns:rule', namespaces=self.ns):
            rule = self.parse_rule(rule_elem)
            model.rules.append(rule)

        return model

    def parse_fuzzy_variable(self, fv_elem) -> FuzzyVariable:
        name = fv_elem.get('name')
        scale = fv_elem.get('scale')
        domain_left = float(fv_elem.get('domainleft'))
        domain_right = float(fv_elem.get('domainright'))
        var_type = fv_elem.get('type')
        accumulation = fv_elem.get('accumulation')
        defuzzifier = fv_elem.get('defuzzifier')
        default_value = float(fv_elem.get('defaultValue'))

        fuzzy_variable = FuzzyVariable(
            name=name,
            scale=scale,
            domain_left=domain_left,
            domain_right=domain_right,
            var_type=var_type,
            accumulation=accumulation,
            defuzzifier=defuzzifier,
            default_value=default_value
        )

        for term_elem in fv_elem.findall('ns:fuzzyTerm', namespaces=self.ns):
            term = self.parse_fuzzy_term(term_elem)
            fuzzy_variable.terms.append(term)

        return fuzzy_variable

    def parse_fuzzy_term(self, term_elem) -> FuzzyTerm:
        name = term_elem.get('name')
        complement = term_elem.get('complement') == 'true'

        # 假設每個 fuzzyTerm 只有一個形狀元素
        shape_elem = list(term_elem)[0]
        shape_type = etree.QName(shape_elem).localname  # 去除命名空間
        params = [float(param) for param in shape_elem.attrib.values()]

        shape = ShapeFactory.create_shape(shape_type, params)

        return FuzzyTerm(
            name=name,
            complement=complement,
            shape=shape
        )

    def parse_rule(self, rule_elem) -> Rule:
        name = rule_elem.get('name')
        connector = rule_elem.get('connector')
        weight = float(rule_elem.get('weight'))

        antecedent = rule_elem.find('ns:antecedent', namespaces=self.ns)
        clauses = []
        for clause_elem in antecedent.findall('ns:clause', namespaces=self.ns):
            variable = clause_elem.find('ns:variable', namespaces=self.ns).text
            term = clause_elem.find('ns:term', namespaces=self.ns).text
            clauses.append(Clause(variable=variable, term=term))

        consequent_elem = rule_elem.find('ns:consequent/ns:then/ns:clause', namespaces=self.ns)
        consequent_variable = consequent_elem.find('ns:variable', namespaces=self.ns).text
        consequent_term = consequent_elem.find('ns:term', namespaces=self.ns).text

        consequent = Consequent(variable=consequent_variable, term=consequent_term)

        return Rule(
            name=name,
            connector=connector,
            weight=weight,
            antecedents=clauses,
            consequent=consequent
        )

    def parse_training_data(self, excel_path: str) -> List[TrainingSample]:
        df = pd.read_excel(excel_path)

        required_columns = ['KUWA_score', 'BCI_weighted', 'JenPin_score', 'Student_level']
        if not all(column in df.columns for column in required_columns):
            raise ValueError(f"Excel 檔案必須包含以下欄位：{required_columns}")

        training_samples = []
        for _, row in df.iterrows():
            sample = TrainingSample(
                KUWA_score=float(row['KUWA_score']),
                BCI_weighted=float(row['BCI_weighted']),
                JenPin_score=float(row['JenPin_score']),
                Student_level=row['Student_level']
            )
            training_samples.append(sample)

        return training_samples

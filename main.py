# main.py
from src.parser import FuzzySystemParser
from src.models import (
    TrapezoidShape, TriangularShape, GaussianShape,
    LeftGaussianShape, RightGaussianShape
)

def main():
    xml_path = 'data/cimodel.xml'
    excel_path = 'data/training_data.xlsx'

    parser = FuzzySystemParser(xml_path)
    model = parser.parse()

    print(f"模糊系統名稱: {model.name}")
    print(f"網絡地址: {model.network_address}\n")

    print("模糊變數:")
    for fv in model.fuzzy_variables:
        print(f"  變數名稱: {fv.name}, 類型: {fv.var_type}")
        for term in fv.terms:
            shape = term.shape
            if isinstance(shape, TrapezoidShape):
                shape_info = f"TrapezoidShape, 參數: [{shape.param1}, {shape.param2}, {shape.param3}, {shape.param4}]"
            elif isinstance(shape, TriangularShape):
                shape_info = f"TriangularShape, 參數: [{shape.param1}, {shape.param2}, {shape.param3}]"
            elif isinstance(shape, GaussianShape):
                shape_info = f"GaussianShape, mean: {shape.mean}, sigma: {shape.sigma}"
            elif isinstance(shape, LeftGaussianShape):
                shape_info = f"LeftGaussianShape, mean: {shape.mean}, sigma: {shape.sigma}"
            elif isinstance(shape, RightGaussianShape):
                shape_info = f"RightGaussianShape, mean: {shape.mean}, sigma: {shape.sigma}"
            else:
                shape_info = f"未知形狀: {shape.type}, 參數: {shape.params}"

            complement_info = " (補數)" if term.complement else ""
            print(f"    模糊術語: {term.name}{complement_info}, 形狀: {shape_info}")
        print()

    print("規則:")
    for rule in model.rules:
        antecedents = ' AND '.join([f"{clause.variable} 是 {clause.term}" for clause in rule.antecedents])
        print(f"  規則名稱: {rule.name}")
        print(f"    如果 {antecedents}，則 {rule.consequent.variable} 是 {rule.consequent.term}\n")
    
    # 讀取訓練資料
    try:
        training_samples = parser.parse_training_data(excel_path)
        print("訓練資料:")
        for sample in training_samples:
            print(f"  KUWA_score: {sample.KUWA_score}, BCI_weighted: {sample.BCI_weighted}, JenPin_score: {sample.JenPin_score}, Student_level: {sample.Student_level}")
    except Exception as e:
        print(f"讀取訓練資料時發生錯誤: {e}")

if __name__ == "__main__":
    main()

import pandas as pd
from project import DataAnalyzer

def test_numerical_analysis():
    # i create a simple DataFrame
    data = {
        "age": [20, 30, 40],
        "score": [80, 90, 100]
    }
    df = pd.DataFrame(data)
    analyzer = DataAnalyzer("dummy.csv")
    analyzer._df = df
    analyzer.numerical_analyze()

    statistics = analyzer.statis["numeric"]

    assert "age" in statistics
    assert statistics["age"]["mean"] == 30
    assert statistics["age"]["min"] == 20
    assert statistics["age"]["max"] == 40
    assert statistics["age"]["mean"] == 30

    assert "score" in statistics
    assert statistics["score"]["mean"] == 90
    assert statistics["score"]["min"] ==80
    assert statistics["score"]["max"] == 100
    assert statistics["score"]["median"] == 90

def test_categorical_analysis():
    data = {
        "gender": ["M", "F", "F", "M", "F"]
    }
    df = pd.DataFrame(data)

    analyzer = DataAnalyzer("dummy.csv")
    # Inject DataFrame directly for testing purposes
    analyzer._df = df
    analyzer.analyze_categorical()

    statistics = analyzer.statis["categoric"]

    assert "gender" in statistics
    assert statistics["gender"]["frequency"]["F"] == 3
    assert statistics["gender"]["frequency"]["M"] == 2

def test_empty_dataframe():
    df = pd.DataFrame()

    analyzer = DataAnalyzer("dummy.csv")
    analyzer._df = df

    analyzer.numerical_analyze()
    analyzer.analyze_categorical()

    assert analyzer.statis["numeric"] == {}
    assert analyzer.statis["categoric"] == {}

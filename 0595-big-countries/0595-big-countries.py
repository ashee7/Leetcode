import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area'] >= 3e6) | (world['population'] >= 25e6)]
    return df[['name','population','area']]
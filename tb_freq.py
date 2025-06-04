# %%

import pandas as pd
import sqlalchemy

df = pd.read_csv("data/points_tmw.csv")
df.head()

engine = sqlalchemy.create_engine("sqlite:///data/tmw.db")

df.to_sql("points", engine, if_exists="replace", index=False)

# %%

freq_produto = (df.groupby(["descProduto"])[["idTransacao"]]
                .count())
freq_produto["Freq. Abs. Acum"] = freq_produto["idTransacao"].cumsum()

freq_produto["Freq. Rel."] = freq_produto["idTransacao"] / freq_produto["idTransacao"].sum()

freq_produto["Freq. Rel. Acum."] = freq_produto["Freq. Rel."].cumsum()
freq_produto

# %%
freq_categoria = (df.groupby(["descCategoriaProduto"])[["idTransacao"]]
                  .count()
                  .rename(columns={"idTransacao": "Freq. Abs"}))

freq_categoria["Freq. Abs. Acum."] = freq_categoria["Freq. Abs"].cumsum()

freq_categoria["Freq. Rel"] = freq_categoria["Freq. Abs"] / freq_categoria["Freq. Abs"].sum()

freq_categoria["Freq. Rel. Acum"] = freq_categoria["Freq. Rel"].cumsum()
freq_categoria
import plotly.express as px
import pandas as pd

# Dados de exemplo
df = pd.DataFrame({
    'Vgs (V)': [0.1, 0.2, 0.3, 0.4, 0.5],
    'Ids (mA)': [0.02, 0.04, 0.09, 0.15, 0.22]
})

fig = px.line(df, x='Vgs (V)', y='Ids (mA)', title="Curva de Transferência")
fig.write_html("analysis/graph.html")

import plotly.express as px
import pandas as pd

# Dados de exemplo
df = pd.DataFrame({
    'Vgs (V)': [0.1, 0.2, 0.3, 0.4, 0.5],
    'Ids (mA)': [0.02, 0.04, 0.09, 0.15, 0.22]
})

# Criar o gráfico
fig = px.line(df, x='Vgs (V)', y='Ids (mA)', title="Curva de Transferência")

# Salvar o gráfico como arquivo HTML
fig.write_html("docs/graph.html")

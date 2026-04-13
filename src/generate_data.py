import pandas as pd
import numpy as np

np.random.seed(42)

n = 2000

df = pd.DataFrame({
    'offer_count': np.random.randint(1, 5, n),
    'isRecurrentUser': np.random.randint(0, 2, n),
    'antiguedadIngresos': np.random.randint(1, 20, n),
    'offered_rate': np.random.uniform(0.1, 0.5, n),
    'numeroPagos': np.random.randint(1, 36, n),
    'fico': np.random.randint(500, 850, n),
    'isFraud': np.random.randint(0, 2, n),
})

# generar target con lógica (esto es clave)
df['took_loan'] = (
    0.3*df['offer_count'] +
    0.5*df['isRecurrentUser'] -
    0.4*df['offered_rate'] -
    0.3*(df['numeroPagos']/36) +
    np.random.normal(0, 0.5, n)
)

df['took_loan'] = (df['took_loan'] > df['took_loan'].median()).astype(int)

df.to_csv('data/synthetic_data.csv', index=False)

print("Dataset created")

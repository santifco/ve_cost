import streamlit as st
import pandas as pd

# Configurar la página
st.set_page_config(page_title="Calculadora de Costo Total de Propiedad (TCO)", layout="wide")

st.title("Calculadora de Costo Total de Propiedad (TCO)")

# Crear dos columnas principales, haciendo la primera columna más ancha
col1,spacer,col2 = st.columns([1.6,0.2, 2])  # Col1 será más ancha que Col2

with col1:
    st.header("Entradas del Usuario")
    # Crear dos subcolumnas dentro de la primera columna principal
    subcol1, subcol2 = st.columns(2)
    
    # Entradas del usuario para el vehículo eléctrico en la primera subcolumna
    with subcol1:
        st.subheader("Vehículo Eléctrico")
        km_mensuales_ev = st.number_input("Kilómetros recorridos por mes (EV)", min_value=1, value=2250, step=500)
        km_anuales_ev = km_mensuales_ev*12
        with st.expander("Purchase Cost"):
            costo_ev = st.number_input("Costo del vehículo (EV) ($)", min_value=0.0, value=30000.0, step=1000.0)
            tasa_patentamiento_ev = st.number_input("Tasa de patentamiento (EV) (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.1) / 100
            valor_residual_ev = st.number_input("Valor residual del vehículo (EV) ($)", min_value=0.0, value=15000.0, step=500.0)
        with st.expander("Operating Cost"):
            pago_patente_anual_ev = st.number_input("Pago de patente anual (EV) ($)", min_value=0.0, value=0.0, step=100000.0)
            pago_seguro_anual_ev = st.number_input("Pago de seguro anual (EV) ($)", min_value=0.0, value=300000.0, step=100000.0)
            mantenimiento_anual_ev = st.number_input("Mantenimiento anual (EV) ($)", min_value=0.0, value=0.0, step=100000.0)
            eficiencia_ev = st.number_input("Eficiencia del vehículo (EV) (kWh/km)", min_value=0.1, value=1.2, step=0.1)
            precio_electricidad = st.number_input("Precio de la electricidad (por kWh)", min_value=0.0, value=51.27, step=10.0)

    # Entradas del usuario para el vehículo a gasolina en la segunda subcolumna
    with subcol2:
        st.subheader("Vehículo a Gasolina")
        km_mensuales_gas = st.number_input("Kilómetros recorridos por mes (Gasolina)", min_value=1, value=2250, step=500)
        km_anuales_gas = km_mensuales_gas*12
        with st.expander("Purchase Cost"):
            costo_gas = st.number_input("Costo del vehículo (Gasolina) ($)", min_value=0.0, value=20000.0, step=1000.0)
            tasa_patentamiento_gas = st.number_input("Tasa de patentamiento (Gasolina) (%)", min_value=0.0, max_value=100.0, value=3.0, step=0.1) / 100
            valor_residual_gas = st.number_input("Valor residual del vehículo (Gasolina) ($)", min_value=0.0, value=10000.0, step=500.0)
        with st.expander("Operating Cost"):
            pago_patente_anual_gas = st.number_input("Pago de patente anual (Gasolina) ($)", min_value=0.0, value=10000.0, step=100000.0)
            pago_seguro_anual_gas = st.number_input("Pago de seguro anual (Gasolina) ($)", min_value=0.0, value=300000.0, step=100000.0)
            mantenimiento_anual_gas = st.number_input("Mantenimiento anual (Gasolina) ($)",min_value=0.0, value=300000.0, step=100000.0)
            eficiencia_gas = st.number_input("Eficiencia del vehículo (Gasolina) (L/km)", min_value=0.0, value=0.08, step=0.01)
            precio_gasolina = st.number_input("Precio de la gasolina (por litro)", min_value=0.0, value=1200.0, step=100.0)

# Función para calcular el costo total por km y por año
def calcular_costo_total(km_anuales, costo_vehiculo, tasa_patentamiento, valor_residual, pago_patente_anual, pago_seguro_anual, mantenimiento_anual, eficiencia, precio_energia, tipo_vehiculo):
    consumo_por_km = eficiencia 
    costo_energia_por_km = consumo_por_km * precio_energia

    costo_depreciacion_anual = (costo_vehiculo - valor_residual) / km_anuales
    costo_patente_anual = pago_patente_anual / km_anuales
    costo_seguro_anual = pago_seguro_anual / km_anuales
    costo_patente_seguro_anual = costo_patente_anual + costo_seguro_anual
    costo_mantenimiento_anual = mantenimiento_anual / km_anuales

    costo_total_por_km = (costo_energia_por_km + costo_depreciacion_anual + 
                          costo_patente_anual + costo_seguro_anual + costo_mantenimiento_anual)

    costo_total_anual = costo_total_por_km * km_anuales

    return costo_patente_seguro_anual,costo_energia_por_km,costo_depreciacion_anual,costo_mantenimiento_anual,costo_total_por_km,costo_total_anual

# Calcular costos para vehículo eléctrico
costo_patente_seguro_anual_ev,costo_energia_por_km_ev,costo_depreciacion_anual_ev,costo_mantenimiento_anual_ev,costo_total_por_km_ev, costo_total_anual_ev = calcular_costo_total(km_anuales_ev, costo_ev, tasa_patentamiento_ev, valor_residual_ev, pago_patente_anual_ev, pago_seguro_anual_ev, mantenimiento_anual_ev, eficiencia_ev, precio_electricidad, "eléctrico")

# Calcular costos para vehículo a gasolina
costo_patente_seguro_anual_gas,costo_energia_por_km_gas,costo_depreciacion_anual_gas,costo_mantenimiento_anual_gas,costo_total_por_km_gas, costo_total_anual_gas = calcular_costo_total(km_anuales_gas, costo_gas, tasa_patentamiento_gas, valor_residual_gas, pago_patente_anual_gas, pago_seguro_anual_gas, mantenimiento_anual_gas, eficiencia_gas, precio_gasolina, "gasolina")


with col2:
    # Crear un contenedor para los resultados con fondo gris claro
    with st.container(border=True):

        st.subheader("Costo Total de Propiedad Estimado (TCO)")

        subcol1, subcol2 = st.columns(2)     
        
        with subcol1:
            # Mostrar resultados para vehículo eléctrico
            st.write("**Vehículo Eléctrico**")
            st.write(f"Costo Energía por km: **{costo_energia_por_km_ev:.2f} $/km**")
            st.write(f"Costo Depreciación por km: **{costo_depreciacion_anual_ev:.2f} $/km**")
            st.write(f"Costo Mantenimiento por km: **{costo_mantenimiento_anual_ev:.2f} $/km**")
            st.write(f"Costo Patente y Seguro por km: **{costo_patente_seguro_anual_ev:.2f} $/km**")
            st.write(f"Costo total por km: **{costo_total_por_km_ev:.2f} $/km**")
            st.write(f"Costo total anual: **{costo_total_anual_ev:,.0f} $/año**")
        
        with subcol2:
        # Mostrar resultados para vehículo a gasolina
            st.write("**Vehículo a Gasolina**")
            st.write(f"Costo Energía por km: **{costo_energia_por_km_gas:.2f} $/km**")
            st.write(f"Costo Depreciación por km: **{costo_depreciacion_anual_gas:.2f} $/km**")
            st.write(f"Costo Mantenimiento por km: **{costo_mantenimiento_anual_gas:.2f} $/km**")
            st.write(f"Costo Patente y Seguro por km: **{costo_patente_seguro_anual_gas:.2f} $/km**")
            st.write(f"Costo total por km: **{costo_total_por_km_gas:.2f} $/km**")
            st.write(f"Costo total anual: **{costo_total_anual_gas:,.0f} $/año**")

    with st.container(border=True):

        años = [1,2,3,4,5,6,7,8,9,10] 

        # Crear un DataFrame para almacenar los costos por kilómetro
        data = {
            "Kilómetros Mensuales": años,
            "Vehículo Eléctrico": [],
            "Vehículo a Gasolina": []
        }

        for km in años:
            km = km*12
            # Calcular el costo por kilómetro para ambos tipos de vehículos
            costo_por_km_ev= calcular_costo_total(km, costo_ev, tasa_patentamiento_ev, valor_residual_ev, pago_patente_anual_ev, pago_seguro_anual_ev, mantenimiento_anual_ev, eficiencia_ev, precio_electricidad, "eléctrico")[4]
            costo_por_km_gas= calcular_costo_total(km, costo_gas, tasa_patentamiento_gas, valor_residual_gas, pago_patente_anual_gas, pago_seguro_anual_gas, mantenimiento_anual_gas, eficiencia_gas, precio_gasolina, "gasolina")[4]
            costo_por_km_ev=  costo_por_km_ev*km
            costo_por_km_gas= costo_por_km_gas*km
            # Agregar los costos por kilómetro al DataFrame
            data["Vehículo Eléctrico"].append(costo_por_km_ev)
            data["Vehículo a Gasolina"].append(costo_por_km_gas)

        # Crear el DataFrame
        df = pd.DataFrame(data)

        # Establecer los kilómetros mensuales como índice del DataFrame
        df.set_index("Kilómetros Mensuales", inplace=True)
        # st.write(df)
        # Mostrar el gráfico con Streamlit
        st.subheader("Cumulative annual owning and operating costs")
        st.line_chart(df, use_container_width=True)
        
        

# Permitir al usuario ingresar una lista de kilómetros mensuales
km_mensuales = st.text_input("Ingrese los kilómetros mensuales separados por coma (por ejemplo: 1000,2000,3000)", value="500,1000,2000,3000,4000,5000")

# Convertir los valores ingresados a una lista de números
km_mensuales = [int(km.strip()) for km in km_mensuales.split(',') if km.strip()]

col1,spacer,col2 = st.columns([1,0.1, 1])  # Col1 será más ancha que Col2

if km_mensuales:
    with col1:
    # Crear un DataFrame para almacenar los costos por kilómetro
        data = {
            "Kilómetros Mensuales": km_mensuales,
            "Vehículo Eléctrico": [],
            "Vehículo a Gasolina": []
        }

        for km in km_mensuales:
            km = km*12
            # Calcular el costo por kilómetro para ambos tipos de vehículos
            costo_por_km_ev = calcular_costo_total(km, costo_ev, tasa_patentamiento_ev, valor_residual_ev, pago_patente_anual_ev, pago_seguro_anual_ev, mantenimiento_anual_ev, eficiencia_ev, precio_electricidad, "eléctrico")[4]
            costo_por_km_gas = calcular_costo_total(km, costo_gas, tasa_patentamiento_gas, valor_residual_gas, pago_patente_anual_gas, pago_seguro_anual_gas, mantenimiento_anual_gas, eficiencia_gas, precio_gasolina, "gasolina")[4]

            # Agregar los costos por kilómetro al DataFrame
            data["Vehículo Eléctrico"].append(costo_por_km_ev)
            data["Vehículo a Gasolina"].append(costo_por_km_gas)

        # Crear el DataFrame
        df = pd.DataFrame(data)

        # Establecer los kilómetros mensuales como índice del DataFrame
        df.set_index("Kilómetros Mensuales", inplace=True)

        # Mostrar el gráfico con Streamlit
        st.subheader("Comparación de Costo por Kilómetro para Diferentes Valores de Kilómetros Mensuales")
        st.line_chart(df, use_container_width=True)

    with col2:
        data = {
            "Kilómetros Mensuales": km_mensuales,
            "Vehículo Eléctrico": [],
            "Vehículo a Gasolina": []
        }

        for km in km_mensuales:
            km = km*12
            # Calcular el costo por kilómetro para ambos tipos de vehículos
            costo_por_km_ev= calcular_costo_total(km, costo_ev, tasa_patentamiento_ev, valor_residual_ev, pago_patente_anual_ev, pago_seguro_anual_ev, mantenimiento_anual_ev, eficiencia_ev, precio_electricidad, "eléctrico")[4]
            costo_por_km_gas= calcular_costo_total(km, costo_gas, tasa_patentamiento_gas, valor_residual_gas, pago_patente_anual_gas, pago_seguro_anual_gas, mantenimiento_anual_gas, eficiencia_gas, precio_gasolina, "gasolina")[4]
            costo_por_km_ev=  costo_por_km_ev*km/12
            costo_por_km_gas= costo_por_km_gas*km/12
            # Agregar los costos por kilómetro al DataFrame
            data["Vehículo Eléctrico"].append(costo_por_km_ev)
            data["Vehículo a Gasolina"].append(costo_por_km_gas)

        # Crear el DataFrame
        df = pd.DataFrame(data)

        # Establecer los kilómetros mensuales como índice del DataFrame
        df.set_index("Kilómetros Mensuales", inplace=True)

        # Mostrar el gráfico con Streamlit
        st.subheader("Comparación de Costo Total para Diferentes Valores de Kilómetros Mensuales")
        st.line_chart(df, use_container_width=True)    
    
st.header("Inversión")
with st.expander("Purchase Cost"):
    costo_vehiculo = st.number_input("Costo del vehículo ($)", min_value=0.0, value=40000.0, step=1000.0)
    tasa_patentamiento = st.number_input("Tasa de patentamiento  (%)", min_value=0.0, max_value=200.0, value=0.0, step=0.1) / 100
    valor_residual   = st.number_input("Valor residual del vehículo ($)", min_value=0.0, value=16000.0, step=500.0)
with st.expander("Infraestructure Cost"):
    carteleria_piso = st.number_input("Cartelería y piso ($)", min_value=0.0, value=70000.0, step=1000.0)
    extension_linea_11kw = st.number_input("Extensión línea 11kW ($)", min_value=0.0, value=70000.0, step=1000.0)
with st.expander("Operating Cost"):
    sueldo_conduccion = st.number_input("Sueldo Conducción ($)", min_value=0.0, value=70000.0, step=1000.0)
    neumaticos = st.number_input("Neumaticos ($)", min_value=0.0, value=70000.0, step=1000.0)
    peajes = st.number_input("Peajes ($)", min_value=0.0, value=70000.0, step=1000.0)
with st.expander("Financial Cost"):
    pass


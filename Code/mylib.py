class mylib:
    def dqr(data): 
        
        
        import pandas as pd
        #%% Lista  de variables o columnas que tenemos
        columns = pd.DataFrame(list(data.columns.values))
        
        #%% Lista de tipos de variables 
        d_types = pd.DataFrame(data.dtypes,columns = ['D_types'])
        
        #%% Lista de datos faltantes
        missing = pd.DataFrame(data.isnull().sum(),columns=['Missing_values'])
        
        #%% lista de datos presentes
        present = pd.DataFrame(data.count(),columns=['Present_values'])
        
        #%% tabla de valores unicos 
        unique_values = pd.DataFrame(columns=['Unique_values'])
        for col in list(data.columns.values):
            unique_values.loc[col] = [data[col].nunique()]
        
        #%% Lista de valores minimos
        min_values = pd.DataFrame(columns=['Min'])
        for col in list (data.columns.values):
            try:
                min_values.loc[col] = [data[col].min()]
            except:
                pass
            
        #%% maimos
        max_values = pd.DataFrame(columns=['Max'])
        for col in list (data.columns.values):
            try:
                max_values.loc[col] = [data[col].max()]
            except:
                pass
        
        #%% crear el reporte de calidad de los datos (data quality report)
        return d_types.join(missing).join(present).join(unique_values).join(min_values).join(max_values)
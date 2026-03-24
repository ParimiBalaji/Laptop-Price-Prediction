import json
import re

path = 'laptop-price-predictor.ipynb'
try:
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            new_source = []
            modified = False
            for line in cell.get('source', []):
                # 1. df.corr()
                if 'df.corr()' in line:
                    line = line.replace('df.corr()', 'df.corr(numeric_only=True)')
                    modified = True
                
                # 2. sparse=False
                if 'sparse=False' in line:
                    line = line.replace('sparse=False', 'sparse_output=False')
                    modified = True
                
                # 3. str.replace(r'\D', '')
                if "str.replace(r'\\D', '')" in line:
                    line = line.replace("str.replace(r'\\D', '')", "str.replace(r'\\D', '', regex=True)")
                    modified = True
                
                # 4. sns.distplot
                if 'sns.distplot' in line:
                    if "np.log(df['Price'])" in line:
                        line = line.replace("sns.distplot(np.log(df['Price']))", "sns.histplot(np.log(df['Price']), kde=True)")
                    else:
                        line = re.sub(r'sns\.distplot\((.*?)\)', r'sns.histplot(\1, kde=True)', line)
                        # Fix my nested parens bug just in case it triggers on the log one if format varied
                        line = line.replace("sns.histplot(np.log(df['Price'], kde=True))", "sns.histplot(np.log(df['Price']), kde=True)")
                    modified = True
                
                # 5. ExtraTrees bootstrap bug
                if 'ExtraTreesRegressor(' in line and 'bootstrap=True' not in line:
                    line = line.replace('ExtraTreesRegressor(n_estimators', 'ExtraTreesRegressor(bootstrap=True, n_estimators')
                    modified = True
                    
                new_source.append(line)
            if modified:
                cell['source'] = new_source

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    
    print("Notebook perfectly patched.")
except Exception as e:
    print(f"Error: {e}")

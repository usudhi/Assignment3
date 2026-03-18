import subprocess
packages = ['numpy', 'pandas', 'matplotlib', 'seaborn', 'scikit-learn', 'scikit-surprise', 'shap', 'lime', 'tensorflow']
for p in packages:
    try:
        print(f'Installing {p}...')
        subprocess.run(['c:/Users/SUDHEESH/Desktop/Assignment 2 ML/.venv-310/Scripts/python.exe', '-m', 'pip', 'install', p], check=True)
        print(f'SUCCESS: {p}')
    except Exception as e:
        print(f'FAILED: {p} - {str(e)}')

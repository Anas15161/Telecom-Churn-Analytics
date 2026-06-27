import json

def fix_notebook():
    file_path = 'notebooks/model.ipynb'
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for cell in nb.get('cells', []):
        # Clear output and execution counts so it looks clean and fixed
        if 'outputs' in cell:
            cell['outputs'] = []
        if 'execution_count' in cell:
            cell['execution_count'] = None
            
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            new_source = []
            for line in source:
                # Fix the pandas append deprecation error
                if 'eval_ =lr.append(svm).append(knn)' in line:
                    line = line.replace('eval_ =lr.append(svm).append(knn).append(k_svm).append(nb).append(dt).append(rf).append(ab).append(gb).append(vc)',
                                        'eval_ = pd.concat([lr, svm, knn, k_svm, nb, dt, rf, ab, gb, vc], ignore_index=True)')
                
                # Fix dropping columns index if it was split on lines
                if '.reset_index().drop(columns = "index")' in line:
                    line = line.replace('.reset_index().drop(columns = "index")', '.reset_index(drop=True)')
                    
                new_source.append(line)
            cell['source'] = new_source

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
        f.write('\n')

if __name__ == '__main__':
    fix_notebook()
    print("Notebook fixed.")

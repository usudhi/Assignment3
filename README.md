---
## README — How to Run

### Dependencies
```bash
pip install scikit-learn numpy pandas scipy matplotlib seaborn
pip install scikit-surprise shap lime tensorflow
```

### Steps
1. Open in Jupyter: `jupyter notebook CSL7110_Assignment3_Recommender_Systems.ipynb`
2. **Kernel → Restart & Run All**
3. Cell 2 auto-downloads the MovieLens dataset (~1 MB)

### Dataset
- **MovieLens ml-latest-small:** 100,836 ratings | 9,742 movies | 610 users
- Auto-downloaded from: https://files.grouplens.org/datasets/movielens/ml-latest-small.zip

### Approximate Runtime
| Section | Time |
|---------|------|
| Parts 1–4 (CF, SVD) | ~5 min |
| Part 5 — Neural Network (Task 8) | ~10 min |
| Part 5 — RL (Task 9) | ~3 min |
| Part 6 — SHAP/LIME (Tasks 10–12) | ~5 min |

### Output Files
`eda_overview.png` · `ubcf_rmse_k.png` · `svd_scree.png`  
`mab_rewards.png` · `qlearning_rewards.png` · `nn_training.png`  
`shap_bar.png` · `shap_beeswarm.png` · `lime_explanation.png` · `final_rmse_comparison.png`

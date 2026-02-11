#!/bin/bash
echo "=== flake8 ===" > results/lint_results.txt
python3 -m flake8 computeSales.py >> results/lint_results.txt 2>&1
echo "" >> results/lint_results.txt
echo "=== pylint ===" >> results/lint_results.txt
python3 -m pylint computeSales.py >> results/lint_results.txt 2>&1
echo "Results saved in results/lint_results.txt"

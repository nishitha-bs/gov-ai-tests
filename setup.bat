@echo off
echo --- 1. Creating Virtual Environment ---
python -m venv venv

echo --- 2. Activating Environment ---
call .\venv\Scripts\activate

echo --- 3. Installing Dependencies ---
pip install -r requirements.txt

echo --- 4. Installing Playwright Browsers ---
python -m playwright install

echo --- ALL DONE! ---
echo Your environment is ready. To run tests, type: pytest
pause
## Run backend

1. Create virtual environment
```
python -m venv ./backend/venv
```
2. Activate virtual environment
  ```
  source ./backend/venv/bin/activate
```
3. Install python package
```
python -m pip install -r ./backend/requirements.txt
```
4. Run uvicorn server
```
python ./backend/run_uvicorn.py
```
5. Open documentation: <http://localhost:8000/docs>

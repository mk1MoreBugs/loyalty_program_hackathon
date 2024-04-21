## Run backend

1. Create virtual environment
```
python -m venv ./venv
```
2. Activate virtual environment
  ```
  source ./venv/bin/activate
```
3. Install python package
```
python -m pip install -r ./requirements.txt
```
4. Run uvicorn server
```
python  uvicorn app.main:app --reload
```
5. Open documentation: <http://localhost:8000/docs>

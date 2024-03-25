#!/bin/bash


cd backend
pip install fastapi
pip install "uvicorn[standard]"
uvicorn main:app --reload --port 3000 &
cd ..

echo "backend funcionando"

cd frontend/travels
npm install
npm run serve

echo "frontend funcionando"

cd ..



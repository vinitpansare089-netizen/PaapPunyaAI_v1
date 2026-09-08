FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

# Install CPU-only PyTorch
# Install CPU-only PyTorch
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Install remaining packages
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["tail","-f","/dev/null"]
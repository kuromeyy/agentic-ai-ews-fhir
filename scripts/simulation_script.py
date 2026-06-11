import requests
from datetime import datetime

WEBHOOK_URL = "http://localhost:5678/webhook-test/vital-signs"

def generate_vital_signs():
    return {
        "Patient ID": "1",
        "Timestamp": datetime.now().isoformat(),
        "Heart Rate": "75",
        "Oxygen Saturation": "99",
        "Body Temperature": "37.1",
        "Systolic Blood Pressure": "120",
        "Diastolic Blood Pressure": "90",
        "Respiratory Rate": "13" 
    }

def send_data():
    print(f"Mengirim data tunggal ke: {WEBHOOK_URL}...")
    
    payload = generate_vital_signs()
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        
        if response.status_code == 200:
            print(f"[{payload['Timestamp']}] Sukses Terkirim!")
            print(f"Respon Server: {response.text}")
        else:
            print(f"Gagal mengirim. Status Code: {response.status_code}")
            print(f"Pesan Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Tidak bisa terhubung ke n8n. Pastikan n8n sudah dijalankan.")

if __name__ == "__main__":
    send_data()
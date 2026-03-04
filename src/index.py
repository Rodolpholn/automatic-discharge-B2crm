import os
import pandas as pd
import requests
import time
from typing import List, Dict
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

class CRMIntegration:
    """Classe responsável pela integração de Leads com o CRM."""
    
    def __init__(self, url: str):
        self.url = url

    def carregar_leads(self, caminho_arquivo: str, colunas: List[str]) -> List[Dict]:
        """Lê o Excel e retorna uma lista de dicionários higienizada."""
        try:
            df = pd.read_excel(caminho_arquivo)
            # Normalização para maiúsculas para evitar erros de digitação no Excel
            df.columns = [col.upper() for col in df.columns]
            
            if not all(col in df.columns for col in colunas):
                missing = set(colunas) - set(df.columns)
                raise ValueError(f"Colunas ausentes no Excel: {missing}")
            
            return df[colunas].to_dict(orient="records")
        except Exception as e:
            print(f"[-] Erro ao carregar Excel: {e}")
            return []

    def enviar_para_crm(self, lead: Dict) -> bool:
        """Envia um único lead para o webhook via POST."""
        # Normaliza chaves para minúsculas (padrão JSON/API)
        payload = {k.lower(): v for k, v in lead.items()}
        
        try:
            response = requests.post(self.url, json=payload, timeout=10)
            if response.status_code == 200:
                print(f"[+] Sucesso: {payload.get('nome', 'Sem Nome')}")
                return True
            else:
                print(f"[!] Erro {response.status_code}: {response.text}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"[-] Falha na conexão: {e}")
            return False

def main():
    # Configurações
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CAMINHO_EXCEL = os.path.join(BASE_DIR, "..", "data", "Leads.xlsx")
    COLUNAS_ALVO = ["ID", "NOME", "CELULAR"]
    
    bot = CRMIntegration(WEBHOOK_URL)
    leads = bot.carregar_leads(CAMINHO_EXCEL, COLUNAS_ALVO)
    
    if not leads:
        print("Nenhum lead para processar.")
        return

    print(f"Iniciando processamento de {len(leads)} leads...")
    
    for lead in leads:
        bot.enviar_para_crm(lead)
        # Delay amigável para não dar Rate Limit no CRM
        time.sleep(0.5) 

if __name__ == "__main__":
    main()
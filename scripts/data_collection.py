import requests
import time
import pandas as pd 
from requests.exceptions import ConnectionError

# List of hospital URLs
hospital_urls = [
    'https://www.mayoclinic.org/',  # Mayo Clinic
    'https://my.clevelandclinic.org/',  # Cleveland Clinic
    'https://www.uhn.ca/',  # Toronto General - University Health Network
    'https://www.hopkinsmedicine.org/',  # The Johns Hopkins Hospital
    'https://www.massgeneral.org/',  # Massachusetts General Hospital
    'https://www.charite.de/',  # Charité - Universitätsmedizin Berlin
    'https://www.karolinska.se/',  # Karolinska Universitetssjukhuset
    'https://www.aphp.fr/hopital/pitie-salpetriere',  # AP-HP - Hôpital Universitaire Pitié Salpêtrière
    'https://www.sheba.co.il/',  # Sheba Medical Center
    'https://www.usz.ch/',  # Universitätsspital Zürich
    'https://www.sgh.com.sg/',  # Singapore General Hospital (SGH)
    'https://www.uclahealth.org/',  # UCLA Health – Ronald Reagan Medical Center
    'https://www.chuv.ch/',  # Centre hospitalier universitaire vaudois (CHUV)
    'https://www.unispital-basel.ch/',  # Universitätsspital Basel
    'https://www.klinikum.uni-heidelberg.de/',  # Universitätsklinikum Heidelberg
    'https://stanfordhealthcare.org/',  # Stanford Health Care - Stanford Hospital
    'https://www.aphp.fr/hopital/europeen-georges-pompidou',  # AP-HP - Hôpital Européen Georges Pompidou
    'https://www.h.u-tokyo.ac.jp/',  # The University of Tokyo Hospital
    'https://www.brighamandwomens.org/',  # Brigham And Women's Hospital
    'https://www.mountsinai.org/',  # The Mount Sinai Hospital
    'https://www.rigshospitalet.dk/',  # Rigshospitalet - København
    'https://www.amc.seoul.kr/asan/main.do',  # Asan Medical Center
    'https://www.auh.dk/',  # Aarhus Universitetshospital
    'https://hospital.luke.ac.jp/',  # St. Luke's International Hospital
    'https://www.akhwien.at/',  # Allgemeines Krankenhaus der Stadt Wien
    'https://www.lmu-klinikum.de/',  # LMU Klinikum
    'https://www.mri.tum.de/',  # Klinikum rechts der Isar der Technischen Universität München
    'https://www.einstein.br/',  # Hospital Israelita Albert Einstein
    'https://oslo-universitetssykehus.no/',  # Oslo Universitetssykehus
    'https://sunnybrook.ca/',  # Sunnybrook Health Sciences Centre
    'https://www.nm.org/',  # Northwestern Memorial Hospital
    'https://www.mountsinai.on.ca/',  # Mount Sinai Hospital (Toronto)
    'https://www.amsterdamumc.org/',  # Amsterdam UMC
    'https://www.samsunghospital.com/',  # Samsung Medical Center
    'https://www.policlinicogemelli.it/',  # Policlinico Universitario A. Gemelli
    'https://www.guysandstthomas.nhs.uk/',  # St Thomas' Hospital
    'https://www.uofmhealth.org/',  # University of Michigan Health
    'https://www.chu-lille.fr/',  # CHU Lille - Hôpital Claude-Huriez
    'https://www.mh-hannover.de/',  # Medizinische Hochschule Hannover
    'https://www.yuhs.or.kr/en/hospitals/severance/',  # Severance Hospital - Yonsei University
    'https://www.cedars-sinai.org/',  # Cedars-Sinai Medical Center
    'https://www.umcutrecht.nl/',  # UMC Utrecht
    'https://www.snuh.org/',  # Seoul National University Hospital
    'https://www.uzleuven.be/en',  # UZ Leuven
    'https://www.kameda.com/',  # Kameda Medical Center
    'https://www.comunidad.madrid/hospital/lapaz',  # Hospital Universitario La Paz
    'https://www.nygh.on.ca/',  # North York General Hospital
    'https://www.uke.de/',  # Universitätsklinikum Hamburg-Eppendorf
    'https://www.ucsfhealth.org/',  # UCSF Medical Center
    'https://www.hus.fi/',  # Helsinki University Hospital
]


def scrape_hospital_data(hospital_url, retries=3):
    """Scrapes hospital data from a given URL with retry logic."""
    for attempt in range(retries):
        try:
            response = requests.get(hospital_url, timeout=10)
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            # Validate that the response contains data (not just an empty page)
            if len(response.content) == 0:
                print(f"Empty response from {hospital_url} on attempt {attempt + 1}")
                continue
            
            print(f"Successfully scraped data from {hospital_url}")
            return response.text
        except ConnectionError as ce:
            print(f"ConnectionError on attempt {attempt + 1} for {hospital_url}: {ce}")
            time.sleep(2)  # Wait for 2 seconds before retrying
        except requests.exceptions.HTTPError as he:
            print(f"HTTPError for {hospital_url}: {he}")
            break  # Stop retrying if it's an HTTP error
        except requests.exceptions.Timeout as te:
            print(f"TimeoutError for {hospital_url}: {te}")
            time.sleep(2)  # Wait for 2 seconds before retrying
        except Exception as e:
            print(f"An unexpected error occurred with {hospital_url}: {e}")
            break  # Handle any other exceptions and stop retrying
    return None  # Return None if all retries fail

def collect_all_hospital_data():
    """Collects data from all hospitals in the list and stores it."""
    all_hospital_data = []
    
    for url in hospital_urls:
        data = scrape_hospital_data(url)
        if data:
            # Log data for verification (optional)
            print(f"Data collected from {url} (length: {len(data)} characters)")
            all_hospital_data.append({'url': url, 'data': data})  # Store as a dictionary
        else:
            print(f"Skipping {url} due to repeated errors.")
    
    return all_hospital_data

def save_data_to_csv(hospital_data):
    """Saves the collected hospital data to a CSV file."""
    try:
        df = pd.DataFrame(hospital_data)  # Ensure pandas is used correctly
        df.to_csv("hospital_data.csv", index=False, encoding='utf-8')
        print("Data successfully written to hospital_data.csv.")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

# Main execution
if __name__ == "__main__":
    all_hospital_data = collect_all_hospital_data()
    
    if all_hospital_data:
        # Save the collected data to a CSV file
        save_data_to_csv(all_hospital_data)
    
    print("Data collection complete.")
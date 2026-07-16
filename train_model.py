import pandas as pd
import re
from ssl_checker import check_ssl_certificate
from urllib.parse import urlparse


data = pd.read_csv('data.csv')


trusted_domains = [
    'google.com', 'microsoft.com', 'apple.com', 'amazon.com',
    'stc.com.sa', 'alrajhibank.com.sa', 'spa.gov.sa', 'moi.gov.sa',
    'linkedin.com', 'github.com'
]

def is_trusted_domain(url):
    try:
        domain = urlparse(url).netloc.replace('www.', '')
        return 1 if domain in trusted_domains else 0
    except Exception:
        return 0


def extract_features(url):
    features = {}
    features['url_length'] = len(url)
    features['has_at_symbol'] = 1 if '@' in url else 0
    features['has_ip'] = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
    features['num_dots'] = url.count('.')
    features['has_https'] = 1 if url.startswith('https') else 0
    features['num_hyphens'] = url.count('-')
    features['has_valid_ssl'] = check_ssl_certificate(url)
    features['is_trusted_domain'] = is_trusted_domain(url)
    return features


feature_list = []
for url in data['url']:
    print(f"Processing: {url}")
    feature_list.append(extract_features(url))


features_df = pd.DataFrame(feature_list)


features_df['label'] = data['label']


print("\nExtracted features:")
print(features_df)


features_df.to_csv('features.csv', index=False)
print("\nFeatures saved to features.csv")
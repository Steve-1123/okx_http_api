# okx_http_api

api for OKX

## Requirements

```text
certifi==2025.1.31
charset-normalizer==3.4.1
idna==3.10
python-dotenv==1.0.1
requests==2.32.3
urllib3==2.3.0
```

Use `pip3 install requirements.txt` to install all the requirements.

## Config

Need to replace the config str in `.env`, and click [here](https://www.okx.com/zh-hans/account/my-api/batch-add "OKX Api Appliance") to apply for your own OKX API Key.

```text
OKX_SECRET_KEY=xxx
OKX_API_KEY=xxx
OKX_PASSPHRASE=xxx
OKX_SIMULATED_FLAG=1 # 1 -> simulated trade | 2 -> real trade
```

# Easy OpenDNS switcher

This program allows you to easily switch restrictions/permissions for domains using OpenDNS.

## Requirements

- Python3
- Google chrome
- OpenDNS account

## Usage

```shell
git clone https://github.com/ittk1229/easy-opendns-switcher.git
cd easy-opendns-switcher
pip install -r requirements.txt
python main.py
```

Before execute `main.py`, you should edit the two json files below.

### user_info.json

Please create `user_info.json` in the same folder with your e-mail address, password, and network_id as follow.

```json:login_information.json
{
    "mail": "example@examp.com",
    "password": "example",
    "network_id": "example"
}
```

**DO NOT** make your `user_info.json` public.

### black_list.json

Please add any domains you want to blacklist to `black_list.json`.

```json:black_list.json
["twitter.com", "youtube.com", "facebook.com"]
```

## Note

I don't test environment under Mac.

## Author

- ittk1229

## Licence

"Easy OpenDNS switcher" is under [MIT Licence](https://en.wikipedia.org/wiki/MIT_License).

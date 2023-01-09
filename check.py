import requests
import time

filename = "links"

working = "working"

def check():
    with open(filename + ".txt", "r") as file:
        lines = file.readlines()
        file.close()
    for line in lines:
        print("\033c")
        start = time.time()
        r = requests.get("https://discordapp.com/api/v6/entitlements/gift-codes/" + line[21:] + "?with_application=false&with_subscription_plan=true")
        if r.status_code == 200:
            with open(working + ".txt", "a") as file:
                file.write(line)
                file.close()
        end = time.time()
        print("Checked " + str(lines.index(line)) + " out of " + str(len(lines)) + " links")
        print("Percentage: " + str(round((lines.index(line) / len(lines)) * 100)) + "%")
        if round((end - start) * len(lines) - (end - start) * lines.index(line)) > 60:
            if round((end - start) * len(lines) - (end - start) * lines.index(line)) > 3600:
                print("Estimated time left: " + str(round((round((end - start) * len(lines) - (end - start) * lines.index(line)) / 60) / 60, 2)) + " hours")
            else:
                print("Estimated time left: " + str(round(round((end - start) * len(lines) - (end - start) * lines.index(line)) / 60, 2)) + " minutes")
        else:
            print("Estimated time left: " + str(round((end - start) * len(lines) - (end - start) * lines.index(line))) + " seconds")

check()
print("Done! " + str(len(open(working + ".txt").readlines())) + " working links put into " + working + ".txt")
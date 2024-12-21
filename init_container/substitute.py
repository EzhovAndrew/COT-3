import os
import json

def main():
    with open("user_policy.json") as f:
        data = f.read()
    data = data.replace("${bucket_name}", os.getenv("BUCKET_NAME"))
    data = json.loads(data)
    with open("policy.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()
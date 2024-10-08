import json
import os
import time

import requests
from get_chrome_driver import GetChromeDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm


def main():
    # Get settings from settings.json
    with open("settings.json") as f:
        settings = json.load(f)
        user_id = settings["user_id"]

    with open("submissions/LastUpdate") as f:
        last_update = int(f.read())

    api_url = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions/?user={user_id}&from_second={last_update}"

    # Get submissions
    res = requests.get(api_url)
    submissions = res.json()

    if not submissions:
        return

    # Extract get data
    submissions.sort(key=lambda x: x["id"])

    with open("submissions/LastUpdate", "w") as f:
        f.write(str(submissions[-1]["epoch_second"] + 1))

    submission_div_contest = dict()

    for submission in submissions:
        if submission["result"] != "AC":
            continue
        contest_id = submission["contest_id"]
        if contest_id not in submission_div_contest:
            submission_div_contest[contest_id] = []
        submission_div_contest[contest_id].append(submission)

    # Get and save submission code
    get_driver = GetChromeDriver()
    get_driver.install()

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)

    root_dir = "submissions"
    with tqdm(submission_div_contest.items()) as pbar1:
        for contest_id, submissions in pbar1:
            pbar1.set_description(contest_id)
            contest_dir = f"{root_dir}/{contest_id}"
            os.makedirs(contest_dir, exist_ok=True)

            with tqdm(submissions, leave=False) as pbar2:
                for submission in pbar2:
                    problem_id = submission["problem_id"]
                    pbar2.set_description(problem_id)
                    if "C++" in submission["language"]:
                        ext = "cpp"
                    elif "Python" in submission["language"]:
                        ext = "py"
                    path = f"{contest_dir}/{problem_id}.{ext}"

                    submission_url = f"https://atcoder.jp/contests/{contest_id}/submissions/{str(submission['id'])}"
                    driver.get(submission_url)

                    script = "return ace.edit('submission-code').getValue();"
                    source_code = driver.execute_script(script)

                    with open(path, "w") as f:
                        f.write(source_code)

                    time.sleep(3)
    driver.quit()


if __name__ == "__main__":
    main()

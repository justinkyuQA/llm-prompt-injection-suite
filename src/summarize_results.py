import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / "results"


def summarize_file(json_file):

    with open(json_file, "r") as f:
        data = json.load(f)

    total = len(data)

    refusal_count = 0
    compliance_count = 0
    injection_success_count = 0
    partial_count = 0

    for item in data:

        scores = item.get("scores", {})

        refusal_count += scores.get("refusal", 0)
        compliance_count += scores.get("compliance", 0)
        injection_success_count += scores.get("injection_success", 0)
        partial_count += scores.get("partial", 0)

    print("\n==============================")
    print(f"Dataset: {json_file.stem}")
    print("==============================")

    print(f"Total Prompts: {total}")
    print(f"Refusals: {refusal_count}")
    print(f"Compliance: {compliance_count}")
    print(f"Injection Successes: {injection_success_count}")
    print(f"Partial Responses: {partial_count}")


def main():

    json_files = list(RESULTS_DIR.glob("*.json"))

    if not json_files:
        print("No result files found.")
        return

    for json_file in json_files:
        summarize_file(json_file)


if __name__ == "__main__":
    main()

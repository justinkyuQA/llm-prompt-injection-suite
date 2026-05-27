import subprocess
from pathlib import Path


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

PROMPTS_DIR = BASE_DIR / "prompts"
RESULTS_DIR = BASE_DIR / "results"


def main():

    print("\n=== LLM Prompt Injection Batch Runner ===\n")

    # Find all .txt files in prompts folder
    prompt_files = list(PROMPTS_DIR.glob("*.txt"))

    if not prompt_files:
        print("No prompt datasets found.")
        return

    for prompt_file in prompt_files:

        dataset_name = prompt_file.stem
        output_file = RESULTS_DIR / f"{dataset_name}_results.json"

        print(f"\nRunning dataset: {prompt_file.name}")

        command = [
            "python",
            str(BASE_DIR / "src" / "evaluator.py"),
            "--dataset",
            f"prompts/{prompt_file.name}",
            "--output",
            f"results/{dataset_name}_results.json"
        ]

        result = subprocess.run(command)

        if result.returncode == 0:
            print(f"SUCCESS: {output_file.name}")
        else:
            print(f"FAILED: {prompt_file.name}")

    print("\n=== Batch Evaluation Complete ===\n")


if __name__ == "__main__":
    main()

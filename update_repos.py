import os
import subprocess
import shutil

def update_sub_repos():
    """
    Updates all Git sub-repositories in the current directory.
    - Pulls the latest changes for each sub-repo.
    - Removes the .git directory after a successful pull.
    - Logs errors for non-Git directories or failed pulls.
    """
    root_dir = os.getcwd()
    sub_dirs = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]

    for sub_dir in sub_dirs:
        repo_path = os.path.join(root_dir, sub_dir)
        git_dir = os.path.join(repo_path, ".git")

        if os.path.exists(git_dir):
            print(f"Processing repository: {sub_dir}")
            try:
                # Change directory to the sub-repo and run git pull
                print(f"  - Pulling latest changes for {sub_dir}...")
                subprocess.run(
                    ["git", "pull"],
                    cwd=repo_path,
                    check=True,
                    capture_output=True,
                    text=True
                )
                print(f"  - Successfully pulled changes for {sub_dir}.")

                # After successful pull, remove the .git directory
                try:
                    print(f"  - Removing .git directory from {sub_dir}...")
                    shutil.rmtree(git_dir)
                    print(f"  - Successfully removed .git directory from {sub_dir}.")
                except OSError as e:
                    print(f"  - Error removing .git directory from {sub_dir}: {e}")

            except subprocess.CalledProcessError as e:
                print(f"  - Error pulling changes for {sub_dir}:")
                print(f"    - Return code: {e.returncode}")
                print(f"    - stdout: {e.stdout.strip()}")
                print(f"    - stderr: {e.stderr.strip()}")
            except Exception as e:
                print(f"  - An unexpected error occurred with {sub_dir}: {e}")
        else:
            print(f"Skipping '{sub_dir}': Not a Git repository.")

if __name__ == "__main__":
    update_sub_repos()
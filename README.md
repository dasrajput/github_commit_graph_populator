# Just Commit

This repository contains a Python script to generate a realistic-looking commit history for your GitHub profile.

## For Humans:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dasrajput/justcommit.git
    cd justcommit
    ```
2.  **Configure your Git username and email:**
    ```bash
    git config user.name "Your Name"
    git config user.email "your.email@example.com"
    ```
3.  **Run the script:**
    *   To generate commits from the beginning of the current year until today:
        ```bash
        python generate_commits.py
        ```
    *   To specify a date range:
        ```bash
        python generate_commits.py --start-date YYYY-MM-DD --end-date YYYY-MM-DD
        ```
        (Replace `YYYY-MM-DD` with the desired dates.)

4.  **Push the commits to your repository:**
    ```bash
    git remote set-url origin <your-repository-url>
    git push -u origin main
    ```

## For AI Agents:

To generate a commit history, follow these steps:

1.  **Verify git configuration:**
    *   Run `git config user.name` and `git config user.email` to ensure they are set.
2.  **Execute the script:**
    *   To generate commits for a specific date range, run the following command, replacing the dates as needed:
        ```bash
        python generate_commits.py --start-date 2025-01-01 --end-date 2025-12-31
        ```
    *   If no dates are provided, the script will default to generating commits from the beginning of the current year to the current date.
3.  **Push to the remote repository:**
    *   Run `git push -u origin main`.
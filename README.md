# The Supreme Court of Our Relationship ❤️

A playful Streamlit relationship quiz with 14 questions, evasive loving
answers, a dramatic court review, and a romantic final verdict.

## What the app includes

- One-question-at-a-time interface
- Progress bar and answer tracking
- Loving answers that evade the cursor on desktop
- Tap rejection messages on phones and tablets
- Animated relationship review and system error
- Dramatic final verdict, falling hearts, and restart button
- Responsive design for computers and phones

## Personalize the names

Open `app.py` and edit these two lines near the top:

```python
PARTNER_NAME = "My Love"
YOUR_NAME = "Rabbi"
```

You can also edit the questions in the `questions` list inside `app.py`.

## Run with Anaconda on Windows

1. Download and extract the project ZIP.
2. Open **Anaconda Prompt**.
3. Move into the extracted folder. For example:

   ```bash
   cd "C:\Users\rabbi\My projects\relationship_court_app"
   ```

4. Create a Python 3.11 environment:

   ```bash
   conda create -n love-court python=3.11 -y
   ```

5. Activate it:

   ```bash
   conda activate love-court
   ```

6. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

7. Start the app:

   ```bash
   streamlit run app.py
   ```

The app will open automatically in your browser. Jupyter Notebook does not
need to be running.

## Upload to GitHub

1. Create a new empty GitHub repository.
2. Select **Add file → Upload files**.
3. Upload the contents of this project folder, including:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
   - `.streamlit/config.toml`
4. Commit the files.

GitHub may hide files and folders beginning with a dot. If you cannot upload
`.streamlit/config.toml` in the browser, the app will still run correctly; that
file only provides additional Streamlit theme settings.

## Deploy on Streamlit Community Cloud

1. Sign in at [share.streamlit.io](https://share.streamlit.io/).
2. Choose **Create app**.
3. Select your GitHub repository and branch.
4. Set the main file path to `app.py`.
5. Open **Advanced settings** and choose Python 3.11 if that option is shown.
6. Deploy the app and share its public URL.

## Important behavior

The app intentionally allows only the emotionally negative answer to be
recorded. The loving answer moves away on desktop and rejects the tap on mobile.
This behavior is implemented as a playful visual joke inside the quiz.


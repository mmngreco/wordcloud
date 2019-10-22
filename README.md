# Install

```bash
git clone https://github.com/mmngreco/wordcloud.git
cd wordcloud
pip install -r requirements.txt
```

# Examples of use

1. Modify `words.txt` file with your own words.
1. Simply run:

    ```bash
    python main.py     # by default it makes 5 images
    python main.py 10  # you can specify the number of images
    ```

Images will be stored in `build` folder. This program uses `words.txt` to get a list of words to word cloud picture.


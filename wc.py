import numpy as np
from cycler import cycle
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path

from wordcloud import (
    WordCloud,
    STOPWORDS,
    ImageColorGenerator,
)


def plot_wordcloud(show=False):
    global i
    plt.imshow(wc.recolor(), interpolation="bilinear")
    plt.tight_layout(pad=0)
    plt.axis("off")
    if show:
        plt.show()
    now = datetime.now()
    fname = Path("build/taza_v%s_%s.png" % (i, now))
    print("writing: %s" % fname)
    plt.savefig(
        fname,
        dpi=900,
        quality=100,
        transparent=True,
    )
    i += 1


def main(n):
    global i, wc
    i = 0
    clist = [
        (0.2, 0.0, 0.4),
        (0.4, 0.4, 0.4),
        (155 / 255, 132 / 255, 178 / 255),
    ]

    newcmp = LinearSegmentedColormap.from_list("testCmap", clist, N=256)
    cm = newcmp(np.linspace(0, 1, 256))

    with open("words.txt") as f:
        text = f.read()

    scale = 273 / 555 * 0.9
    w = 900
    h = int(w * scale)

    wordcloud = WordCloud(
        width=w,
        height=h,
        margin=1,
        background_color="white",
        colormap=newcmp,
        min_font_size=10,
        font_path=str(Path("fonts/Cabin-Bold.ttf")),
    )
    wc = wordcloud.generate(text)

    for j in range(n):
        plot_wordcloud()

if __name__ == "__main__":
    import sys
    try:
        n = int(sys.argv[1])
    except:
        n = 5
    main(n=n)
